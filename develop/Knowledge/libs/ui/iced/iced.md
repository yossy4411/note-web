---
title: Iced
description: " RustのGUIライブラリ"
lead: icedはRustで書かれたGUIライブラリの1つであり、宣言的なUIの定義が特徴である。
tags: 
aliases:
  - iced
date: 2025-04-09T15:50:19+09:00
lastmod: 2025-05-14
draft: false
showContent: true
slug: about
---
**iced** ([crates.io](https://crates.io/crates/iced), [GitHub](https://github.com/iced-rs/iced))は[Rust](../../../lang/Rust/Rust.md)で書かれた[GUIライブラリ](../GUIライブラリ.md)の1つであり、宣言的なUIの定義が特徴である。
## 特徴
> A cross-platform GUI library for Rust focused on simplicity and type-safety. Inspired by [Elm](https://elm-lang.org/).

日本語にすると、

> 単純性と型安全性に注視した[Rust](../../../lang/Rust/Rust.md)のクラスプラットフォームGUIライブラリ。Elmにインスパイアされました。

となりますね。

## クロスプラットフォーム
デスクトップ（Windows、macOS、Linux）とWeb（WebAssembly）で、同じコードで動作します。

また、Rustはクロスコンパイルが可能なので、その点はかなり便利じゃないかな―って思います。

### 宣言的UI
UIを宣言する形で書く。  
つまり、UIを「どう見えるべきか」を宣言的に、単純に書くことができる。

例えば、ボタンやテキストなどをコードで直感的に記述できるよ。

### 非同期対応
アプリケーション全体が非同期タスク（`async`）に対応しているので、APIリクエストや長時間かかる処理も簡単に扱える。

よかったね、Rustが非同期対応してて。
### プラグイン可能な柔軟性
カスタムウィジェットやスタイルを実装できるので、自由度が高い。

ちなみにこれの実装にはちょっとクセが合ったりします。
## バックエンド
icedはバックエンドに[wgpu](../../wgpu/wgpu.md)を採用している。  
また、パフォーマンスこそまずまずだが、tiny-skiaにも対応している。  
↪[icedのバックエンドの特性](icedのバックエンドの特性.md)

## サンプルコード

`iced`は、関数型言語Elmのアーキテクチャにインスパイアされて設計されています。

アプリの状態（State）を明確に管理しやすく、UIイベントもスッキリと書くことができます。

**構成要素**:
- **Model**: アプリケーションの状態
- **Message**: ユーザーやシステムからのイベント
- **Update**: 状態を更新するロジック
- **View**: 状態に基づいてUIを描画

```rust
#[derive(Default)]
struct Counter {
    value: i32,
}

#[derive(Debug, Clone, Copy)]
pub enum Message {
    Increment,
    Decrement,
}


use iced::widget::{button, column, text, Column};

impl Counter {
    pub fn view(&self) -> Column<Message> {
        column![
            button("+").on_press(Message::Increment),
            
            text(self.value).size(50),
            
            button("-").on_press(Message::Decrement),
        ]
    }
	
	pub fn update(&mut self, message: Message) {
        match message {
            Message::Increment => {
                self.value += 1;
            }
            Message::Decrement => {
                self.value -= 1;
            }
        }
    }
}

fn main() -> iced::Result {
    iced::run("A cool counter", Counter::update, Counter::view)
}
```

関数`view`部分にはマクロと純粋関数を使用しています。ここに関数型言語としての特徴が出てきていますね。

ボタンを押したときのイベントを`on_press`で割り当て、イベント発生時に`update`関数が呼び出されます。  
`self.value`を変更すると、`view`関数が呼び出されます。

そうやってローテーションしていきます。
