# Studocu PDF Exporter

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

접근 권한이 있는 Studocu 문서를 PDF로 내보내기 위한 다국어 Windows 데스크톱 도구입니다. 단계별 안내, 저장 폴더 선택, 실시간 진행률 및 색상 로그를 제공합니다.

> **교육 및 연구 목적으로만 사용:** 이 프로젝트는 학습, 연구 및 기술 참고만을 위한 것입니다. Studocu와 제휴, 승인 또는 공식 허가 관계가 없습니다. 유료 장벽, 접근 제어 또는 저작권 보호를 우회하는 데 사용하지 마세요.

## 다운로드

- [최신 릴리스](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)
- [StudocuHack.exe 직접 다운로드](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest/download/StudocuHack.exe)

EXE에는 Python, PyQt5 및 Playwright 런타임이 포함되어 있으므로 Python을 별도로 설치할 필요가 없습니다.

## 주요 기능

- 명확한 3단계 작업 흐름
- 10개 언어를 지원하는 내장 언어 선택기
- 화면에 맞춘 자동 창 크기 조절
- PDF 저장 폴더 선택
- 실시간 상태, 진행률 표시줄 및 색상 로그
- 로컬에 설치된 Microsoft Edge 사용
- 여러 PDF 생성 대체 방식
- 독립 실행형 Windows EXE

## EXE 사용 방법

1. [최신 릴리스](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)에서 `StudocuHack.exe`를 다운로드합니다.
2. Microsoft Edge가 설치되어 있는지 확인합니다.
3. 브라우저 작업을 저장하고 모든 Edge 창을 닫습니다.
4. `StudocuHack.exe`를 실행합니다.
5. 인터페이스 언어를 선택합니다.
6. 접근 권한이 있는 Studocu 문서 URL을 붙여넣습니다.
7. 저장 폴더를 선택하고 PDF 다운로드를 시작합니다.
8. 처리가 끝나면 생성된 PDF를 엽니다.

### Windows 안내

- 현재 앱은 시작 및 종료 시 실행 중인 Edge 프로세스를 종료합니다.
- EXE는 디지털 서명되지 않았으므로 Windows SmartScreen 또는 백신이 경고를 표시할 수 있습니다.
- EXE는 이 저장소의 공식 Releases 페이지에서만 다운로드하세요.

## 소스 코드로 실행

요구 사항: Windows 10/11 64비트, Microsoft Edge 및 Python 3.11.

```powershell
git clone https://github.com/liqiheng777/Studocu_PDF-Exporter.git
cd Studocu_PDF-Exporter

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## EXE 빌드

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

생성된 파일은 `dist\StudocuHack.exe`에 있습니다.

## 합법적이고 책임 있는 사용

- 직접 만들었거나 소유하고 있거나 명시적으로 내보내기 권한을 받은 문서만 처리하세요.
- 저작권, 개인정보 보호, 학문적 진실성, Studocu 이용 약관 및 관련 법률을 준수하세요.
- 구독, 유료 장벽, 인증 또는 접근 제어를 우회하는 데 사용하지 마세요.
- Studocu는 해당 권리자의 상표입니다. 이 독립 프로젝트는 Studocu와 공식 관계가 없습니다.

## MIT 라이선스

Copyright (c) 2026 QIHENG

본 소프트웨어 및 관련 문서 파일(이하 “소프트웨어”)의 사본을 취득하는 모든 사람에게 소프트웨어를 제한 없이 취급할 수 있는 권리를 무료로 부여합니다. 여기에는 소프트웨어를 사용, 복사, 수정, 병합, 게시, 배포, 재라이선스 및/또는 판매할 권리와 소프트웨어를 제공받은 사람이 이를 수행하도록 허용할 권리가 포함되며, 이에 국한되지 않습니다. 단, 다음 조건을 따라야 합니다.

위 저작권 고지와 본 허가 고지는 소프트웨어의 모든 사본 또는 상당 부분에 포함되어야 합니다.

본 소프트웨어는 상품성, 특정 목적에 대한 적합성 및 비침해에 대한 보증을 포함하되 이에 국한되지 않는 어떠한 명시적 또는 묵시적 보증 없이 “있는 그대로” 제공됩니다. 어떠한 경우에도 저작자 또는 저작권자는 계약, 불법 행위 또는 기타 사유로 인한 것인지 여부와 관계없이 소프트웨어, 소프트웨어의 사용 또는 소프트웨어와 관련된 기타 거래에서 발생하는 청구, 손해 또는 기타 책임에 대해 책임을 지지 않습니다.

공식 라이선스 본문은 영어 [LICENSE](LICENSE) 파일입니다.
