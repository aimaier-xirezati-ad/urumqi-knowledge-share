# ウルムチから来ました

ウルムチ出身者が新疆とウルムチを紹介する、スクロール型のナレッジシェア用ページです。

- 新疆の輪郭に同じ縮尺の日本を重ねる地図（ドラッグで移動できます）
- 東京からウルムチまでの飛行を、昼夜の影つきの地球儀で再生
- 東京、北京時間、新疆時間の3つの時計
- 海から一番遠い大都市を示す正距方位図、世界の両極端と比べる日の出・日の入り
- 実際の標高データと衛星写真で作った新疆の3D地形を、スクロールで北から南へ飛ぶ
- 料理、楽器、ことば（アラビア文字とラテン文字）、旅行のヒント
- このページの作り方（使ったOSSと、途中であったこと）

## 見る

`index.html` をブラウザで開くだけで表示できます（ライブラリはCDNから読み込むため、ネット接続が必要です）。

ただし、ファイルを直接開く（`file://`）と、ブラウザの制限で3D地形の衛星写真が読み込めず、簡易な色分けで表示されます。ローカルできれいに見るときは、このフォルダで次を実行して http://localhost:8000 を開いてください。

```bash
python3 -m http.server 8000
```

発表中は `→` / `←` キーで章を移動できます。

## GitHub Pagesで公開する

```bash
git init && git add . && git commit -m "Urumqi knowledge share"
git branch -M main
git remote add origin git@github.com:<あなたのアカウント>/urumqi-knowledge-share.git
git push -u origin main
```

リポジトリの **Settings → Pages → Branch: main / (root)** を選ぶと、数分で `https://<アカウント>.github.io/urumqi-knowledge-share/` に公開されます。

## ファイル構成

| パス | 内容 |
|---|---|
| `src/page.html` | 編集するのはこのファイル |
| `build.py` | `src/page.html` に地図・地形データ（geo.js / world.js / terrain.js）とクレジットを埋め込み、`index.html` を作る |
| `index.html` | GitHub Pages用の完成版（自動生成） |
| `artifact.html` | claude.ai Artifact用（自動生成） |
| `geo.js` | 新疆と日本の輪郭（簡略化済みのGeoJSON座標） |
| `terrain.js` | 3D地形用の標高データ（640×572点、4m単位の差分をzlib圧縮してBase64化） |
| `world.js` | 地球儀用の世界の陸地と中国の輪郭（world-atlas 110m から変換） |
| `images/` | 写真と `credits.json`（撮影者・ライセンス）、3D地形用の衛星写真 `xj-satellite.jpg` |

文章を直したら `python3 build.py` を実行してください。

## 使ったもの

- [three.js](https://github.com/mrdoob/three.js)：3D地形
- [AWS Terrain Tiles](https://registry.opendata.aws/terrain-tiles/)：標高データ（Mapzen / SRTM ほか）
- [NASA Blue Marble Next Generation](https://earthobservatory.nasa.gov/features/BlueMarble)：3D地形の衛星写真（NASA GIBS から取得）
- [GSAP / ScrollTrigger](https://github.com/greensock/GSAP)：スクロール演出
- [d3-geo](https://github.com/d3/d3-geo)：正積方位図法で地図を描画
- [dataofjapan/land](https://github.com/dataofjapan/land)：日本の輪郭データ
- [topojson/world-atlas](https://github.com/topojson/world-atlas)：地球儀の陸地データ（Natural Earth）
- [DataV.GeoAtlas](https://datav.aliyun.com/portal/school/atlas/area_selector)：新疆の輪郭データ
- [Wikimedia Commons](https://commons.wikimedia.org/)：写真

## 写真のライセンス

写真はすべてWikimedia Commonsのもので、CC BY / CC BY-SA / CC0 / パブリックドメインです。撮影者とライセンスは `images/credits.json` とページ下部のクレジットに載せています。公開するときは、クレジット表記を消さないでください。
