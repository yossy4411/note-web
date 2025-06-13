---
title: JourneyStreetMapとは
description: '"JourneyStreetMap Project" について'
lead: 
tags: 
aliases:
  - journeystreetmap
  - JSM
date: 2025-04-04T15:50:47+09:00
lastmod: 2025-04-04T21:24:04+09:00
draft: false
showContent: true
slug: about
---
> [!WARNING]
> このプロジェクトは開発が停止しています。詳しくは[[JSMの開発停止|こちら]]。
## 仕組み

### 1. JourneyMapのデータを読み込む
まず、[JourneyMap](https://www.curseforge.com/minecraft/mc-mods/journeymap)というのは、Minecraftでマップを表示するModです。

このModで保存されるワールドデータを抽出します。  
→Anvilファイルフォーマット、NBTデータ

### 2. アプリ画面に表示
> 適当に[[Rust]]で組んどくかー

うぇい。

### 3. マップデータを編集
アプリ画面上で道路とか地点を追加したりします。

ここには[[GUIライブラリ]]を使用するとやりやすいかもしれんね

### 4. PMTilesにエクスポート
PMTiles形式の１つのファイルにエクスポートすると使いやすいよね〜！

### 5. GSIとして見る
例えばGoogle Mapsみたいなサービスのように、マイクラの地図も見られるように編集可能だったりします。