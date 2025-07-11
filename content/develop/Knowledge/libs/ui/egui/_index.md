---
title: egui UIライブラリ
description: 
draft: false
created: 2025-04-10T08:34:51+09:00
modified: 2025-07-11T10:51:30+09:00
aliases:
  - egui
---
## 特徴
> egui: an easy-to-use immediate mode GUI in Rust that runs on both web and native

日本語にすると、

> Webとネイティブアプリケーションとして動作できる、[[develop/Knowledge/lang/programming/Rust/_index|Rust]]の使いやすい即時モードの[[GUIライブラリ]]。

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

