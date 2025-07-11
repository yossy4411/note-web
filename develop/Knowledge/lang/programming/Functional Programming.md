---
title: 関数型プログラミング
description: 
lead: 
tags: 
aliases:
  - 関数型プログラミング
draft: false
showContent: true
created: 2025-05-16T05:46:01+09:00
modified: 2025-07-11T09:05:59+09:00
---
**関数型プログラミング** (英: Functional programming)とは、数学的な意味での『関数』を主に使用する[[Programming Paradime]]である。

関数型プログラミングを推奨している言語を、**関数型プログラミング言語** (functional programming language) というが、略して**関数型言語** (functional language)と呼ぶこともある。

## 概要
関数型プログラミングでは、関数を軸にプログラミングを行う。  
ここでの関数とは、数学的な関数、すなわち[[Pure Function#参照透過性|参照透過性]]をもつもの（[[Pure Function]]）を指す。

**参照透過性**とは、数学的な関数と同じように、引数が同じであれば同じ値を返す性質である。  
例としてこのPythonコードを見ていただく。

```python
def expression(x):
    return x ** 2 # xの2乗
```

ここでは、$x=3$のときには$9$、$x=4$のときは$16$のように、引数が同じときは常に同じ値を返す。数学で言うところの$f(x)=x^2$と同じだ。

関数プログラミングでは、関数を使って組み立てた式が軸となっている。プログラミング言語ではよく「関数を実行する」や「関数を呼び出す」と表現するが、関数型プログラミング言語では「式を評価する」という表現もよく使われる。

## 言語
主要な言語は以下の通り。
### 特化
- Elm
- Scala
- Haskell
- LISP
### マルチパラダイム
- Python
- JavaScript
- Ruby
- Kotlin
- [[Rust]]
