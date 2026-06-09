# StudocuHack

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

StudocuHack, desteklenen Studocu belge sayfalarını işleyip PDF olarak kaydeden bir Windows masaüstü uygulamasıdır. Anlaşılır bir arayüz, seçilebilir çıktı klasörü, canlı ilerleme, renkli günlükler ve otomatik yedek yöntemler sunar.

> Bu projeyi yalnızca erişim izniniz olan belgeler için kullanın. Telif haklarına, platform koşullarına ve geçerli yasalara uyun.

## Özellikler

- Adım adım yönlendirmeli anlaşılır masaüstü arayüzü
- 10 dili destekleyen yerleşik arayüz dili seçici
- Büyük ve küçük ekranlara göre otomatik pencere boyutu
- Seçilebilir PDF çıktı klasörü
- Canlı durum, ilerleme çubuğu ve renkli işlem günlükleri
- Bilgisayarda kurulu Microsoft Edge tarayıcısını kullanır
- Birden fazla belge çıkarma ve PDF oluşturma yedek yöntemi
- Python kurulumu gerektirmeyen bağımsız Windows EXE

## EXE Dosyasını Doğrudan Kullanma

1. En son GitHub Release sayfasından `StudocuHack.exe` dosyasını indirin veya [`dist/StudocuHack.exe`](dist/StudocuHack.exe) dosyasını kullanın.
2. Microsoft Edge’in kurulu olduğundan emin olun.
3. Çalışmalarınızı kaydedin ve tüm Edge pencerelerini kapatın.
4. `StudocuHack.exe` dosyasını çalıştırın.
5. Desteklenen bir Studocu belge bağlantısını yapıştırın.
6. Çıktı klasörünü seçin ve **PDF İndir** düğmesine tıklayın.
7. İşlemin bitmesini bekleyin ve oluşturulan PDF’yi açın.

EXE; Python, PyQt5 ve Playwright çalışma ortamını içerir.

### Windows Uyarıları

- Uygulama şu anda başlatılırken ve kapatılırken çalışan Microsoft Edge işlemlerini kapatır. Önce tarayıcı çalışmalarınızı kaydedin.
- EXE dijital olarak imzalanmamıştır; Windows SmartScreen veya antivirüs uyarı gösterebilir.
- Windows 10/11 64 bit ve Microsoft Edge gereklidir.

## Kaynak Koddan Çalıştırma

### Gereksinimler

- Windows 10/11 64 bit
- Microsoft Edge
- Python 3.11

```powershell
git clone <depo-adresiniz>
cd Studocu-Rehelper-main

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## EXE Oluşturma

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

Betik `.venv` ortamını oluşturur, gerekli bağımlılıkları yükler ve şunu üretir:

```text
dist\StudocuHack.exe
```

## Proje Yapısı

```text
studocuhack_desktop.py   Masaüstü uygulaması kaynak kodu
requirements.txt         Python bağımlılıkları
build_exe.ps1            Windows derleme betiği
StudocuHack.spec         PyInstaller yapılandırması
img/icon128.ico          Uygulama simgesi
dist/StudocuHack.exe     Önceden derlenmiş Windows uygulaması
```

## Sorun Giderme

- **Edge bulunamıyor:** Microsoft Edge’i varsayılan konumuna kurun.
- **Belge yüklenmiyor:** Önce Edge’de açıp erişilebilir olduğunu doğrulayın.
- **Windows EXE’yi engelliyor:** Yalnızca bu depodan veya resmi Release sayfasından indirilen dosyaları kullanın.
- **İlk açılış yavaş:** Tek dosyalı EXE önce dahili çalışma ortamını çıkarır.

## Katkıda Bulunma

Issue, çeviri, belge iyileştirmesi ve pull request katkıları memnuniyetle karşılanır.

## Lisans

Depoyu yayımlamadan önce uygun bir lisans dosyası ekleyin.
