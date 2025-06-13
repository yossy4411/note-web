---
title: URI
description: 
lead: 
tags: 
aliases: 
date: 2025-04-20T16:50:35+09:00
lastmod: 2025-04-20T16:50:35+09:00
draft: false
showContent: false
slug: uri
---
**Uniform Resource Identifier** （ユニフォーム リソース アイデンティファイア、統一資源識別子）、**URI**とは、抽象的または物理的なリソースを識別するためのコンパクトな文字列のことである。また、一定の書式によってリソースを指し示す識別子（Identifier）である。

## 形式
`https://example.com`  
これはURIの中では特に[[URL]]であるが、これは以下のような要素で構成されている。

```code
scheme://[userinfo@]host[:port]/path[?query][#fragment]
```

URIのスキームは、一般的には[[HTTP]] (`http://`, `https://`) が使用されるが、他にもFTP (`ftp://`)やメール (`mailto:`)、ローカルファイル (`file://`)などがある。