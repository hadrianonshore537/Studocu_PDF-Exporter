# StudocuHack

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

StudocuHack è un’applicazione desktop per Windows che elabora le pagine dei documenti Studocu supportati e le salva come PDF. Offre un’interfaccia chiara, una cartella di output selezionabile, avanzamento in tempo reale, log colorati e strategie di riserva automatiche.

> Usa questo progetto solo per documenti a cui sei autorizzato ad accedere. Rispetta il copyright, i termini della piattaforma e le leggi applicabili.

## Funzionalità

- Interfaccia desktop chiara con guida passo passo
- Selettore della lingua integrato con supporto per 10 lingue
- Dimensione della finestra adattata automaticamente allo schermo
- Cartella di output PDF selezionabile
- Stato in tempo reale, barra di avanzamento e log colorati
- Utilizza Microsoft Edge installato localmente
- Più strategie di riserva per estrazione e generazione PDF
- EXE Windows autonoma senza necessità di installare Python

## Usare direttamente l’EXE

1. Scarica `StudocuHack.exe` dall’ultima GitHub Release oppure usa [`dist/StudocuHack.exe`](dist/StudocuHack.exe).
2. Assicurati che Microsoft Edge sia installato.
3. Salva il tuo lavoro e chiudi tutte le finestre Edge.
4. Avvia `StudocuHack.exe`.
5. Incolla un URL Studocu supportato.
6. Seleziona la cartella di output e fai clic su **Scarica PDF**.
7. Attendi il completamento e apri il PDF generato.

L’EXE include già Python, PyQt5 e il runtime Playwright.

### Avvisi per Windows

- L’applicazione chiude attualmente i processi Microsoft Edge all’avvio e alla chiusura. Salva prima il lavoro nel browser.
- L’EXE non è firmata digitalmente; Windows SmartScreen o l’antivirus potrebbero mostrare un avviso.
- Sono richiesti Windows 10/11 a 64 bit e Microsoft Edge.

## Avviare dal codice sorgente

### Requisiti

- Windows 10/11 a 64 bit
- Microsoft Edge
- Python 3.11

```powershell
git clone <url-del-tuo-repository>
cd Studocu-Rehelper-main

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## Creare l’EXE

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

Lo script crea `.venv`, installa le dipendenze necessarie e genera:

```text
dist\StudocuHack.exe
```

## Struttura del progetto

```text
studocuhack_desktop.py   Codice sorgente dell’applicazione
requirements.txt         Dipendenze Python
build_exe.ps1            Script di build Windows
StudocuHack.spec         Configurazione PyInstaller
img/icon128.ico          Icona dell’applicazione
dist/StudocuHack.exe     Eseguibile Windows precompilato
```

## Risoluzione dei problemi

- **Edge non viene trovato:** installa Microsoft Edge nel percorso predefinito.
- **Il documento non si carica:** aprilo prima in Edge e verifica l’accesso.
- **Windows blocca l’EXE:** usa solo file provenienti da questo repository o dalla pagina Release ufficiale.
- **Il primo avvio è lento:** l’EXE a file singolo deve prima estrarre il runtime.

## Contribuire

Issue, traduzioni, miglioramenti alla documentazione e pull request sono benvenuti.

## Licenza

Aggiungi un file di licenza adatto prima di pubblicare il repository.
