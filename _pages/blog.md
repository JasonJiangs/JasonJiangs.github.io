---
layout: single
title: "Blog"
permalink: /blog/
author_profile: true
---
<h1 class="page-title">Resources</h1>

<style>
  .resources-container {
    width: 70%;
    margin: 2rem auto;
  }
  
  .page-title {
    text-align: center;
    margin: 2rem 0 1.5rem 0;
    font-size: 2em;
    font-weight: bold;
    color: #2c3e50;
  }
  
  .resource-section-title {
    font-size: 1.3em;
    font-weight: 600;
    color: #2c3e50;
    margin-top: 2rem;
    margin-bottom: 0.8rem;
    border-bottom: 2px solid #e0e0e0;
    padding-bottom: 0.5rem;
  }
  
  .resource-table {
    margin-bottom: 2rem;
  }
  
  .resource-table table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1rem;
  }
  
  .resource-table th {
    background-color: #e8f4f8;
    padding: 0.8rem;
    text-align: left;
    border-bottom: 2px solid #d0d0d0;
    font-weight: 600;
    color: #2c3e50;
  }
  
  .resource-table td {
    padding: 0.8rem;
    border-bottom: 1px solid #e8e8e8;
  }
  
  .resource-table tr:last-child td {
    border-bottom: 2px solid #d0d0d0;
  }
  
  .resource-table tr:hover {
    background-color: #f9f9f9;
  }
  
  .resource-table a {
    color: #0066cc;
    text-decoration: none;
  }
  
  .resource-table a:hover {
    text-decoration: underline;
  }
</style>

<div class="resources-container">

<div class="resource-section-title">Generative AI and General ML</div>

<div class="resource-table">
<table>
<thead>
<tr>
<th>Title</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

<div class="resource-section-title">Biological Foundation Model</div>

<div class="resource-table">
<table>
<thead>
<tr>
<th>Title</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/OmicsML/awesome-foundation-model-single-cell-papers">awesome-foundation-model-single-cell-papers</a></td>
<td>Collection of papers for state-of-the-art single-cell foundation model development</td>
</tr>
</tbody>
</table>
</div>

<div class="resource-section-title">AI Drug Discovery</div>

<div class="resource-table">
<table>
<thead>
<tr>
<th>Title</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

</div>

<h1 class="page-title">Blog</h1>

<style>
  .blog-posts {
    width: 80%;
    margin: 0 auto;
  }
  
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
