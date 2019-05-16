---
layout: default
title: Bookmarks
permalink: /bookmarks/
---

{% for bookmark in site.data.bookmarks %}
1. *{{ bookmark.title }}*. Tags: [{{bookmark.tags}}]. <{{ bookmark.uri }}>.
{% endfor %}
