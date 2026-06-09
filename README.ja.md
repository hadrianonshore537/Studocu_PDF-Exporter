# StudocuHack

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

StudocuHack は、対応する Studocu ドキュメントページを処理して PDF として保存する Windows デスクトップアプリです。分かりやすい画面、保存先の選択、リアルタイム進捗、色分けされたログ、自動フォールバック処理を備えています。

> アクセス権限のあるドキュメントにのみ使用してください。著作権、プラットフォームの利用規約、適用される法律を遵守してください。

## 機能

- 手順ガイド付きの分かりやすいデスクトップ画面
- 10 言語に対応した内蔵の表示言語切り替え
- 画面サイズに応じたウィンドウの自動調整
- PDF 保存先フォルダーの選択
- リアルタイム状態、進捗バー、色分けログ
- ローカルにインストールされた Microsoft Edge を使用
- 複数のドキュメント抽出・PDF 作成フォールバック方式
- Python のインストールが不要な Windows EXE

## EXE を直接使用する

1. 最新の GitHub Release から `StudocuHack.exe` をダウンロードするか、[`dist/StudocuHack.exe`](dist/StudocuHack.exe) を使用します。
2. Microsoft Edge がインストールされていることを確認します。
3. 作業を保存し、すべての Edge ウィンドウを閉じます。
4. `StudocuHack.exe` を実行します。
5. 対応する Studocu ドキュメント URL を貼り付けます。
6. 保存先を選び、**PDF ダウンロード開始**をクリックします。
7. 処理完了後、生成された PDF を開きます。

EXE には Python、PyQt5、Playwright ランタイムが含まれています。

### Windows に関する注意

- 現在のアプリは起動時と終了時に実行中の Microsoft Edge プロセスを終了します。先にブラウザー上の作業を保存してください。
- EXE はデジタル署名されていないため、Windows SmartScreen やウイルス対策ソフトが警告する場合があります。
- Windows 10/11 64 ビット版と Microsoft Edge が必要です。

## ソースコードから実行する

### 必要環境

- Windows 10/11 64 ビット
- Microsoft Edge
- Python 3.11

```powershell
git clone <リポジトリURL>
cd Studocu-Rehelper-main

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## EXE をビルドする

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

スクリプトは `.venv` を作成し、必要な依存関係をインストールして次のファイルを生成します。

```text
dist\StudocuHack.exe
```

## プロジェクト構成

```text
studocuhack_desktop.py   デスクトップアプリのソースコード
requirements.txt         Python 依存関係
build_exe.ps1            Windows 用ビルドスクリプト
StudocuHack.spec         PyInstaller 設定
img/icon128.ico          アプリアイコン
dist/StudocuHack.exe     ビルド済み Windows 実行ファイル
```

## トラブルシューティング

- **Edge が見つからない:** Microsoft Edge を標準の場所にインストールしてください。
- **ドキュメントが読み込まれない:** 先に Edge で開き、アクセス可能か確認してください。
- **Windows が EXE をブロックする:** このリポジトリまたは公式 Release ページから取得したファイルのみ使用してください。
- **初回起動が遅い:** 単一ファイル EXE は起動前に内部ランタイムを展開します。

## コントリビューション

Issue、翻訳、ドキュメント改善、Pull Request を歓迎します。

## ライセンス

リポジトリを公開する前に、適切なライセンスファイルを追加してください。
