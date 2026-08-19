---
layout: default
title: "Miscellaneous"
permalink: /miscellaneous/
author_profile: true
---

<div class="misc-intro">
  <p>
    Outside of work, you’ll often find me at the gym, playing soccer, road cycling, or hiking.
    I also enjoy playing table tennis and the piano from time to time.
  </p>
  <p>
    I once drove from Los Angeles all the way to Florida on a cross-country road trip across the US.
    I have also climbed Mount Siguniang (四姑娘山) and Aotaina Snow Mountain (奥太娜雪山) in China,
    and I hope to climb many more in the future.
  </p>
  <p>
    I was the captain of my undergraduate varsity soccer team, and later played for the
    <a href="https://www.jhucfc.org/home" target="_blank" rel="noopener">Johns Hopkins University Chinese Football Club</a>
    during the 2022–2024 seasons.
  </p>
</div>

{% comment %}
  Photos are picked up automatically from /images/misc/.
  Drop image files in that folder — no code change needed.
  Files are ordered by filename, so prefix them (01_, 02_, ...) to control the order.
  Optional captions live in _data/misc_photos.yml.
{% endcomment %}
{% assign misc_files = site.static_files | where_exp: "f", "f.path contains '/images/misc/'" | sort: "name" %}
{% assign photo_count = 0 %}
{% for f in misc_files %}
  {% assign ext = f.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" or ext == ".webp" or ext == ".gif" or ext == ".avif" %}
    {% assign photo_count = photo_count | plus: 1 %}
  {% endif %}
{% endfor %}

{% if photo_count > 0 %}
<div class="misc-carousel" id="misc-carousel" tabindex="0" role="group" aria-roledescription="carousel" aria-label="Life photos">
  <div class="misc-carousel__viewport">
    <div class="misc-carousel__track">
      {% for f in misc_files %}
        {% assign ext = f.extname | downcase %}
        {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" or ext == ".webp" or ext == ".gif" or ext == ".avif" %}
          {% assign cap = "" %}
          {% if site.data.misc_photos %}
            {% assign meta = site.data.misc_photos | where: "file", f.name | first %}
            {% if meta and meta.caption %}{% assign cap = meta.caption %}{% endif %}
          {% endif %}
          <div class="misc-slide" role="group" aria-roledescription="slide" aria-label="{{ forloop.index }} of {{ photo_count }}">
            <img class="misc-slide__bg" src="{{ f.path | relative_url }}" alt="" aria-hidden="true" loading="lazy">
            <img class="misc-slide__img" src="{{ f.path | relative_url }}" alt="{{ cap | default: f.basename | escape }}" loading="lazy">
            {% if cap != "" %}<div class="misc-slide__caption">{{ cap }}</div>{% endif %}
          </div>
        {% endif %}
      {% endfor %}
    </div>

    {% if photo_count > 1 %}
    <button class="misc-carousel__nav misc-carousel__nav--prev" type="button" aria-label="Previous photo">
      <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
    </button>
    <button class="misc-carousel__nav misc-carousel__nav--next" type="button" aria-label="Next photo">
      <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
    </button>
    {% endif %}

    <button class="misc-carousel__expand" type="button" aria-label="View full size">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3M16 3h3a2 2 0 0 1 2 2v3M8 21H5a2 2 0 0 1-2-2v-3M16 21h3a2 2 0 0 0 2-2v-3"></path></svg>
    </button>
  </div>

  {% if photo_count > 1 %}<div class="misc-carousel__dots" role="tablist" aria-label="Choose photo"></div>{% endif %}
</div>

<div class="misc-lightbox" id="misc-lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer" hidden>
  <button class="misc-lightbox__close" type="button" aria-label="Close">&times;</button>
  <figure class="misc-lightbox__figure">
    <img class="misc-lightbox__img" src="" alt="">
    <figcaption class="misc-lightbox__caption"></figcaption>
  </figure>
</div>
{% else %}
<div class="misc-empty">
  <p>📷 No photos here yet — drop image files into <code>images/misc/</code> and they will show up automatically.</p>
</div>
{% endif %}

<style>
  .misc-intro {
    max-width: 900px;
    margin: 2.5rem auto 2rem auto;
  }

  .misc-intro p + p { margin-top: 0.9rem; }

  .misc-intro p {
    font-size: 1rem;
    line-height: 1.7;
    color: #333;
    margin-bottom: 1rem;
  }

  .misc-intro a {
    color: #0066cc;
    text-decoration: none;
    border-bottom: 1px solid rgba(0, 102, 204, 0.3);
  }

  .misc-intro a:hover {
    text-decoration: none;
    border-bottom-color: #0066cc;
  }

  /* --- Sliding carousel --- */
  .misc-carousel {
    position: relative;
    max-width: 485px;
    margin: 0 auto 2rem auto;
    border-radius: 12px;
    overflow: hidden;
    background-color: #111;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.18);
    outline: none;
  }

  .misc-carousel:focus-visible {
    box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.5), 0 4px 20px rgba(0, 0, 0, 0.18);
  }

  .misc-carousel__viewport {
    position: relative;
    width: 100%;
    padding-bottom: 62.5%; /* 16:10 frame */
    overflow: hidden;
    touch-action: pan-y;
  }

  .misc-carousel__track {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    transition: transform 0.45s cubic-bezier(0.4, 0, 0.2, 1);
    will-change: transform;
  }

  .misc-slide {
    position: relative;
    flex: 0 0 100%;
    width: 100%;
    height: 100%;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #111;
  }

  /* Blurred copy of the photo fills the frame so portrait shots don't sit on empty bars */
  .misc-slide__bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: blur(28px) brightness(0.5);
    transform: scale(1.2);
    z-index: 0;
  }

  .misc-slide__img {
    position: relative;
    z-index: 1;
    max-width: 100%;
    max-height: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
  }

  .misc-slide__caption {
    position: absolute;
    z-index: 2;
    left: 0;
    right: 0;
    bottom: 0;
    padding: 2.5rem 1.25rem 1rem 1.25rem;
    color: #fff;
    font-size: 0.95rem;
    line-height: 1.4;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.8);
    background: linear-gradient(to top, rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0));
    pointer-events: none;
  }

  .misc-carousel__nav,
  .misc-carousel__expand {
    position: absolute;
    z-index: 3;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    border-radius: 50%;
    background-color: rgba(0, 0, 0, 0.4);
    color: #fff;
    cursor: pointer;
    padding: 0;
    opacity: 0.75;
    transition: opacity 0.2s ease, background-color 0.2s ease;
  }

  .misc-carousel__nav:hover,
  .misc-carousel__expand:hover {
    opacity: 1;
    background-color: rgba(0, 0, 0, 0.65);
  }

  .misc-carousel__nav {
    top: 50%;
    transform: translateY(-50%);
    width: 44px;
    height: 44px;
  }

  .misc-carousel__nav--prev { left: 0.75rem; }
  .misc-carousel__nav--next { right: 0.75rem; }

  .misc-carousel__expand {
    top: 0.75rem;
    right: 0.75rem;
    width: 34px;
    height: 34px;
  }

  .misc-carousel__dots {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 0.4rem;
    padding: 0.7rem 0.75rem;
    background-color: #111;
  }

  .misc-carousel__dot {
    width: 8px;
    height: 8px;
    padding: 0;
    border: none;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.35);
    cursor: pointer;
    transition: background-color 0.25s ease, width 0.25s ease;
  }

  .misc-carousel__dot:hover { background-color: rgba(255, 255, 255, 0.6); }

  .misc-carousel__dot[aria-selected="true"] {
    width: 20px;
    border-radius: 999px;
    background-color: #fff;
  }

  @media (max-width: 600px) {
    .misc-carousel { border-radius: 8px; }
    .misc-carousel__nav { width: 34px; height: 34px; }
    .misc-carousel__nav--prev { left: 0.4rem; }
    .misc-carousel__nav--next { right: 0.4rem; }
    .misc-slide__caption { font-size: 0.85rem; padding: 2rem 0.9rem 0.8rem 0.9rem; }
  }

  @media (prefers-reduced-motion: reduce) {
    .misc-carousel__track { transition: none; }
  }

  .misc-empty {
    max-width: 485px;
    margin: 0 auto 2rem auto;
    padding: 2rem 1rem;
    border: 1px dashed #d0d0d0;
    border-radius: 5px;
    text-align: center;
    color: #999;
  }

  .misc-empty p { margin: 0; font-size: 0.95rem; }

  .misc-empty code {
    background-color: #f2f2f2;
    padding: 0.1rem 0.35rem;
    border-radius: 3px;
    color: #555;
  }

  /* --- Full-size viewer --- */
  .misc-lightbox {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 3rem 1rem;
    background-color: rgba(0, 0, 0, 0.92);
  }

  .misc-lightbox[hidden] { display: none; }

  .misc-lightbox__figure {
    margin: 0;
    max-width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .misc-lightbox__img {
    max-width: 100%;
    max-height: 82vh;
    width: auto;
    height: auto;
    border-radius: 4px;
  }

  .misc-lightbox__caption {
    margin-top: 0.8rem;
    color: #eee;
    font-size: 0.9rem;
    text-align: center;
    max-width: 60ch;
  }

  .misc-lightbox__caption:empty { display: none; }

  .misc-lightbox__close {
    position: absolute;
    top: 0.75rem;
    right: 1.25rem;
    background: none;
    border: none;
    color: #fff;
    font-size: 2.5rem;
    line-height: 1;
    cursor: pointer;
    opacity: 0.7;
    transition: opacity 0.2s ease;
  }

  .misc-lightbox__close:hover { opacity: 1; }

  body.misc-lightbox-open { overflow: hidden; }
</style>

<script>
(function () {
  var root = document.getElementById('misc-carousel');
  if (!root) { return; }

  var track = root.querySelector('.misc-carousel__track');
  var slides = Array.prototype.slice.call(root.querySelectorAll('.misc-slide'));
  var dotsBar = root.querySelector('.misc-carousel__dots');
  var btnPrev = root.querySelector('.misc-carousel__nav--prev');
  var btnNext = root.querySelector('.misc-carousel__nav--next');
  var btnExpand = root.querySelector('.misc-carousel__expand');
  var box = document.getElementById('misc-lightbox');
  var total = slides.length;
  var current = 0;
  var dots = [];

  if (total === 0) { return; }

  if (dotsBar) {
    for (var i = 0; i < total; i++) {
      var dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'misc-carousel__dot';
      dot.setAttribute('role', 'tab');
      dot.setAttribute('aria-label', 'Photo ' + (i + 1));
      dot.setAttribute('aria-selected', i === 0 ? 'true' : 'false');
      (function (index) {
        dot.addEventListener('click', function () { goTo(index); });
      })(i);
      dotsBar.appendChild(dot);
      dots.push(dot);
    }
  }

  function goTo(index) {
    current = (index % total + total) % total;
    track.style.transform = 'translateX(' + (-100 * current) + '%)';
    for (var i = 0; i < dots.length; i++) {
      dots[i].setAttribute('aria-selected', i === current ? 'true' : 'false');
    }
    for (var j = 0; j < slides.length; j++) {
      slides[j].setAttribute('aria-hidden', j === current ? 'false' : 'true');
    }
  }

  if (btnPrev) { btnPrev.addEventListener('click', function () { goTo(current - 1); }); }
  if (btnNext) { btnNext.addEventListener('click', function () { goTo(current + 1); }); }

  root.addEventListener('keydown', function (e) {
    if (box && !box.hidden) { return; }
    if (e.key === 'ArrowLeft') { e.preventDefault(); goTo(current - 1); }
    else if (e.key === 'ArrowRight') { e.preventDefault(); goTo(current + 1); }
  });

  var startX = null;
  var startY = null;
  var viewport = root.querySelector('.misc-carousel__viewport');

  viewport.addEventListener('touchstart', function (e) {
    if (e.touches.length !== 1) { return; }
    startX = e.touches[0].clientX;
    startY = e.touches[0].clientY;
  }, { passive: true });

  viewport.addEventListener('touchend', function (e) {
    if (startX === null) { return; }
    var dx = e.changedTouches[0].clientX - startX;
    var dy = e.changedTouches[0].clientY - startY;
    startX = null;
    startY = null;
    if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)) {
      goTo(dx < 0 ? current + 1 : current - 1);
    }
  }, { passive: true });

  if (btnExpand && box) {
    var boxImg = box.querySelector('.misc-lightbox__img');
    var boxCap = box.querySelector('.misc-lightbox__caption');
    var btnClose = box.querySelector('.misc-lightbox__close');

    var openBox = function () {
      var img = slides[current].querySelector('.misc-slide__img');
      var cap = slides[current].querySelector('.misc-slide__caption');
      boxImg.src = img.getAttribute('src');
      boxImg.alt = img.getAttribute('alt') || '';
      boxCap.textContent = cap ? cap.textContent.trim() : '';
      box.hidden = false;
      document.body.classList.add('misc-lightbox-open');
      btnClose.focus();
    };

    var closeBox = function () {
      box.hidden = true;
      boxImg.src = '';
      document.body.classList.remove('misc-lightbox-open');
      btnExpand.focus();
    };

    btnExpand.addEventListener('click', openBox);
    btnClose.addEventListener('click', closeBox);
    box.addEventListener('click', function (e) {
      if (e.target === box || e.target === box.querySelector('.misc-lightbox__figure')) { closeBox(); }
    });
    box.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closeBox(); }
    });
  }

  goTo(0);
})();
</script>
