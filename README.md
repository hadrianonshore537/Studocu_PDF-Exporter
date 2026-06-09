# StudocuHack

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

StudocuHack is a Windows desktop application that processes supported Studocu document pages and saves them as PDF files. It provides a clear graphical interface, selectable output directory, live progress, colored logs, and automatic fallback strategies.

> Use this project only for documents you are authorized to access. Respect copyright, platform terms, and applicable laws.

## Features

- Simple desktop interface with step-by-step guidance
- Built-in interface language switcher with 10 languages
- Automatically sized window for large and small screens
- Selectable PDF output directory
- Live status, progress bar, and colored processing logs
- Uses the locally installed Microsoft Edge browser
- Multiple document extraction and PDF generation fallback strategies
- Standalone Windows EXE for users who do not want to install Python

## Use the EXE

This is the easiest option for most users.

1. Download `StudocuHack.exe` from the latest GitHub Release, or use [`dist/StudocuHack.exe`](dist/StudocuHack.exe).
2. Make sure Microsoft Edge is installed.
3. Save your work and close all Edge windows.
4. Run `StudocuHack.exe`.
5. Paste a supported Studocu document URL.
6. Select an output folder and click **Start Download PDF**.
7. Wait for processing to finish, then click **Open generated PDF**.

The EXE already includes Python, PyQt5, and the Playwright runtime. Python does not need to be installed.

### Windows warning

- The application currently closes running Microsoft Edge processes when starting and exiting. Save your browser work first.
- The EXE is not digitally signed, so Windows SmartScreen or antivirus software may display a warning.
- The application requires Windows 10/11 64-bit and Microsoft Edge.

## Run From Source

### Requirements

- Windows 10/11 64-bit
- Microsoft Edge
- Python 3.11

### Installation

```powershell
git clone <your-repository-url>
cd Studocu-Rehelper-main

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## Build the EXE

The repository includes a PyInstaller configuration and one-click build script.

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

The script automatically creates `.venv`, installs dependencies when needed, and builds:

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
dist/StudocuHack.exe     Prebuilt Windows executable
```

## Troubleshooting

**Edge cannot be found**

Install Microsoft Edge in its default Windows location.

**The document does not load**

Open the document in Edge first, confirm that it is accessible, then try again.

**Windows blocks the EXE**

Only continue if you downloaded it from this repository or its official Release page. You may need to choose **More info → Run anyway**.

**The first launch is slow**

The single-file EXE extracts its bundled runtime before opening, which can take several seconds.

## Contributing

Issues, translations, documentation improvements, and pull requests are welcome.

## License

Add a license file before publishing the repository. Choose a license that matches how you want others to use and redistribute the project.
