---
title: OGSP Seismometer
description: 
lead: 
tags:
  - MOC
aliases:
  - 地震計
date: 2025-05-16T23:02:10+09:00
lastmod: 2025-05-16T23:02:10+09:00
draft: true
showContent: true
slug: about
---
**OGSP Seismometer**は、[OGSP](../../OGSP.md)の一部である地震計を提供するファームウェアまたはプログラムの名称である。[OGSP Disaster Network](../../network/OGSP%20Disaster%20Network.md)では、センサー層の地象観測群に属する。

## 設計
OGSP Seismometerは、地震動そのものや長周期地震動の観測、地震の規模の推定、その他様々な研究用途に使用するための、そのデータ収集とネットワーク側への送信を目的とする、センサー層として動作する。

地震計自体は地震波検出などの高度な計算を行う必要はなく、ESP32やRaspberry Pi Pico (未サポート)などのマイコンで簡単に作ることができる。

使用する加速度センサはある程度精度の高いものを使用する必要があるが、1万円未満で導入できることを目指しており、たくさん設置することに重点を置いている。たくさん設置することで、マルチサンプリングなどを活用して精度を向上させることも**理論上は可能**。