---
title: Keep-Alive接続について
description: 
lead: 
tags: 
aliases: 
date: 2025-05-09T18:26:35+09:00
lastmod: 2025-05-09T18:26:35+09:00
draft: false
showContent: false
slug: keep-alive
---
**Keep-Alive**、または**Keep-Alive接続**とは、[[HTTP]]において、[[TCP]]接続を切断させずに持続的に接続を行うことである。

HTTPの仕組みとして、データを転送するときには、ハンドシェイクを行って接続を確立し、そのあとにリクエスト本体を送信する。Keep-Aliveは、その確立された接続を、接続したままにする仕組みである。

Keep-Aliveを使用しない場合、リクエストを送信する度にハンドシェイクなどの処理を行う必要があり、時間がかかる。Keep-Aliveの登場は、主に無駄な時間を減らすことが目的である。