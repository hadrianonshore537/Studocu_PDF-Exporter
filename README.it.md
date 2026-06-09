# Studocu PDF Exporter

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

Uno strumento desktop Windows multilingue per esportare in PDF i documenti Studocu ai quali sei autorizzato ad accedere. L’applicazione offre una procedura guidata, una cartella di output selezionabile, avanzamento in tempo reale e log colorati.

> **Solo per finalità educative:** questo progetto è destinato esclusivamente allo studio, alla ricerca e alla consultazione tecnica. Non è affiliato, approvato o autorizzato da Studocu. Non utilizzarlo per aggirare paywall, controlli di accesso o protezioni del diritto d’autore.

## Download

- [Ultima release](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)
- [Download diretto di StudocuHack.exe](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest/download/StudocuHack.exe)

L’EXE include Python, PyQt5 e il runtime Playwright. Non è necessario installare Python.

## Funzionalità

- Procedura chiara in tre passaggi
- Selettore integrato con supporto per 10 lingue
- Dimensione della finestra adattata automaticamente
- Cartella di output PDF selezionabile
- Stato, avanzamento e log colorati in tempo reale
- Utilizza Microsoft Edge installato localmente
- Più strategie alternative di generazione PDF
- EXE Windows autonomo

## Utilizzare l’EXE

1. Scarica `StudocuHack.exe` dall’[ultima release](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest).
2. Assicurati che Microsoft Edge sia installato.
3. Salva il lavoro nel browser e chiudi tutte le finestre Edge.
4. Avvia `StudocuHack.exe`.
5. Seleziona la lingua dell’interfaccia.
6. Incolla l’URL di un documento Studocu che sei autorizzato a consultare.
7. Scegli una cartella di output e avvia il download PDF.
8. Al termine, apri il PDF generato.

### Avviso Windows

- Attualmente l’applicazione chiude i processi Edge in esecuzione all’avvio e all’uscita.
- L’EXE non è firmato digitalmente; Windows SmartScreen o l’antivirus potrebbero mostrare un avviso.
- Scarica l’EXE solo dalla pagina Releases ufficiale di questo repository.

## Eseguire dal codice sorgente

Requisiti: Windows 10/11 a 64 bit, Microsoft Edge e Python 3.11.

```powershell
git clone https://github.com/liqiheng777/Studocu_PDF-Exporter.git
cd Studocu_PDF-Exporter

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## Creare l’EXE

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

Il file generato si trova in `dist\StudocuHack.exe`.

## Uso legale e responsabile

- Elabora soltanto documenti creati da te, di tua proprietà o per i quali hai un’esplicita autorizzazione all’esportazione.
- Rispetta diritto d’autore, privacy, integrità accademica, termini di Studocu e leggi applicabili.
- Non utilizzare il progetto per aggirare abbonamenti, paywall, autenticazioni o controlli di accesso.
- Studocu è un marchio del rispettivo proprietario. Questo progetto indipendente non ha alcun rapporto ufficiale con Studocu.

## Licenza MIT

Copyright (c) 2026 QIHENG

È concessa gratuitamente a chiunque ottenga una copia di questo software e dei relativi file di documentazione (il “Software”) l’autorizzazione a utilizzare il Software senza restrizioni, inclusi, senza limitazione, i diritti di usare, copiare, modificare, unire, pubblicare, distribuire, concedere in sublicenza e/o vendere copie del Software, nonché di consentire alle persone a cui il Software viene fornito di fare altrettanto, alle seguenti condizioni:

L’avviso di copyright sopra riportato e il presente avviso di autorizzazione devono essere inclusi in tutte le copie o parti sostanziali del Software.

IL SOFTWARE VIENE FORNITO “COSÌ COM’È”, SENZA GARANZIE DI ALCUN TIPO, ESPLICITE O IMPLICITE, INCLUSE, A TITOLO ESEMPLIFICATIVO, LE GARANZIE DI COMMERCIABILITÀ, IDONEITÀ A UNO SCOPO PARTICOLARE E NON VIOLAZIONE. IN NESSUN CASO GLI AUTORI O I TITOLARI DEL COPYRIGHT SARANNO RESPONSABILI PER RECLAMI, DANNI O ALTRE RESPONSABILITÀ, SIA IN UN’AZIONE CONTRATTUALE, ILLECITA O DI ALTRO TIPO, DERIVANTI DAL SOFTWARE, DAL SUO UTILIZZO O DA ALTRE OPERAZIONI RELATIVE AL SOFTWARE.

Il testo ufficiale della licenza è il file inglese [LICENSE](LICENSE).
