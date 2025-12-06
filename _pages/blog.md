---
layout: single
title: "Blog"
permalink: /blog/
author_profile: true
---

This is a blog test.

<style>
  .blog-post {
    margin-bottom: 2.5rem;
    padding: 1.5rem;
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    background-color: #fafafa;
    transition: all 0.3s ease;
  }
  
  .blog-post:hover {
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    background-color: #f5f5f5;
  }
  
  .blog-post-title {
    margin-top: 0;
    margin-bottom: 0.5rem;
  }
  
  .blog-post-title a {
    color: #2c3e50;
    text-decoration: none;
  }
  
  .blog-post-title a:hover {
    color: #0066cc;
    text-decoration: underline;
  }
  
  .blog-post-meta {
    font-size: 0.95rem;
    color: #666;
    margin-bottom: 1rem;
  }
  
  .blog-post-excerpt {
    font-size: 0.95rem;
    line-height: 1.6;
    color: #333;
  }
</style>

<div class="blog-posts">
{% if site.posts.size > 0 %}
  {% for post in site.posts %}
    <div class="blog-post">
      <h3 class="blog-post-title">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h3>
      <div class="blog-post-meta">
        <span class="post-date">📅 {{ post.date | date: "%B %d, %Y" }}</span>
        {% if post.categories.size > 0 %}
          <span style="margin-left: 1rem;">📁 {{ post.categories | join: ", " }}</span>
        {% endif %}
      </div>
      {% if post.excerpt %}
        <div class="blog-post-excerpt">
          {{ post.excerpt | strip_html }}
        </div>
      {% endif %}
    </div>
  {% endfor %}
{% else %}
  <p style="text-align: center; color: #999; font-size: 1.1rem;">No posts yet. Check back soon! 📝</p>
{% endif %}
</div>
