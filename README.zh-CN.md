# StudocuHack

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

StudocuHack 是一款 Windows 桌面应用，用于处理受支持的 Studocu 文档页面并保存为 PDF。软件提供清晰的图形界面、可选保存目录、实时进度、彩色日志以及自动降级处理方案。

> 请仅处理你有权访问的文档，并遵守版权、平台条款与当地法律。

## 功能特点

- 清晰易懂的桌面界面与三步使用引导
- 内置界面语言切换，支持 10 种语言
- 根据屏幕大小自动调整窗口尺寸
- 可自由选择 PDF 保存目录
- 实时状态、进度条与彩色处理日志
- 使用电脑本地安装的 Microsoft Edge
- 多种文档提取与 PDF 生成备用方案
- 提供无需安装 Python 的 Windows EXE

## 直接使用 EXE

这是最适合普通用户的使用方式。

1. 从最新 GitHub Release 下载 `StudocuHack.exe`，或使用 [`dist/StudocuHack.exe`](dist/StudocuHack.exe)。
2. 确保电脑已安装 Microsoft Edge。
3. 保存浏览器中的工作并关闭所有 Edge 窗口。
4. 运行 `StudocuHack.exe`。
5. 粘贴受支持的 Studocu 文档链接。
6. 选择保存目录，然后点击“开始下载 PDF”。
7. 等待处理完成，再点击“打开生成的 PDF”。

EXE 已包含 Python、PyQt5 和 Playwright 运行环境，无需另外安装 Python。

### Windows 使用提醒

- 软件启动和退出时目前会关闭正在运行的 Microsoft Edge，请提前保存浏览器工作。
- EXE 尚未进行数字签名，Windows SmartScreen 或杀毒软件可能会显示警告。
- 软件需要 Windows 10/11 64 位系统与 Microsoft Edge。

## 从源代码运行

### 环境要求

- Windows 10/11 64 位
- Microsoft Edge
- Python 3.11

### 安装与运行

```powershell
git clone <你的仓库地址>
cd Studocu-Rehelper-main

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## 打包 EXE

项目已经提供 PyInstaller 配置和一键打包脚本：

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

脚本会自动创建 `.venv`、安装缺失依赖，并生成：

```text
dist\StudocuHack.exe
```

## 项目结构

```text
studocuhack_desktop.py   桌面应用源代码
requirements.txt         Python 依赖
build_exe.ps1            Windows 一键打包脚本
StudocuHack.spec         PyInstaller 打包配置
img/icon128.ico          程序图标
dist/StudocuHack.exe     已构建的 Windows 程序
```

## 常见问题

**提示找不到 Edge**

请将 Microsoft Edge 安装在 Windows 默认目录。

**文档无法加载**

先在 Edge 中打开文档并确认可以访问，然后重新尝试。

**Windows 阻止运行 EXE**

请确认文件来自本仓库或官方 Release 页面，然后可选择“更多信息 → 仍要运行”。

**首次启动较慢**

单文件 EXE 启动前需要解压内置运行环境，可能需要等待几秒。

## 参与贡献

欢迎提交 Issue、翻译、文档改进和 Pull Request。

## 开源许可证

发布仓库前请添加许可证文件，并根据你希望他人如何使用和分发本项目来选择合适的许可证。
