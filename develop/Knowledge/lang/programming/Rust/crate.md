---
title: クレート
description: 
lead: 
tags: 
aliases:
  - クレート
date: 2025-04-08T15:29:13+09:00
lastmod: 2025-04-08T15:29:13+09:00
draft: true
showContent: false
slug:
---
## クレートとは
クレート (Crate)は、[Rust](Rust.md)のコードをまとめる基本単位の1つ。Rustのプロジェクトやライブラリのことを指す。

コンパイル先の違いによって[バイナリクレート](#バイナリクレート)と[ライブラリクレート](#ライブラリクレート)に分けられる。
## バイナリクレート
CLIアプリケーションやGUIアプリケーションなどを含む、実行可能なプログラムを提供するクレートは一般的に『バイナリクレート』と呼ばれる。

コンパイル時にバイナリとしてビルドされ、バイナリファイルを実行したときに関数`main`が呼び出されるようになっている。

デフォルトでは`src/main.rs`がバイナリクレートの定義になる。  
また、`src/bin/*.rs`がすべてバイナリとして認識される。

```rust: main.rs
fn main() {
	println!("Hello, World!");
}
```

実行すると、CLIで`Hello, World!`が出力される。

また、都度`Cargo.toml`を編集して別のバイナリクレートを同じプロジェクト内に作ることもできる。

```toml Cargo.toml
[package]  
name = "mypackage"
version = "0.1.0"
edition = "2024"

[[bin]]  
name = "run-all"
path = "src/run.rs"
```

### ライブラリクレート
[ライブラリ](../../../libs/ライブラリ.md)を提供するクレートは、『ライブラリクレート』と呼ばれる。

一般的にいくつもの構造体やトレイト、関数などを定義する。

デフォルトで`src/lib.rs`がライブラリクレートの中心となる。ここでモジュールなどを定義する。

```rust lib.rs
pub mod client;
pub mod server;

pub struct MyStruct {
	&str name,
}

impl MyStruct {
	pub fn name(&self) -> &str {
		self.name
	}
}
```

モジュールごとに`mod.rs`を定義して、その中に更にモジュールを定義したりすることもできる。