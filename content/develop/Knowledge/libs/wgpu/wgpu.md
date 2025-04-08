---
title: Wgpu
description: 
lead: 
tags:
  - GPU
  - グラフィック
aliases:
  - wgpu
date: 2025-04-08T14:49:09+09:00
lastmod: 2025-04-08T14:49:09+09:00
draft: true
showContent: false
slug: about
---
## 概要
[`wgpu`](https://github.com/gfx-rs/wgpu)は[WebGPU](../../platform/graphics/webgpu/WebGPU.md)のAPIを[Rust](../../lang/Rust/Rust.md)で実装した[クレート](../../lang/Rust/crate.md)。  
↪ https://wgpu.rs/

Windows, MacOS, Linux, Web (WASM) の複数プラットフォームで動作する。

他の言語とは違い、Rustのメモリ安全性を活かし、GPUのリソースを安全に管理したり、楽に並行処理が可能である。
### WGSLシェーダー