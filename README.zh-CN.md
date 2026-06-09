# Studocu PDF Exporter

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

一款多语言 Windows 桌面工具，用于将用户有权访问的 Studocu 文档导出为 PDF。软件提供清晰的操作引导、可选保存目录、实时进度、彩色日志以及多种 PDF 生成方案。

> **仅供学习与研究：** 本项目仅用于学习、研究和技术参考，与 Studocu 官方无关，未获得 Studocu 的认可或授权。不得使用本项目绕过付费墙、访问控制、版权保护，或获取无权访问的内容。

## 下载程序

普通用户推荐直接下载最新版 Windows 程序：

- [最新 Release 页面](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)
- [直接下载 StudocuHack.exe](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest/download/StudocuHack.exe)

EXE 已包含 Python、PyQt5 和 Playwright 运行环境，无需另外安装 Python。

## 功能特点

- 清晰易懂的三步操作引导
- 内置界面语言切换，支持 10 种语言
- 根据屏幕大小自动调整窗口尺寸
- 可自由选择 PDF 保存目录
- 实时状态、进度条与彩色处理日志
- 使用电脑本地安装的 Microsoft Edge
- 多种 PDF 生成备用方案
- 提供独立 Windows EXE

## 使用 EXE

1. 从[最新 Release](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)下载 `StudocuHack.exe`。
2. 确保电脑已安装 Microsoft Edge。
3. 保存浏览器中的工作并关闭所有 Edge 窗口。
4. 运行 `StudocuHack.exe`。
5. 选择需要的界面语言。
6. 粘贴你有权访问的 Studocu 文档链接。
7. 选择保存目录，然后点击“开始下载 PDF”。
8. 等待处理完成，再打开生成的 PDF。

### Windows 使用提醒

- 软件启动和退出时目前会关闭正在运行的 Microsoft Edge，请提前保存浏览器工作。
- EXE 尚未进行数字签名，Windows SmartScreen 或杀毒软件可能显示警告。
- 请仅从本仓库官方 Releases 页面下载 EXE。

## 从源代码运行

### 环境要求

- Windows 10/11 64 位
- Microsoft Edge
- Python 3.11

### 安装与运行

```powershell
git clone https://github.com/liqiheng777/Studocu_PDF-Exporter.git
cd Studocu_PDF-Exporter

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## 打包 EXE

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

打包完成后生成：

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
README*.md               多语言说明文档
```

## 合规与责任说明

- 仅处理由你创建、归你所有，或明确获得访问与导出授权的文档。
- 请遵守版权、隐私、学术诚信、Studocu 服务条款及适用法律。
- 不得使用本项目绕过订阅、付费墙、身份验证、技术限制或访问控制。
- 项目维护者不鼓励任何侵权行为，也不对滥用行为承担责任。
- Studocu 是其权利人的商标，本独立项目与 Studocu 不存在官方关系。

## 常见问题

**提示找不到 Edge：** 请将 Microsoft Edge 安装在 Windows 默认目录。

**文档无法加载：** 先在 Edge 中打开文档，并确认你的账户已获授权访问。

**Windows 阻止运行 EXE：** 请确认文件来自官方 Releases 页面，并仔细查看警告后再决定是否运行。

**首次启动较慢：** 单文件 EXE 启动前需要解压内置运行环境。

## MIT 许可证

版权所有 (c) 2026 QIHENG

特此免费授予任何获得本软件及相关文档文件（以下简称“软件”）副本的人不受限制地处理本软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售本软件副本的权利，并允许获得本软件的人这样做，但须符合以下条件：

上述版权声明和本许可声明应包含在本软件的所有副本或主要部分中。

本软件按“原样”提供，不提供任何形式的明示或默示保证，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对因本软件或本软件的使用或其他交易而产生、引起或与之相关的任何索赔、损害或其他责任承担责任，无论该责任是基于合同、侵权行为还是其他原因。

正式许可文本以英文 [LICENSE](LICENSE) 文件为准。
