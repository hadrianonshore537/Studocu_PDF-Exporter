# Studocu PDF Exporter

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

アクセス権限を持つ Studocu 文書を PDF としてエクスポートするための、多言語対応 Windows デスクトップツールです。操作ガイド、保存先の選択、リアルタイム進捗、色分けされたログを提供します。

> **教育・研究目的のみ：** 本プロジェクトは、学習、研究、技術的な参考のみを目的としています。Studocu との提携、承認、許可はありません。ペイウォール、アクセス制御、著作権保護を回避する目的では使用しないでください。

## ダウンロード

- [最新リリース](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)
- [StudocuHack.exe を直接ダウンロード](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest/download/StudocuHack.exe)

EXE には Python、PyQt5、Playwright ランタイムが含まれているため、Python のインストールは不要です。

## 機能

- 分かりやすい 3 ステップの操作フロー
- 10 言語に対応した内蔵言語切り替え
- 画面に応じたウィンドウサイズの自動調整
- PDF 保存先フォルダーの選択
- リアルタイム状態、進捗バー、色分けログ
- ローカルにインストールされた Microsoft Edge を使用
- 複数の PDF 生成代替方式
- 単体で動作する Windows EXE

## EXE の使い方

1. [最新リリース](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)から `StudocuHack.exe` をダウンロードします。
2. Microsoft Edge がインストールされていることを確認します。
3. ブラウザー上の作業を保存し、すべての Edge ウィンドウを閉じます。
4. `StudocuHack.exe` を起動します。
5. インターフェース言語を選択します。
6. アクセス権限を持つ Studocu 文書の URL を貼り付けます。
7. 保存先を選び、PDF ダウンロードを開始します。
8. 処理完了後、生成された PDF を開きます。

### Windows に関する注意

- 現在、アプリは起動時と終了時に実行中の Edge プロセスを終了します。
- EXE はデジタル署名されていないため、Windows SmartScreen やウイルス対策ソフトが警告を表示する場合があります。
- EXE は本リポジトリの公式 Releases ページからのみダウンロードしてください。

## ソースコードから実行

要件：Windows 10/11 64 ビット、Microsoft Edge、Python 3.11。

```powershell
git clone https://github.com/liqiheng777/Studocu_PDF-Exporter.git
cd Studocu_PDF-Exporter

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## EXE のビルド

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

生成ファイルは `dist\StudocuHack.exe` にあります。

## 適法かつ責任ある利用

- 自分で作成した文書、所有する文書、または明示的にエクスポートを許可された文書のみを処理してください。
- 著作権、プライバシー、学術的誠実性、Studocu の利用規約、適用法令を遵守してください。
- サブスクリプション、ペイウォール、認証、アクセス制御の回避には使用しないでください。
- Studocu は各権利者の商標です。本プロジェクトは Studocu と公式な関係を持たない独立プロジェクトです。

## MIT ライセンス

Copyright (c) 2026 QIHENG

本ソフトウェアおよび関連文書ファイル（以下「ソフトウェア」）の複製を取得するすべての者に対し、ソフトウェアを使用、複製、変更、結合、公開、配布、サブライセンス、および／または販売する権利を含むがこれらに限定されない、ソフトウェアを制限なく取り扱う権利を無償で許可します。また、ソフトウェアを提供された者が同様に行うことを、以下の条件に従って許可します。

上記の著作権表示および本許諾表示は、ソフトウェアのすべての複製または重要な部分に記載するものとします。

本ソフトウェアは「現状のまま」提供され、商品性、特定目的への適合性、および権利非侵害に関する保証を含むがこれらに限定されない、明示または黙示を問わず、いかなる種類の保証もありません。著作者または著作権者は、契約、不法行為、その他の行為に起因するかを問わず、ソフトウェア、ソフトウェアの使用、またはその他の取引から生じるいかなる請求、損害、その他の責任についても責任を負いません。

正式なライセンス本文は英語の [LICENSE](LICENSE) ファイルです。
