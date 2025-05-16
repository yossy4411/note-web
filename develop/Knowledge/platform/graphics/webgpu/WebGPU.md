---
title: WebGPUについて
description: 
lead: 
tags:
  - グラフィック
  - GPU
  - Web
aliases:
  - webgpu
date: 2025-04-08T14:35:29+09:00
lastmod: 2025-05-16
draft: false
showContent: true
slug: about
---
## 概要
**WebGPU**は、グラフィカル処理とGPGPUのための将来的な標準とAPIのためのワーキングネームである。「モダンな3D画像処理と計算機能」を提供することを目的としている。  
Apple, Google, Microsoft, Mozillaを含むさまざまな組織のエンジニアが協力して、[W3C](https://ja.wikipedia.org/wiki/World_Wide_Web_Consortium "World Wide Web Consortium")の*GPU for the Web*コミュニティグループで開発される。

VulkanやMetal、Direct3Dをラップするような形で、クロスプラットフォームに動作するAPIの提供を行う。

## 実装・設計
設計の中心となるヘッダーファイルは[webgpu.h](https://raw.githubusercontent.com/webgpu-native/webgpu-headers/main/webgpu.h)で提供されている。これには関数や構造体などの「設計書」のみが定義されており、中身は別のライブラリに存在する。
### Rust
WebGPUの設計書に基づいて純粋な[Rust](../../../lang/programming/Rust/Rust.md)でそれを実装したものが[wgpu](../../../libs/wgpu/wgpu.md)だ。主にMozilla FirefoxやRustの[GUIライブラリ](../../../libs/ui/GUIライブラリ.md)で使用されている。
## C++
WebGPUをC++で実装したものが、[WebGPU-C++](https://github.com/eliemichel/WebGPU-Cpp)や[Dawn](https://github.com/google/dawn)である。特にDawnはGoogleによって開発されており、Google Chromeに搭載されている。
## ブラウザの対応
### Google Chrome
Google Chromeでは、バージョン113以上で正式にサポートされている。  
同じくMicrosoft Edgeもバージョン113以上で対応している。
### Safari
SafariはMetalを通してWebGPUをサポートするが、現時点ではプレビュー版でサポートされている。

また、フラグで`WebGPU = true`を設定することでプレビュー版でなくても使用できる。
## Firefox
Mozilla Firefoxは、残念ながらデフォルトではサポートされない。代わりに`dom.webgpu.enabled`フラグを有効化することでサポートされる。

W3CにMozillaが参加しているので、じきに正式サポートされるはずだ。