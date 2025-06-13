---
title: egui
description: RustのGUIライブラリ
lead: 
tags:
  - グラフィック
aliases:
  - egui
date: 2025-04-10T17:35:48+09:00
lastmod: 2025-04-10T17:35:48+09:00
draft: false
showContent: true
slug: about
---
## 特徴
> egui: an easy-to-use immediate mode GUI in Rust that runs on both web and native

日本語にすると、

> Webとネイティブアプリケーションとして動作できる、[[Rust]]の使いやすい即時モードの[[GUIライブラリ]]。

となりますね。

### 即時モードについて
即時モードとは、アプリケーションが常に更新され続ける形のUI構築システムのことで、ウィンドウでは定期的に再描画処理が呼ばれる。

## サンプルコード
```rust
ui.heading("My egui Application");
ui.horizontal(|ui| {
    ui.label("Your name: ");
    ui.text_edit_singleline(&mut name);
});
ui.add(egui::Slider::new(&mut age, 0..=120).text("age"));
if ui.button("Increment").clicked() {
    age += 1;
}
ui.label(format!("Hello '{name}', age {age}"));
ui.image(egui::include_image!("ferris.png"));
```

やっぱりわかりやすいね。

他のGUIライブラリとは違って、ボタンのクリックの処理がイベントハンドラではないところが少し気になると思うが、`clicked()`はボタンが押された瞬間だけ`true`になるため、これでボタンの押された処理が実装できる。

私は以前Scratchをやっていましたが、それにとても近いと思います。

