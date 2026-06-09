# Studocu PDF Exporter

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

Công cụ máy tính Windows đa ngôn ngữ dùng để xuất sang PDF các tài liệu Studocu mà bạn được phép truy cập. Ứng dụng cung cấp hướng dẫn sử dụng, lựa chọn thư mục lưu, tiến trình trực tiếp và nhật ký màu.

> **Chỉ dành cho giáo dục và nghiên cứu:** dự án này chỉ nhằm mục đích học tập, nghiên cứu và tham khảo kỹ thuật. Dự án không liên kết, không được xác nhận hoặc ủy quyền bởi Studocu. Không sử dụng để vượt tường phí, kiểm soát truy cập hoặc bảo vệ bản quyền.

## Tải xuống

- [Bản phát hành mới nhất](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)
- [Tải trực tiếp StudocuHack.exe](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest/download/StudocuHack.exe)

EXE đã bao gồm Python, PyQt5 và môi trường Playwright. Bạn không cần cài đặt Python.

## Tính năng

- Quy trình sử dụng rõ ràng trong ba bước
- Bộ chọn ngôn ngữ tích hợp hỗ trợ 10 ngôn ngữ
- Tự động điều chỉnh kích thước cửa sổ
- Có thể chọn thư mục lưu PDF
- Trạng thái trực tiếp, thanh tiến trình và nhật ký màu
- Sử dụng Microsoft Edge được cài đặt trên máy
- Nhiều phương án tạo PDF dự phòng
- EXE Windows độc lập

## Sử dụng EXE

1. Tải `StudocuHack.exe` từ [bản phát hành mới nhất](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest).
2. Đảm bảo Microsoft Edge đã được cài đặt.
3. Lưu công việc trong trình duyệt và đóng tất cả cửa sổ Edge.
4. Chạy `StudocuHack.exe`.
5. Chọn ngôn ngữ giao diện.
6. Dán URL tài liệu Studocu mà bạn được phép truy cập.
7. Chọn thư mục lưu và bắt đầu tải PDF.
8. Mở PDF đã tạo sau khi xử lý hoàn tất.

### Lưu ý cho Windows

- Hiện tại ứng dụng sẽ đóng các tiến trình Edge khi khởi động và thoát.
- EXE chưa được ký số; Windows SmartScreen hoặc phần mềm diệt virus có thể hiển thị cảnh báo.
- Chỉ tải EXE từ trang Releases chính thức của kho lưu trữ này.

## Chạy từ mã nguồn

Yêu cầu: Windows 10/11 64-bit, Microsoft Edge và Python 3.11.

```powershell
git clone https://github.com/liqiheng777/Studocu_PDF-Exporter.git
cd Studocu_PDF-Exporter

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## Tạo EXE

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

Tệp được tạo nằm tại `dist\StudocuHack.exe`.

## Sử dụng hợp pháp và có trách nhiệm

- Chỉ xử lý tài liệu do bạn tạo, sở hữu hoặc được cho phép rõ ràng để xuất.
- Tuân thủ bản quyền, quyền riêng tư, tính trung thực học thuật, điều khoản của Studocu và pháp luật hiện hành.
- Không sử dụng dự án để vượt đăng ký, tường phí, xác thực hoặc kiểm soát truy cập.
- Studocu là nhãn hiệu của chủ sở hữu tương ứng. Dự án độc lập này không có quan hệ chính thức với Studocu.

## Giấy phép MIT

Copyright (c) 2026 QIHENG

Theo đây, mọi cá nhân nhận được bản sao của phần mềm này và các tệp tài liệu liên quan (“Phần mềm”) được cấp quyền miễn phí để sử dụng Phần mềm mà không bị hạn chế, bao gồm nhưng không giới hạn ở quyền sử dụng, sao chép, sửa đổi, hợp nhất, xuất bản, phân phối, cấp phép lại và/hoặc bán các bản sao của Phần mềm, đồng thời cho phép những người được cung cấp Phần mềm thực hiện các quyền đó, với các điều kiện sau:

Thông báo bản quyền nêu trên và thông báo cấp phép này phải được đưa vào tất cả các bản sao hoặc phần quan trọng của Phần mềm.

PHẦN MỀM ĐƯỢC CUNG CẤP “NGUYÊN TRẠNG”, KHÔNG KÈM BẤT KỲ BẢO ĐẢM NÀO, DÙ RÕ RÀNG HAY NGỤ Ý, BAO GỒM NHƯNG KHÔNG GIỚI HẠN Ở CÁC BẢO ĐẢM VỀ KHẢ NĂNG THƯƠNG MẠI, SỰ PHÙ HỢP CHO MỘT MỤC ĐÍCH CỤ THỂ VÀ KHÔNG VI PHẠM. TRONG MỌI TRƯỜNG HỢP, TÁC GIẢ HOẶC CHỦ SỞ HỮU BẢN QUYỀN KHÔNG CHỊU TRÁCH NHIỆM ĐỐI VỚI BẤT KỲ KHIẾU NẠI, THIỆT HẠI HOẶC TRÁCH NHIỆM NÀO KHÁC, DÙ PHÁT SINH TỪ HỢP ĐỒNG, HÀNH VI DÂN SỰ HAY NGUYÊN NHÂN KHÁC, LIÊN QUAN ĐẾN PHẦN MỀM, VIỆC SỬ DỤNG PHẦN MỀM HOẶC CÁC GIAO DỊCH KHÁC VỚI PHẦN MỀM.

Văn bản giấy phép chính thức là tệp [LICENSE](LICENSE) bằng tiếng Anh.
