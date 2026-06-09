# StudocuHack

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

StudocuHack ist eine Windows-Desktopanwendung, die unterstützte Studocu-Dokumentseiten verarbeitet und als PDF speichert. Sie bietet eine übersichtliche Benutzeroberfläche, einen frei wählbaren Ausgabeordner, Live-Fortschritt, farbige Protokolle und automatische Ausweichverfahren.

> Verwende dieses Projekt nur für Dokumente, auf die du zugreifen darfst. Beachte Urheberrecht, Plattformbedingungen und geltende Gesetze.

## Funktionen

- Übersichtliche Desktop-Oberfläche mit Schritt-für-Schritt-Anleitung
- Integrierter Sprachumschalter mit Unterstützung für 10 Sprachen
- Automatische Fenstergröße für große und kleine Bildschirme
- Frei wählbarer PDF-Ausgabeordner
- Live-Status, Fortschrittsanzeige und farbige Protokolle
- Verwendet den lokal installierten Microsoft Edge
- Mehrere Ausweichverfahren für Extraktion und PDF-Erstellung
- Eigenständige Windows-EXE ohne notwendige Python-Installation

## EXE direkt verwenden

1. Lade `StudocuHack.exe` aus dem neuesten GitHub Release herunter oder verwende [`dist/StudocuHack.exe`](dist/StudocuHack.exe).
2. Stelle sicher, dass Microsoft Edge installiert ist.
3. Speichere deine Arbeit und schließe alle Edge-Fenster.
4. Starte `StudocuHack.exe`.
5. Füge eine unterstützte Studocu-Dokument-URL ein.
6. Wähle einen Ausgabeordner und klicke auf **PDF herunterladen**.
7. Warte bis zum Abschluss und öffne anschließend die erzeugte PDF.

Die EXE enthält bereits Python, PyQt5 und die Playwright-Laufzeit.

### Windows-Hinweise

- Die Anwendung beendet derzeit laufende Microsoft-Edge-Prozesse beim Starten und Beenden. Speichere vorher deine Browserarbeit.
- Die EXE ist nicht digital signiert. Windows SmartScreen oder Antivirensoftware kann eine Warnung anzeigen.
- Benötigt werden Windows 10/11 64-Bit und Microsoft Edge.

## Aus dem Quellcode starten

### Voraussetzungen

- Windows 10/11 64-Bit
- Microsoft Edge
- Python 3.11

```powershell
git clone <deine-repository-url>
cd Studocu-Rehelper-main

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## EXE erstellen

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

Das Skript erstellt bei Bedarf `.venv`, installiert Abhängigkeiten und erzeugt:

```text
dist\StudocuHack.exe
```

## Projektstruktur

```text
studocuhack_desktop.py   Quellcode der Desktopanwendung
requirements.txt         Python-Abhängigkeiten
build_exe.ps1            Windows-Buildskript
StudocuHack.spec         PyInstaller-Konfiguration
img/icon128.ico          Anwendungssymbol
dist/StudocuHack.exe     Vorgefertigte Windows-Anwendung
```

## Fehlerbehebung

- **Edge wird nicht gefunden:** Installiere Microsoft Edge im Standardverzeichnis.
- **Dokument lädt nicht:** Öffne es zuerst in Edge und prüfe den Zugriff.
- **Windows blockiert die EXE:** Verwende nur Dateien aus diesem Repository oder der offiziellen Release-Seite.
- **Erster Start dauert länger:** Die Ein-Datei-EXE entpackt zunächst ihre Laufzeit.

## Mitwirken

Issues, Übersetzungen, Dokumentationsverbesserungen und Pull Requests sind willkommen.

## Lizenz

Füge vor der Veröffentlichung eine passende Lizenzdatei hinzu.
