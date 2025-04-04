---
title: Rust
description: Rust the programming language
draft: false
---
## 概要
- [ソースコード (GitHub)](https://github.com/rust-lang/rust)
### コンパイラ
`rustc`, `cargo`
- AOTコンパイル
- クロスコンパイルが可能 (Windows, Mac, Linux, iOS, Android, WASM)
- 実行時に発生する可能性のあるエラーをチェックしてくれます

実行時のエラーを最大限まで減らすため、コンパイルには比較的時間がかかります。
### 所有権
Rustには"所有権システム"というのがあります。
これには、ゼロコストのメモリ管理ができるという利点があります。

これによりGCが不必要となり、速度が圧倒的に上がります。

関数やマクロなどで値を使用したとき、その値の所有権は関数へ移動します。

```rust
fn main() {
	let a: String = "text".to_string();
	
	custom_function(a);  // aの所有権はcustom_functionに渡る
	// ここより下ではもうaは使用できない
	
	println!("移動後の値の使用: {}", a);  // コンパイルエラー
}

// 
fn custom_function(text: String) {
	println!("関数内での値: {}", text);
	// ここより下ではもうtextは使用できない
}
```

> また、main関数内の変数`a`は`fn main`→`custom_function`→`println!`のように移動しています。
> println!関数に渡ったあと、その関数内でスコープを抜けるときに変数はメモリ上から破棄されます。
> 
> > つまり、custom_function関数でaを使ったあとにはもう値は存在しないこととなります。

