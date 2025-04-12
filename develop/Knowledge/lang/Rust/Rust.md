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
## Rustの開発状況について
- [ソースコード (GitHub)](https://github.com/rust-lang/rust)
Rustはあの"Firefox"を手掛けるMozilla社が開発したプログラミング言語で、高速でメモリの安全性が特徴です。
これには独自の[所有権](所有権.md)というシステムが大きく関わっており、これによって[GC](../ガベージコレクション.md)なしでメモリの安全性を手に入れています。

所有権を正しく判別し、コンパイル時にエラーを出すために強力な[rustc](rustc.md) (rustc)が作られています。
## 用語集
- [所有権](所有権.md)
- [rustc](rustc.md) - Rust compiler
- [デリファレンス](デリファレンス.md)