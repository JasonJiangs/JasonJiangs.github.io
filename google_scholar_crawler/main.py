"""Scrape a Google Scholar profile into the JSON the homepage consumes.

Deliberately stdlib-only. The previous version used ``scholarly==1.5.1``
(released 2020), which no longer parses current Scholar markup and drags in a
dozen transitive dependencies that break on modern runners. Everything needed
here is a single profile page, so we parse it directly.

Output (``results/gs_data.json``) keeps the schema
``_includes/fetch_google_scholar_stats.html`` already reads:

    {"scholar_id", "citedby", "updated",
     "publications": {"<author_pub_id>": {"bib": {"title", "pub_year"},
                                          "num_citations": int}}}

Scholar rate-limits datacenter IPs, so a blocked fetch is reported as a
warning and exits 0 *without* writing anything. Keeping yesterday's numbers
on the site is strictly better than replacing them with an error page.
"""

import html
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

PROFILE_URL = (
    "https://scholar.google.com/citations"
    "?user={user}&hl=en&view_op=list_works&sortby=pubdate&cstart={cstart}&pagesize={pagesize}"
)
PAGE_SIZE = 100
MAX_PAGES = 10
ATTEMPTS = 4

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
]

# One <tr> per publication. The citation cell is empty for uncited work, and
# the year cell is empty for work with no publication date, hence the
# permissive inner groups.
ROW_RE = re.compile(
    r'<tr class="gsc_a_tr">.*?citation_for_view=([^"&]+)".*?'
    r'class="gsc_a_at">(.*?)</a>.*?'
    r'<td class="gsc_a_c">(.*?)</td>.*?'
    r'<td class="gsc_a_y">(.*?)</td>',
    re.DOTALL,
)
CITES_RE = re.compile(r'class="gsc_a_ac[^"]*"[^>]*>(\d+)</a>')
YEAR_RE = re.compile(r">(\d{4})<")
TAG_RE = re.compile(r"<[^>]+>")
# Right-hand "Cited by / h-index / i10-index" table: All, then Since <year>.
STATS_RE = re.compile(r'class="gsc_rsb_std">(\d+)</td>')
NAME_RE = re.compile(r'id="gsc_prf_in"[^>]*>(.*?)<')
BLOCKED_RE = re.compile(
    r"(?:/sorry/|unusual traffic|not a robot|captcha)", re.IGNORECASE
)


def warn(message):
    """Emit a GitHub Actions warning annotation (plain text when run locally)."""
    print("::warning::" + message if os.environ.get("GITHUB_ACTIONS") else message)


def fetch(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_with_retry(url):
    """Return the page, or None if Scholar refused us on every attempt."""
    for attempt in range(1, ATTEMPTS + 1):
        try:
            page = fetch(url)
        except urllib.error.HTTPError as error:
            page, reason = None, "HTTP %s" % error.code
        except Exception as error:  # timeouts, DNS, TLS resets
            page, reason = None, "%s: %s" % (type(error).__name__, error)
        else:
            if BLOCKED_RE.search(page):
                page, reason = None, "rate-limited (CAPTCHA / sorry page)"
            elif 'id="gsc_prf_in"' not in page:
                page, reason = None, "unexpected page layout"
            else:
                return page

        if attempt < ATTEMPTS:
            delay = 2 ** attempt + random.uniform(0, 2)
            print("attempt %d/%d failed (%s); retrying in %.1fs"
                  % (attempt, ATTEMPTS, reason, delay))
            time.sleep(delay)
        else:
            warn("Google Scholar fetch failed after %d attempts (%s)."
                 % (ATTEMPTS, reason))
    return None


def text_of(fragment):
    return html.unescape(TAG_RE.sub("", fragment)).strip()


def parse_publications(page):
    publications = {}
    for pub_id, title, cites_cell, year_cell in ROW_RE.findall(page):
        cites = CITES_RE.search(cites_cell)
        year = YEAR_RE.search(year_cell)
        publications[html.unescape(pub_id)] = {
            "author_pub_id": html.unescape(pub_id),
            "bib": {
                "title": text_of(title),
                "pub_year": year.group(1) if year else "",
            },
            "num_citations": int(cites.group(1)) if cites else 0,
        }
    return publications


def main():
    user = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not user:
        print("GOOGLE_SCHOLAR_ID is not set. Add it under "
              "Settings -> Secrets and variables -> Actions.", file=sys.stderr)
        return 1

    first_page = fetch_with_retry(
        PROFILE_URL.format(user=user, cstart=0, pagesize=PAGE_SIZE)
    )
    if first_page is None:
        print("Leaving the published data untouched.")
        return 0

    publications = parse_publications(first_page)
    # Scholar caps a page at 100 works; walk forward until a page adds nothing.
    for page_index in range(1, MAX_PAGES):
        if len(publications) < page_index * PAGE_SIZE:
            break
        time.sleep(random.uniform(1.5, 3.5))
        page = fetch_with_retry(
            PROFILE_URL.format(user=user, cstart=page_index * PAGE_SIZE,
                               pagesize=PAGE_SIZE)
        )
        if page is None:
            break
        before = len(publications)
        publications.update(parse_publications(page))
        if len(publications) == before:
            break

    if not publications:
        warn("Parsed 0 publications - Scholar's markup may have changed. "
             "Leaving the published data untouched.")
        return 0

    stats = [int(value) for value in STATS_RE.findall(first_page)]
    # Six cells: citedby, citedby5y, hindex, hindex5y, i10index, i10index5y.
    keys = ["citedby", "citedby5y", "hindex", "hindex5y", "i10index", "i10index5y"]
    name = NAME_RE.search(first_page)

    author = {
        "scholar_id": user,
        "name": html.unescape(name.group(1)).strip() if name else "",
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "publications": publications,
    }
    author.update(dict(zip(keys, stats)))
    # Fall back to the sum of per-paper counts if the summary table moved.
    if "citedby" not in author:
        author["citedby"] = sum(p["num_citations"] for p in publications.values())

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as handle:
        json.dump(author, handle, ensure_ascii=False)
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as handle:
        json.dump({"schemaVersion": 1, "label": "citations",
                   "message": str(author["citedby"])}, handle, ensure_ascii=False)

    print("%s: %d citations across %d publications (h-index %s)"
          % (author["name"] or user, author["citedby"], len(publications),
             author.get("hindex", "?")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
