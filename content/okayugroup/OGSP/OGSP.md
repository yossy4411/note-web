---
title: おかゆグループ地震計プロジェクト
description: 
lead: 
tags:
  - MOC
aliases:
  - OGSP
date: 2025-04-07T22:38:56+09:00
lastmod: 2025-04-07T22:38:56+09:00
draft: false
showContent: true
slug: about
---
## 概要
おかゆグループ地震計プロジェクト（英: Okayu Group Seismometer Project、略: OGSP）は、オープンソースで地震観測網および災害対策網を構築するプロジェクト。

主導は[おかゆグループ](../おかゆグループ.md)であるが、基本的にWeb3の考えを取り入れており、分散化を目標としている。すべてのプログラムがGitHub上に公開される、オープンソースプロジェクトである[^1]。
## 地震計開発
地震計は、加速度データから震度を計算し、データを[サーバー](#サーバー開発)に送信する。

現在ではESP32マイコンを使い、開発を進めています。

言語: [Rust](../../develop/Knowledge/lang/programming/Rust/Rust.md)
↪ [OGSP Seismometer](sensor/seismometer/OGSP%20Seismometer.md)


また、スマホに内蔵される加速度センサを使って、スマホを地震計にすることで新しく地震計を作製することなく地震観測が可能になるプロジェクト。
## サーバー開発
地震計から収集したデータを集める場所。

同時に受信デバイスへのデータ配信と気象庁などの機関からのデータ収集も行う。

↪ [OGSP Server Node](server/OGSP%20Server%20Node.md)

## 受信システム・アプリ開発
### [EarthQuake](previous/EarthQuake/EarthQuake.desktop.md) - デスクトップ版地震災害情報アプリ
パフォーマンスの理由で開発停止  
言語: C#  
GUIフレームワーク: Avalonia + SkiaSharp
↪ [GitHub](https://github.com/yossy4411/EarthQuake)
### [OGSP Disaster Prevention](application/disaster-prevention/OGSP%20Disaster%20Prevention.md)
パフォーマンスを最大化した最新鋭の設計  
言語: [Rust](../../develop/Knowledge/lang/programming/Rust/Rust.md)
 GUIフレームワーク: `vello` + `xilem`

[^1]: 詳しくは[なぜオープンソースなのか](なぜオープンソースなのか.md)を参照。
