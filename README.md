# Studocu PDF Exporter

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

A multilingual Windows desktop tool for exporting Studocu documents that you are authorized to access as PDF files. The application provides guided operation, a selectable output folder, live progress, colored logs, and multiple PDF generation strategies.

> **Educational use only:** This project is intended solely for learning, research, and technical reference. It is not affiliated with, endorsed by, or authorized by Studocu. Do not use it to bypass paywalls, access controls, copyright protections, or to obtain content you are not authorized to access.

## Download

For most users, download the latest Windows executable from:

- [Latest Release](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)
- [Direct download: StudocuHack.exe](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest/download/StudocuHack.exe)

The EXE includes Python, PyQt5, and the Playwright runtime. Python does not need to be installed.

## Features

- Clear three-step desktop workflow
- Built-in interface switcher supporting 10 languages
- Automatically sized window for different screens
- Selectable PDF output directory
- Live status, progress bar, and colored processing logs
- Uses the locally installed Microsoft Edge browser
- Multiple PDF generation fallback strategies
- Standalone Windows executable

## Use the EXE

1. Download `StudocuHack.exe` from the [latest release](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest).
2. Make sure Microsoft Edge is installed.
3. Save your browser work and close all Edge windows.
4. Run `StudocuHack.exe`.
5. Select your preferred interface language.
6. Paste a Studocu document URL that you are authorized to access.
7. Select an output folder and click **Start PDF Download**.
8. Wait for processing to finish, then open the generated PDF.

### Windows Notice

- The application currently closes running Microsoft Edge processes when starting and exiting. Save your browser work first.
- The EXE is not digitally signed, so Windows SmartScreen or antivirus software may display a warning.
- Only download the EXE from this repository's official Releases page.

## Run From Source

### Requirements

- Windows 10/11 64-bit
- Microsoft Edge
- Python 3.11

### Installation

```powershell
git clone https://github.com/liqiheng777/Studocu_PDF-Exporter.git
cd Studocu_PDF-Exporter

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## Build the EXE

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

The build script creates:

```text
dist\StudocuHack.exe
```

## Project Structure

```text
studocuhack_desktop.py   Desktop application source code
requirements.txt         Python dependencies
build_exe.ps1            One-click Windows build script
StudocuHack.spec         PyInstaller build configuration
img/icon128.ico          Application icon
README*.md               Multilingual documentation
```

## Legal and Responsible Use

- Only process documents that you created, own, or are explicitly authorized to access and export.
- Respect copyright, privacy, academic integrity, Studocu's terms of service, and applicable laws.
- Do not use this project to bypass subscriptions, paywalls, authentication, technical restrictions, or access controls.
- The maintainers do not encourage infringement and are not responsible for misuse.
- Studocu is a trademark of its respective owner. This independent project has no official relationship with Studocu.

## Troubleshooting

**Edge cannot be found:** Install Microsoft Edge in its default Windows location.

**The document does not load:** Open the document in Edge first and confirm that your account is authorized to access it.

**Windows blocks the EXE:** Confirm that it came from the official Releases page, then review the warning before continuing.

**The first launch is slow:** The single-file EXE extracts its bundled runtime before opening.

## MIT License

Copyright (c) 2026 QIHENG

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

See the canonical license text in [LICENSE](LICENSE).
