---
title: OGSP防災アプリ
description: 
draft: false
aliases:
  - OGSP Disaster Prevention
created: 2025-04-09T02:40:31+09:00
modified: 2025-07-11T08:30:33+09:00
---
**OGSP Disaster Prevention**、または**OGSP防災**は、[[OGSP]]や気象庁から提供される防災情報を表示するためのデスクトップ (およびモバイル) アプリケーションである。  
また、このアプリケーションは[[OGSP Disaster Network]]のアプリケーション層を担う役割があり、地震計から取得したデータをレンダリングする機能を備える。
## 特徴
OGSP Disaster Preventionの最大の特徴は、[[Rust]]のメモリ安全性と並列性を活用した、軽量で高速な動作だ。

OGSP Disaster Preventionは、C#で構成される[[EarthQuake.desktop|EarthQuake]]の次期プロジェクトである。前任では、機能を盛りすぎたために、フレームレート的にもバイナリサイズ的にも重くなってしまった。  
ランタイムの重さはほとんどが[[ガベージコレクション|GC]]に由来するもので、開発者である[[about-me|yossy4411]]は[[Rust]]がこれを解消するカギだと考えた。

実際、GCを搭載しないRustは、C#よりも高速で、省リソースで動作することが多い。
## 開発
### 環境
- IDE: RustRover
- プラットフォーム: GitHub
### 依存関係
- [[wgpu]]
- Vello
- Xilem
