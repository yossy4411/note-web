---
title: icedのバックエンドの特性
description: icedの描画ライブラリの使い方にクセがある
lead: 
tags:
  - グラフィック
aliases: 
lastmod: 2025-04-01 21:20:37
date: 2025-05-14
draft: true
slug: iced-backend
---
## `tiny-skia`を使うとどうなるか
`tiny-skia`はSkiaを基にした軽量な[[../../../lang/Rust/_index|Rust]]のライブラリです。

まずこいつ、遅いです。

後述のwgpuよりも数十倍ほど。
```toml: Cargo.toml
iced_tiny_skia = { version = "0.13.0", features = ["image"] }  
iced = { version = "0.13.0", default-features = false, features = ["tiny-skia"] }
```

使い方は結構簡単。
Skiaの直感的な記述を活かせててGood。
```rust
let pixmap = Pixmap::new(width, height);

let path_builder = PathBuilder::new();
path_builder.move_to(0, 0);
path_builder.line_to(10, 0);

pixmap.stroke_path(path_builder.build());

renderer.draw_pixmap(pixmap);
// renderer: iced_tiny_skia::Renderer
```

## wgpu最強
やっぱりパフォーマンス的には[wgpu](../../wgpu/wgpu.md)が最強だと思います...w

icedはデフォルトでwgpuを使用しています。 
wgpuを使おうとするとシェーダーの定義などでコード全体が悲しいことになります。抽象化されたメソッドは存在します。書きませんけど。気になったらDMとかください。

## 結論
ちなみに、tiny-skiaはno-std環境でも動作するので、例えば組み込み開発などで重宝します。

普通に使う分にはwgpuが無難だと思います。