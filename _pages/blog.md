---
layout: single
title: "Blog"
permalink: /blog/
author_profile: true
---

Welcome to my blog! Here I share thoughts on research, computational biology, AI for science, and related topics.

## Recent Posts

{% for post in site.posts %}
- **[{{ post.title }}]({{ post.url }})** - *{{ post.date | date: "%B %d, %Y" }}*
  
  {{ post.excerpt | strip_html }}

{% endfor %}
