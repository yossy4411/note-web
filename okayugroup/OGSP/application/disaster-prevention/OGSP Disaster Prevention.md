---
title: OGSP Disaster Prevention
description: OGSPのクライアントアプリ
lead: 
tags: 
aliases:
  - OGSP防災
date: 2025-04-07T22:37:43+09:00
lastmod: 2025-05-16
draft: false
showContent: true
slug: about
---
**OGSP Disaster Prevention**、または**OGSP防災**は、[OGSP](../../OGSP.md)や気象庁から提供される防災情報を表示するためのデスクトップ (およびモバイル) アプリケーションである。  
また、このアプリケーションは[OGSP Disaster Network](../../network/OGSP%20Disaster%20Network.md)のアプリケーション層を担う役割があり、地震計から取得したデータをレンダリングする機能を備える。
## 特徴
OGSP Disaster Preventionの最大の特徴は、[Rust](../../../../develop/Knowledge/lang/programming/Rust/Rust.md)のメモリ安全性と並列性を活用した、軽量で高速な動作だ。

OGSP Disaster Preventionは、C#で構成される[EarthQuake](../../previous/EarthQuake/EarthQuake.desktop.md)の次期プロジェクトである。前任では、機能を盛りすぎたために、フレームレート的にもバイナリサイズ的にも重くなってしまった。  
ランタイムの重さはほとんどが[GC](../../../../develop/Knowledge/lang/programming/ガベージコレクション.md)に由来するもので、開発者である[yossy4411](../../../../私について.md)は[Rust](../../../../develop/Knowledge/lang/programming/Rust/Rust.md)がこれを解消するカギだと考えた。

実際、GCを搭載しないRustは、C#よりも高速で、省リソースで動作することが多い。
## 開発
### 環境
- IDE: RustRover
- プラットフォーム: GitHub
### 依存関係
- [wgpu](../../../../develop/Knowledge/libs/wgpu/wgpu.md)
- Vello
- Xilem
