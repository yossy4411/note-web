# 知識の倉庫
俺の思ったこと全部置いてる場所

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
---

## 内容
...
```