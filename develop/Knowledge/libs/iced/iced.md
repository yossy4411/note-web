---
title: Iced - RustのGUIライブラリ
description: 
lead: 
tags: 
aliases:
  - iced
date: 2025-04-09T15:50:19+09:00
lastmod: 2025-04-09T15:50:19+09:00
draft: false
showContent: true
slug: about
---

## 特徴
> A cross-platform GUI library for Rust focused on simplicity and type-safety. Inspired by [Elm](https://elm-lang.org/).

日本語にすると、

> 単純性と型安全性に注視した[Rust](../../lang/Rust/Rust.md)のクラスプラットフォームGUIライブラリ。Elmにインスパイアされました。

となりますね。

1. **Elmアーキテクチャを採用**:
    
    - `iced`は、関数型言語Elmのアーキテクチャにインスパイアされて設計されている。
    - アプリの状態（State）を明確に管理しやすく、UIイベントもスッキリと書ける。
    - **構成要素**:
        - **Model**: アプリケーションの状態
        - **Message**: ユーザーやシステムからのイベント
        - **Update**: 状態を更新するロジック
        - **View**: 状態に基づいてUIを描画
2. **クロスプラットフォーム対応**:
    
    - デスクトップ（Windows、macOS、Linux）とWeb（WebAssembly）で動く。
    - しかも同じコードでね。
3. **宣言的UI**:
    
    - UIを「どう見えるべきか」を宣言的に書くことができる。
    - 例えば、ボタンやテキストなどをコードで直感的に記述できるよ。
4. **非同期対応**:
    
    - 非同期タスク（`async`）に対応しているから、APIリクエストや長時間かかる処理も簡単に扱える。
5. **プラグイン可能な柔軟性**:
    
    - カスタムウィジェットやスタイルを実装できるので、自由度が高い。

## バックエンド
icedはバックエンドに[wgpu](../wgpu/wgpu.md)を採用している。  
また、パフォーマンスこそまずまずだが、tiny-skiaにも対応している。  
↪[icedのバックエンドの特性](../../../../okayugroup/OGSP/previous/icedのバックエンドの特性.md)

## サンプルコード

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
        // We use a column: a simple vertical layout
        column![
            // The increment button. We tell it to produce an
            // `Increment` message when pressed
            button("+").on_press(Message::Increment),

            // We show the value of the counter here
            text(self.value).size(50),

            // The decrement button. We tell it to produce a
            // `Decrement` message when pressed
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

関数`view`部分にはマクロと純粋関数を使用している。ここに関数型言語Elmの特徴が出てきていますね。

ボタンを押したときのイベントを`on_press`で割り当て、イベント発生時に`update`関数が呼び出されます。  
`self.value`を変更すると、`view`関数が呼び出されます。

そうやってローテーションしていきます。
