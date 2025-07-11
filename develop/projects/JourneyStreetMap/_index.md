---
title: JourneyStreetMap
description: A library to display JourneyMap maps on your website.
draft: false
created: 2025-04-03T04:18:58+09:00
modified: 2025-07-11T11:12:35+09:00
aliases:
  - JourneyStreetMap
  - JSM
---
> [!WARNING]
> このプロジェクトは開発が停止しています。詳しくは[[JSM is not longer under the develop|こちら]]。
## 仕組み

### 1. JourneyMapのデータを読み込む
まず、[JourneyMap](https://www.curseforge.com/minecraft/mc-mods/journeymap)というのは、Minecraftでマップを表示するModです。

このModで保存されるワールドデータを抽出します。  
→Anvilファイルフォーマット、NBTデータ

### 2. アプリ画面に表示
> 適当に[[develop/Knowledge/lang/programming/Rust/_index|Rust]]で組んどくかー

うぇい。

### 3. マップデータを編集
アプリ画面上で道路とか地点を追加したりします。

ここには[[GUI library|GUIライブラリ]]を使用するとやりやすいかもしれんね

### 4. PMTilesにエクスポート
PMTiles形式の１つのファイルにエクスポートすると使いやすいよね〜！

### 5. GSIとして見る
例えばGoogle Mapsみたいなサービスのように、マイクラの地図も見られるように編集可能だったりします。