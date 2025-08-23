---
created: 2025-04-01T07:36:41+09:00
modified: 2025-08-23T05:28:47+09:00
---
# 知識の倉庫
俺の思ったこと、日記などを置く場所

> [!NOTE]
> 情報の宝箱やー

> [!CAUTION]
> 流石にプライバシーとか次の動画のネタとかは載せてません。
> あくまで役立つ情報のまとめとか、頭の中の整理のために使っています。

## Hugo統合
基本的に、Hugo（静的サイトビルダー）として利用できるような形にしたいと思っています。
したがって、Markdownファイルそれぞれには次のようなテンプレートが貼られています。

```markdown
---
title: タイトル
description: 説明
lead: 記事の冒頭 (meta description)
tags: タグ1, タグ2
aliases: エイリアス（リダイレクション）
date: YYYY-MM-DD HH:mm:ss 作成日時
lastmod: YYYY-MM-DD HH:mm:ss 更新日時
draft: true/false ドラフトかどうか
showContent: true/false _index.mdで内容まで表示するか
---

## 内容
...
```

## Home
[[_index|Home]]