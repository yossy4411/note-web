---
title: <% tp.date.now("YYYY年MM月DD日(ddd)") %>
description: <% tp.date.now("YYYY年M月D日") %>の日記
tags:
---
<%
tp.file.rename(tp.date.now()) 
%>