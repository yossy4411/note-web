---
title: Rustの概要
description: 
lead: Rustはあの"Firefox"を手掛けるMozilla社が開発したプログラミング言語で、高速でメモリの安全性が特徴です。
tags:
  - MOC
aliases:
  - rust
date: 2025-04-04T16:46:51+09:00
lastmod: 2025-04-04T16:46:51+09:00
draft: false
showContent: true
slug: about
---
**Rust**は、性能やメモリ安全性を目指して作られた、マルチパラダイムのシステムプログラミング言語である。C系の言語を置き換えることを目標としているが、ポインターなどの概念が存在せず安全に開発を行うことができる。

読み方は**ラスト**。 
## 概要
Rustには**ポインターが存在しない**。その代わり、借用といって、参照を取るシステムによって値を共有することができる。また、値の本体を、変数やメンバーへの代入、関数での引数としての使用を行うときは、その値は移動する。これを譲渡という。  
このシステムによって、[[ガベージコレクション]]を必要としない安全なメモリ管理ができるのである。

Rustでは、ほとんどのエラーを[[rustc|コンパイラ]]がキャッチできるように設計されている。そのため、ランタイムエラーは従来の言語よりも少ない。Javaで最も多いとされるNullPointerExceptionのような、Rustでいう参照によって発生するエラーはコンパイルエラーとして扱われる。

Rustは、並列・並行処理、非同期処理を標準でサポートする。参照システムは安全に並行処理を行うことができるように設計されている。

## コード
HelloWorldは以下の通り。
```rust
fn main() {
	println!("Hello, World!");
}
```

そう、とても単純なのである。これはRustの単純な構文と、マクロのおかげである。
## 用語集
- [[crate]]
- [[所有権]]
- [[rustc]] - Rust compiler
- [[デリファレンス]]
