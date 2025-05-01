---
title: HTTP/3
description: 
lead: 
tags: 
aliases:
  - HTTP/3
date: 2025-04-30T22:52:22+09:00
lastmod: 2025-04-30T22:52:22+09:00
draft: false
showContent: false
slug: "3"
---
**HTTP/3** は、[HTTP2](HTTP2.md)に続く[HTTP](HTTP.md)の3つ目のメジャーバージョンであり、最新版である。2022年に RFC 9114 によって正式化された。

## 概要
HTTP/3は、RFCドラフト「HTTP over QUIC」をベースとしている。[QUIC](../../transport/quic/QUIC.md)はGoogleによってはじめに開発された、[トランスポート層](../../transport/トランスポート層.md)のプロトコルである。

もっとも、通信プロトコルの基盤が[TCP](../../transport/tcp/TCP.md)から[UDP](../../transport/udp/UDP.md)ベースの[QUIC](../../transport/quic/QUIC.md)に変化したことが最大の変化である。

## 特徴
### QUICプロトコルベース
HTTP/3は、[TCP/IP](../../TCP-IP.md)接続から進化して、[UDP](../../transport/udp/UDP.md)上に築かれた[QUIC](../../transport/quic/QUIC.md)という新しいプロトコルを使用する。これにより、[0-RTT接続](0-RTT接続.md)が可能である。

また、QUICの機能を活かし、再接続なしで接続の再開ができる。

### 真・並列通信
TCPの越えられなかった制限を超え、パケットロスがあっても他ストリームには影響しないというUDPの特性を活かす。これによって、Head-of-Line Blockingが完全に解消できる。

### TLSの内蔵
QUICでは暗号化(TLS 1.3)が標準化されていて、通信は常にセキュアである。ハンドシェイクと暗号化処理が一体化しており、高速かつ安全に通信を行うことができる設計。

## 課題
- UDPをブロックする設計のネットワークではそもそも使用できない。
- 実装が複雑なため、マイナーな言語やツールでは非対応の部分がある。

## 比較
(ChatGPTによる生成)

| 項目        | [HTTP1.1](HTTP1.1.md)             | [HTTP/2](HTTP2.md)                | HTTP/3                                                                   |
| --------- | --------------------------------- | --------------------------------- | ------------------------------------------------------------------------ |
| 通信方式      | [TCP](../../transport/tcp/TCP.md) | [TCP](../../transport/tcp/TCP.md) | [UDP](../../transport/udp/UDP.md)（+[QUIC](../../transport/quic/QUIC.md)） |
| マルチプレクシング | ×（順番に処理）                          | ◯（1接続で並列）                         | ◎（独立して並列）                                                                |
| HOL問題     | ×（がっつり）                           | △（少しあり）                           | ◎（完全解消）                                                                  |
| 暗号化       | 任意（TLS対応）                         | 任意（TLS推奨）                         | 強制（TLS 1.3内蔵）                                                            |
| ヘッダ圧縮     | ×                                 | ◯（HPACK）                          | ◯（QPACK）                                                                 |
| サーバープッシュ  | ×                                 | ◯（あり）                             | △（非推奨傾向）                                                                 |
