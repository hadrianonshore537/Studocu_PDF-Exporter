# Studocu PDF Exporter

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

Ein mehrsprachiges Windows-Desktop-Tool zum Exportieren von Studocu-Dokumenten, für die Sie eine Zugriffsberechtigung besitzen, als PDF. Die Anwendung bietet eine geführte Bedienung, einen wählbaren Ausgabeordner, Live-Fortschritt und farbige Protokolle.

> **Nur für Bildung und Forschung:** Dieses Projekt dient ausschließlich dem Lernen, der Forschung und als technische Referenz. Es steht in keiner Verbindung zu Studocu und wird von Studocu weder unterstützt noch autorisiert. Es darf nicht zur Umgehung von Bezahlschranken, Zugriffskontrollen oder Urheberrechtsschutz verwendet werden.

## Download

- [Neueste Release-Version](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)
- [StudocuHack.exe direkt herunterladen](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest/download/StudocuHack.exe)

Die EXE enthält Python, PyQt5 und die Playwright-Laufzeit. Eine separate Python-Installation ist nicht erforderlich.

## Funktionen

- Übersichtlicher Ablauf in drei Schritten
- Integrierter Sprachumschalter mit 10 Sprachen
- Automatisch angepasste Fenstergröße
- Frei wählbarer PDF-Ausgabeordner
- Live-Status, Fortschrittsanzeige und farbige Protokolle
- Verwendet den lokal installierten Microsoft Edge
- Mehrere alternative PDF-Erstellungsstrategien
- Eigenständige Windows-EXE

## EXE verwenden

1. Laden Sie `StudocuHack.exe` aus der [neuesten Release-Version](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest) herunter.
2. Stellen Sie sicher, dass Microsoft Edge installiert ist.
3. Speichern Sie Ihre Browserarbeit und schließen Sie alle Edge-Fenster.
4. Starten Sie `StudocuHack.exe`.
5. Wählen Sie die gewünschte Sprache.
6. Fügen Sie eine Studocu-Dokument-URL ein, auf die Sie zugreifen dürfen.
7. Wählen Sie einen Ausgabeordner und starten Sie den PDF-Download.
8. Öffnen Sie nach Abschluss die erzeugte PDF-Datei.

### Windows-Hinweis

- Die Anwendung beendet derzeit laufende Edge-Prozesse beim Starten und Beenden.
- Die EXE ist nicht digital signiert; Windows SmartScreen oder Antivirensoftware kann eine Warnung anzeigen.
- Laden Sie die EXE nur von der offiziellen Releases-Seite dieses Repositorys herunter.

## Aus dem Quellcode starten

Voraussetzungen: Windows 10/11 64-Bit, Microsoft Edge und Python 3.11.

```powershell
git clone https://github.com/liqiheng777/Studocu_PDF-Exporter.git
cd Studocu_PDF-Exporter

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## EXE erstellen

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

Die fertige Datei befindet sich unter `dist\StudocuHack.exe`.

## Rechtmäßige und verantwortungsvolle Nutzung

- Verarbeiten Sie nur Dokumente, die Sie erstellt haben, besitzen oder ausdrücklich exportieren dürfen.
- Beachten Sie Urheberrecht, Datenschutz, akademische Integrität, die Studocu-Nutzungsbedingungen und geltendes Recht.
- Verwenden Sie dieses Projekt nicht zur Umgehung von Abonnements, Bezahlschranken, Authentifizierung oder Zugriffskontrollen.
- Studocu ist eine Marke des jeweiligen Rechteinhabers. Dieses unabhängige Projekt hat keine offizielle Verbindung zu Studocu.

## MIT-Lizenz

Copyright (c) 2026 QIHENG

Hiermit wird jeder Person, die eine Kopie dieser Software und der zugehörigen Dokumentationsdateien (die „Software“) erhält, unentgeltlich die Erlaubnis erteilt, uneingeschränkt mit der Software zu handeln. Dies schließt insbesondere das Recht ein, die Software zu verwenden, zu kopieren, zu verändern, zusammenzuführen, zu veröffentlichen, zu verbreiten, unterzulizenzieren und/oder Kopien der Software zu verkaufen sowie Personen, denen die Software zur Verfügung gestellt wird, dies unter den folgenden Bedingungen zu gestatten:

Der obige Urheberrechtsvermerk und dieser Erlaubnisvermerk müssen in allen Kopien oder wesentlichen Teilen der Software enthalten sein.

DIE SOFTWARE WIRD OHNE JEGLICHE AUSDRÜCKLICHE ODER STILLSCHWEIGENDE GEWÄHRLEISTUNG „WIE BESEHEN“ BEREITGESTELLT, EINSCHLIESSLICH, ABER NICHT BESCHRÄNKT AUF DIE GEWÄHRLEISTUNG DER MARKTGÄNGIGKEIT, EIGNUNG FÜR EINEN BESTIMMTEN ZWECK UND NICHTVERLETZUNG. IN KEINEM FALL HAFTEN DIE AUTOREN ODER URHEBERRECHTSINHABER FÜR ANSPRÜCHE, SCHÄDEN ODER SONSTIGE HAFTUNG, SEI ES AUS VERTRAG, UNERLAUBTER HANDLUNG ODER ANDERWEITIG, DIE AUS DER SOFTWARE, IHRER NUTZUNG ODER ANDEREN GESCHÄFTEN MIT DER SOFTWARE ENTSTEHEN.

Maßgeblich ist der englische Lizenztext in der Datei [LICENSE](LICENSE).
