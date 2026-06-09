# Studocu PDF Exporter

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

Erişim yetkiniz bulunan Studocu belgelerini PDF olarak dışa aktarmaya yönelik çok dilli bir Windows masaüstü aracıdır. Uygulama yönlendirmeli kullanım, seçilebilir çıktı klasörü, canlı ilerleme ve renkli günlükler sunar.

> **Yalnızca eğitim amaçlıdır:** Bu proje sadece öğrenme, araştırma ve teknik referans amacıyla hazırlanmıştır. Studocu ile bağlantılı değildir ve Studocu tarafından onaylanmamış veya yetkilendirilmemiştir. Ödeme duvarlarını, erişim kontrollerini veya telif hakkı korumalarını aşmak için kullanmayın.

## İndirme

- [En son sürüm](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)
- [StudocuHack.exe doğrudan indirme](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest/download/StudocuHack.exe)

EXE; Python, PyQt5 ve Playwright çalışma ortamını içerir. Python kurulumu gerekmez.

## Özellikler

- Açık ve anlaşılır üç adımlı kullanım
- 10 dili destekleyen yerleşik dil seçici
- Ekrana göre otomatik pencere boyutu
- Seçilebilir PDF çıktı klasörü
- Canlı durum, ilerleme çubuğu ve renkli günlükler
- Yerel olarak kurulu Microsoft Edge’i kullanır
- Birden fazla alternatif PDF oluşturma yöntemi
- Bağımsız Windows EXE

## EXE Kullanımı

1. `StudocuHack.exe` dosyasını [en son sürümden](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest) indirin.
2. Microsoft Edge’in kurulu olduğundan emin olun.
3. Tarayıcıdaki çalışmalarınızı kaydedin ve tüm Edge pencerelerini kapatın.
4. `StudocuHack.exe` dosyasını çalıştırın.
5. Arayüz dilini seçin.
6. Erişim yetkiniz bulunan bir Studocu belge URL’si yapıştırın.
7. Çıktı klasörünü seçin ve PDF indirmeyi başlatın.
8. İşlem tamamlandığında oluşturulan PDF’yi açın.

### Windows Uyarısı

- Uygulama şu anda başlatılırken ve kapatılırken çalışan Edge işlemlerini sonlandırır.
- EXE dijital olarak imzalanmamıştır; Windows SmartScreen veya antivirüs yazılımı uyarı gösterebilir.
- EXE’yi yalnızca bu deponun resmi Releases sayfasından indirin.

## Kaynak Koddan Çalıştırma

Gereksinimler: Windows 10/11 64 bit, Microsoft Edge ve Python 3.11.

```powershell
git clone https://github.com/liqiheng777/Studocu_PDF-Exporter.git
cd Studocu_PDF-Exporter

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## EXE Oluşturma

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

Oluşturulan dosya `dist\StudocuHack.exe` konumundadır.

## Yasal ve Sorumlu Kullanım

- Yalnızca oluşturduğunuz, sahibi olduğunuz veya dışa aktarma izniniz bulunan belgeleri işleyin.
- Telif hakkı, gizlilik, akademik dürüstlük, Studocu hizmet şartları ve geçerli yasalara uyun.
- Projeyi abonelikleri, ödeme duvarlarını, kimlik doğrulamayı veya erişim kontrollerini aşmak için kullanmayın.
- Studocu ilgili sahibinin ticari markasıdır. Bu bağımsız projenin Studocu ile resmi bir ilişkisi yoktur.

## MIT Lisansı

Copyright (c) 2026 QIHENG

Bu yazılımın ve ilgili belge dosyalarının (“Yazılım”) bir kopyasını edinen herhangi bir kişiye, Yazılımı herhangi bir kısıtlama olmaksızın kullanma, kopyalama, değiştirme, birleştirme, yayımlama, dağıtma, alt lisanslama ve/veya satma hakları dahil ancak bunlarla sınırlı olmamak üzere Yazılım üzerinde işlem yapma ve Yazılımın sağlandığı kişilere de bunu yapma izni, aşağıdaki koşullara tabi olmak üzere ücretsiz olarak verilir:

Yukarıdaki telif hakkı bildirimi ve bu izin bildirimi, Yazılımın tüm kopyalarına veya önemli bölümlerine dahil edilmelidir.

YAZILIM, TİCARETE ELVERİŞLİLİK, BELİRLİ BİR AMACA UYGUNLUK VE İHLAL ETMEME GARANTİLERİ DAHİL ANCAK BUNLARLA SINIRLI OLMAMAK ÜZERE, AÇIK VEYA ZIMNİ HİÇBİR GARANTİ OLMAKSIZIN “OLDUĞU GİBİ” SAĞLANIR. YAZARLAR VEYA TELİF HAKKI SAHİPLERİ, SÖZLEŞME, HAKSIZ FİİL VEYA BAŞKA BİR NEDENDEN KAYNAKLANAN; YAZILIMDAN, YAZILIMIN KULLANIMINDAN VEYA YAZILIMLA İLGİLİ DİĞER İŞLEMLERDEN DOĞAN HERHANGİ BİR TALEP, ZARAR VEYA DİĞER SORUMLULUKTAN HİÇBİR DURUMDA SORUMLU TUTULAMAZ.

Resmî lisans metni İngilizce [LICENSE](LICENSE) dosyasıdır.
