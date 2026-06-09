# StudocuHack

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

StudocuHack là ứng dụng máy tính Windows dùng để xử lý các trang tài liệu Studocu được hỗ trợ và lưu thành PDF. Ứng dụng có giao diện rõ ràng, thư mục lưu tùy chọn, tiến trình trực tiếp, nhật ký màu và các phương án dự phòng tự động.

> Chỉ sử dụng dự án này với tài liệu mà bạn được phép truy cập. Hãy tuân thủ bản quyền, điều khoản nền tảng và pháp luật hiện hành.

## Tính năng

- Giao diện máy tính rõ ràng với hướng dẫn từng bước
- Bộ chọn ngôn ngữ tích hợp hỗ trợ 10 ngôn ngữ
- Tự động điều chỉnh kích thước cửa sổ theo màn hình
- Có thể chọn thư mục lưu PDF
- Trạng thái trực tiếp, thanh tiến trình và nhật ký màu
- Sử dụng Microsoft Edge đã cài đặt trên máy
- Nhiều phương án dự phòng để trích xuất tài liệu và tạo PDF
- EXE Windows độc lập, không cần cài Python

## Sử dụng trực tiếp file EXE

1. Tải `StudocuHack.exe` từ GitHub Release mới nhất hoặc dùng [`dist/StudocuHack.exe`](dist/StudocuHack.exe).
2. Đảm bảo Microsoft Edge đã được cài đặt.
3. Lưu công việc và đóng tất cả cửa sổ Edge.
4. Chạy `StudocuHack.exe`.
5. Dán URL tài liệu Studocu được hỗ trợ.
6. Chọn thư mục lưu và nhấn **Bắt đầu tải PDF**.
7. Chờ xử lý hoàn tất rồi mở file PDF đã tạo.

EXE đã bao gồm Python, PyQt5 và môi trường chạy Playwright.

### Lưu ý trên Windows

- Ứng dụng hiện đóng các tiến trình Microsoft Edge đang chạy khi khởi động và thoát. Hãy lưu công việc trình duyệt trước.
- EXE chưa được ký số nên Windows SmartScreen hoặc phần mềm diệt virus có thể cảnh báo.
- Yêu cầu Windows 10/11 64-bit và Microsoft Edge.

## Chạy từ mã nguồn

### Yêu cầu

- Windows 10/11 64-bit
- Microsoft Edge
- Python 3.11

```powershell
git clone <url-kho-ma-nguon-cua-ban>
cd Studocu-Rehelper-main

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## Tạo file EXE

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

Script sẽ tạo `.venv`, cài các phụ thuộc cần thiết và tạo:

```text
dist\StudocuHack.exe
```

## Cấu trúc dự án

```text
studocuhack_desktop.py   Mã nguồn ứng dụng máy tính
requirements.txt         Các phụ thuộc Python
build_exe.ps1            Script đóng gói Windows
StudocuHack.spec         Cấu hình PyInstaller
img/icon128.ico          Biểu tượng ứng dụng
dist/StudocuHack.exe     Chương trình Windows đã đóng gói
```

## Khắc phục sự cố

- **Không tìm thấy Edge:** cài Microsoft Edge vào vị trí mặc định.
- **Tài liệu không tải:** mở tài liệu trong Edge trước và xác nhận có thể truy cập.
- **Windows chặn EXE:** chỉ sử dụng file từ kho mã nguồn này hoặc trang Release chính thức.
- **Lần chạy đầu chậm:** EXE một file cần giải nén môi trường tích hợp trước khi mở.

## Đóng góp

Hoan nghênh issue, bản dịch, cải thiện tài liệu và pull request.

## Giấy phép

Hãy thêm file giấy phép phù hợp trước khi công khai kho mã nguồn.
