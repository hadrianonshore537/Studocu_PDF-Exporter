# StudocuHack

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

StudocuHack은 지원되는 Studocu 문서 페이지를 처리하여 PDF로 저장하는 Windows 데스크톱 애플리케이션입니다. 이해하기 쉬운 화면, 저장 폴더 선택, 실시간 진행 상태, 색상 로그 및 자동 대체 처리 방식을 제공합니다.

> 접근 권한이 있는 문서에만 이 프로젝트를 사용하세요. 저작권, 플랫폼 이용 약관 및 관련 법률을 준수해야 합니다.

## 주요 기능

- 단계별 안내가 포함된 명확한 데스크톱 UI
- 10개 언어를 지원하는 내장 인터페이스 언어 선택기
- 화면 크기에 따른 자동 창 크기 조절
- PDF 저장 폴더 선택
- 실시간 상태, 진행률 표시줄 및 색상 로그
- 로컬에 설치된 Microsoft Edge 사용
- 여러 문서 추출 및 PDF 생성 대체 방식
- Python 설치가 필요 없는 독립 실행형 Windows EXE

## EXE 직접 사용

1. 최신 GitHub Release에서 `StudocuHack.exe`를 다운로드하거나 [`dist/StudocuHack.exe`](dist/StudocuHack.exe)를 사용합니다.
2. Microsoft Edge가 설치되어 있는지 확인합니다.
3. 작업을 저장하고 모든 Edge 창을 닫습니다.
4. `StudocuHack.exe`를 실행합니다.
5. 지원되는 Studocu 문서 URL을 붙여넣습니다.
6. 저장 폴더를 선택하고 **PDF 다운로드 시작**을 클릭합니다.
7. 처리가 끝나면 생성된 PDF를 엽니다.

EXE에는 Python, PyQt5 및 Playwright 런타임이 포함되어 있습니다.

### Windows 주의사항

- 현재 애플리케이션은 시작 및 종료 시 실행 중인 Microsoft Edge 프로세스를 닫습니다. 먼저 브라우저 작업을 저장하세요.
- EXE는 디지털 서명이 없으므로 Windows SmartScreen 또는 백신 프로그램이 경고할 수 있습니다.
- Windows 10/11 64비트와 Microsoft Edge가 필요합니다.

## 소스 코드에서 실행

### 요구 사항

- Windows 10/11 64비트
- Microsoft Edge
- Python 3.11

```powershell
git clone <저장소-주소>
cd Studocu-Rehelper-main

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## EXE 빌드

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

스크립트는 `.venv`를 만들고 필요한 의존성을 설치한 후 다음 파일을 생성합니다.

```text
dist\StudocuHack.exe
```

## 프로젝트 구조

```text
studocuhack_desktop.py   데스크톱 애플리케이션 소스 코드
requirements.txt         Python 의존성
build_exe.ps1            Windows 빌드 스크립트
StudocuHack.spec         PyInstaller 설정
img/icon128.ico          애플리케이션 아이콘
dist/StudocuHack.exe     빌드된 Windows 실행 파일
```

## 문제 해결

- **Edge를 찾을 수 없음:** Microsoft Edge를 기본 위치에 설치하세요.
- **문서가 로드되지 않음:** 먼저 Edge에서 열어 접근 가능한지 확인하세요.
- **Windows가 EXE를 차단함:** 이 저장소 또는 공식 Release 페이지에서 받은 파일만 사용하세요.
- **첫 실행이 느림:** 단일 파일 EXE가 내부 런타임을 먼저 압축 해제합니다.

## 기여

Issue, 번역, 문서 개선 및 Pull Request를 환영합니다.

## 라이선스

저장소를 공개하기 전에 적절한 라이선스 파일을 추가하세요.
