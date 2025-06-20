---
title: QUIC
description: 
lead: 
tags: 
aliases: 
date: 2025-04-28T21:39:46+09:00
lastmod: 2025-04-28T21:39:46+09:00
draft: false
showContent: true
slug: about
---
**QUIC** (クイック) は、次世代型の[[トランスポート層]]の通信プロトコルである。

## 概要
QUICは、[[UDP]]を基礎にGoogleのJIM Roskindによって設計された、TLSを用いたセキュリティやUDPに由来する高速性などの面で優れている通信プロトコルである。

QUICは、エンドポイント間の多重化接続の集合体に対応しており、レイテンシ削減や接続の一時的な切断にも柔軟に対応できる。これらの理由から、[[HTTP3|HTTP/3]]にも採用されている。

## 特徴
### セキュリティが高い
QUICの接続は、すべてTLS1.3で暗号化されており、この規則を破ることはどんな場合においても**不可能**である。また、接続時にはTLSハンドシェイクを行い、高効率で信頼性の高い通信ができるよう設計されている。

### UDPベース
TCPのようなコネクション型であるが、[[UDP]]がベースとなっている。

UDPの上に再送処理や順序制御などで、信頼性を築き上げている。

### コネクションの再利用と再開が可能
モバイル回線やWi-Fiの切り替えなどでIPアドレスが変わっても、QUICはコネクションを保持できる。これは、コネクションをIPアドレスで判別するのではなくコネクションIDを割り当てて判別しているからである。

### ストリームの多重化
QUICでは、一つの接続に対して複数のストリームを持つことができる。これによりHTTP/2のヘッドオブラインブロッキング問題（HoL）を解決できる。

### 利用状況
Google, YouTube, Gmail, Facebook, Cloudflare, LINEなどの多数のサービスで、HTTP/3を含めたQUICプロトコルが採用されている。

2020年には、IETF (Internet Engineering Task Force)により正式な標準仕様として承認された。

なお、[[../../application/http/HTTP.md#HTTP/3|HTTP/3]]はQUICの上で動作する。このHTTP/3は現状、多数のサーバーで採用されている。

## TCPと比較

| 項目       | TCP + TLS     | QUIC           |
| -------- | ------------- | -------------- |
| ベース      | TCP           | UDP            |
| 暗号化      | 別（TLS）        | 組み込み（TLS 1.3）  |
| 接続確立     | 複数ラウンド        | 1-RTT or 0-RTT |
| ストリーム    | 全体が止まる（HoLあり） | 独立（HoLなし）      |
| 接続遮断への対応 | 再接続が必要        | コネクション維持可能     |
### セキュリティと拡張性

暗号化された状態で通信されるため、**中継装置（ミドルボックス）による最適化が難しい**。だがその分、**プロトコルの進化が高速にできる**というメリットもある。