---
title: 型安全性
description: Rustの型安全性について
lead: 
tags: 
aliases: 
date: 2025-04-09T21:35:49+09:00
lastmod: 2025-04-09T21:35:49+09:00
draft: true
showContent: false
slug: type-safe
---
この記事は執筆途中です。
## 静的型付け
まず、[Rust](Rust.md)は強い静的型付け言語である。

強い静的型付けというのは、すべてのオブジェクトに対してコンパイル時に型が割り振られるということである。この型付けは[rustc](rustc.md)が行う。

```rust
struct MyObject;
impl MyObject {
	fn new() -> Self {
		Self{}
	}
}

fn main() {
	let a = MyObject::new();
}
```

このとき`a`の型は、`MyObject`と決定する。  
これは関数`new`が`Self`(`MyObject`)を返すと明示的に指定されているからだ。

これがImplicit Typing（暗示的な型付け）。
## 動的型付け
Rustは静的型付け言語でありながらも、動的型付けもサポートしている。

動的型付けが使われている最も身近な例としては、`Box<dyn Error>`がある。

```rust
fn main() -> Result<(), Box<dyn Error>> {
	println!("Hello World");
	Ok()
}
```

`dyn`キーワードは動的な型付けを意味している。  
`Error`がトレイトだからだ。

こうすることで、トレイト`Error`を実装するすべてのstructをResultに使用することができるようになる。
