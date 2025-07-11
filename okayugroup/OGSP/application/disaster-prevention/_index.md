---
title: OGSP防災アプリ
description: 
draft: false
aliases:
  - OGSP Disaster Prevention
created: 2025-04-09T02:40:31+09:00
modified: 2025-07-11T11:13:35+09:00
---
**OGSP Disaster Prevention**、または**OGSP防災**は、[[okayugroup/OGSP/_index|OGSP]]や気象庁から提供される防災情報を表示するためのデスクトップ (およびモバイル) アプリケーションである。  
また、このアプリケーションは[[okayugroup/OGSP/network/_index|OGSP Disaster Network]]のアプリケーション層を担う役割があり、地震計から取得したデータをレンダリングする機能を備える。
## 特徴
OGSP Disaster Preventionの最大の特徴は、[[develop/Knowledge/lang/programming/Rust/_index|Rust]]のメモリ安全性と並列性を活用した、軽量で高速な動作だ。

OGSP Disaster Preventionは、C#で構成される[[okayugroup/OGSP/previous/EarthQuake/_index|EarthQuake.Desktop]]の次期プロジェクトである。前任では、機能を盛りすぎたために、フレームレート的にもバイナリサイズ的にも重くなってしまった。  
ランタイムの重さはほとんどが[[GC|GC]]に由来するもので、開発者である[[about-me|yossy4411]]は[[develop/Knowledge/lang/programming/Rust/_index|Rust]]がこれを解消するカギだと考えた。

実際、GCを搭載しないRustは、C#よりも高速で、省リソースで動作することが多い。
## 開発
### 環境
- IDE: RustRover
- プラットフォーム: GitHub
### 依存関係
- [[develop/Knowledge/libs/wgpu/_index|wgpu]]
- Vello
- Xilem
