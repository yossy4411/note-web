---
title: <% tp.date.now("YYYY年MM月DD日(ddd)") %>
description: <% tp.date.now("YYYY年M月D日") %>の日記
tags: 
date: <% tp.date.now("YYYY-MM-DD") %>
---
<%
tp.file.rename(tp.date.now()) 
%>

## 今日の体調

| 体調  | 元気    |
| --- | ----- |
| 就寝  | 22:00 |
| 起床  | 6:30  |
| 朝食  | 6:50  |
| 天気痛 | false |
