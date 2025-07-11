---
title: 所有権システム
description: 値を保持する場所
lead: Rustには"所有権システム"というのがあります。これには、ゼロコストのメモリ管理ができるという利点があります。
tags: 
aliases:
  - 所有権
draft: false
created: 2025-04-04T07:25:59+09:00
modified: 2025-07-11T09:08:48+09:00
---
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

