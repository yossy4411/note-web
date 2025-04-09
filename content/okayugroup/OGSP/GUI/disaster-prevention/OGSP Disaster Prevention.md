---
title: OGSP Disaster Prevention
description: OGSPのクライアントアプリ
lead: 
tags: 
aliases: 
date: 2025-04-07T22:37:43+09:00
lastmod: 2025-04-09
draft: true
showContent: false
slug: about
moc: true
---
## 特徴
このプロジェクトの最大の特徴は、[Rust](../../../../develop/Knowledge/lang/Rust/Rust.md)のメモリ安全性[^1]と高速性を活用した軽量な動作だと思います。  
前プロジェクトの[EarthQuake](EarthQuake/EarthQuake.desktop.md)(C#)では、機能を追加していくにつれて動作がどんどん重くなっていき、開発を諦めてしまいました。この動作の重さは[GC](../../../../develop/Knowledge/lang/ガベージコレクション.md)から来ていると考えられます。  
GCのないRustはC#よりも高速かつ少ないリソースでも動くと考えられます。
## 開発
現在の開発段階は「検討中」です。[^2]基礎からまるっきり変わる可能性もあります。
- IDE: RustRover
- プラットフォーム: GitHub
## 技術的情報
**依存関係**
- [wgpu](../../../../develop/Knowledge/libs/wgpu/wgpu.md)
- [iced](../../../../develop/Knowledge/libs/iced/iced.md)

[^1]: [所有権](../../../../develop/Knowledge/lang/Rust/所有権.md)システムによって保証されている。
[^2]: 詳しくは[やることリスト（すべて）](../../../../TODO/やることリスト（すべて）.md)をご覧ください。
