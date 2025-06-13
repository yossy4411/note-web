---
title: wgpu
description: 
lead: 
tags:
  - GPU
  - グラフィック
aliases:
  - wgpu
date: 2025-04-08T14:49:09+09:00
lastmod: 2025-05-16
draft: false
showContent: false
slug: about
---
**wgpu**は[[WebGPU]]のAPIを[[Rust]]で実装した[[crate|クレート]]である。

> [!IMPORTANT]
> ラッパーではなく、WebGPUの設計に則ってRustで実装された、ピュアRustのライブラリである。

wgpuは、Windows, MacOS, Linux, Web (WASM) の複数プラットフォームで動作する。

Rustのメモリ安全性を活かし、GPUのリソースを安全に管理したり、楽に並行処理が可能である。また、直接的に非同期処理をサポートしている。
### WGSLシェーダー
WebGPUのシェーダーはWGSL (拡張子`.wgsl`)で定義する。この構文はRustに非常に似ている。

```wgsl
// 頂点シェーダ
@vertex
fn vs_main(@builtin(vertex_index) vertex_index: u32) -> @builtin(position) vec4<f32> {
    let positions = array<vec2<f32>, 3>(
        vec2<f32>(0.0, 0.5),     // 上
        vec2<f32>(-0.5, -0.5),   // 左下
        vec2<f32>(0.5, -0.5)     // 右下
    );

    let pos = positions[vertex_index];
    return vec4<f32>(pos, 0.0, 1.0);
}

// フラグメントシェーダ
@fragment
fn fs_main() -> @location(0) vec4<f32> {
    return vec4<f32>(1.0, 0.0, 0.0, 1.0); #FF0000FF
}
```

詳しくは別のドキュメントで説明する...

## リンク
- [GitHub](https://github.com/gfx-rs/wgpu)
- [公式サイト](https://wgpu.rs/)
