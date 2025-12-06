---
layout: archive
title: "Blog"
permalink: /blog/
author_profile: true
---

This is a test blog page.

{% include base_path %}
{% assign posts = site.posts | where_exp: "post", "post.hidden != true" %}

{% if posts.size > 0 %}
  <h2>Recent Posts</h2>
  <ul>
    {% for post in posts %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span class="post-date">{{ post.date | date: "%B %d, %Y" }}</span>
        {% if post.excerpt %}<p>{{ post.excerpt }}</p>{% endif %}
      </li>
    {% endfor %}
  </ul>
{% else %}
  <p>No posts yet. Check back soon!</p>
{% endif %}
