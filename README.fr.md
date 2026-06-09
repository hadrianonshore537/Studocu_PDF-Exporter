# StudocuHack

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

StudocuHack est une application de bureau Windows qui traite les pages de documents Studocu prises en charge et les enregistre au format PDF. Elle propose une interface claire, un dossier de sortie personnalisable, une progression en direct, des journaux colorés et plusieurs méthodes de secours automatiques.

> Utilisez ce projet uniquement pour les documents auxquels vous êtes autorisé à accéder. Respectez les droits d’auteur, les conditions de la plateforme et les lois applicables.

## Fonctionnalités

- Interface claire avec guide étape par étape
- Sélecteur de langue intégré prenant en charge 10 langues
- Taille de fenêtre adaptée automatiquement à l’écran
- Dossier de sortie PDF personnalisable
- État en direct, barre de progression et journaux colorés
- Utilise Microsoft Edge installé localement
- Plusieurs méthodes de secours pour l’extraction et la génération PDF
- EXE Windows autonome ne nécessitant pas Python

## Utiliser directement l’EXE

1. Téléchargez `StudocuHack.exe` depuis la dernière GitHub Release ou utilisez [`dist/StudocuHack.exe`](dist/StudocuHack.exe).
2. Vérifiez que Microsoft Edge est installé.
3. Enregistrez votre travail et fermez toutes les fenêtres Edge.
4. Lancez `StudocuHack.exe`.
5. Collez une URL de document Studocu prise en charge.
6. Choisissez le dossier de sortie et cliquez sur **Télécharger le PDF**.
7. Attendez la fin du traitement, puis ouvrez le PDF généré.

L’EXE inclut déjà Python, PyQt5 et l’environnement Playwright.

### Avertissements Windows

- L’application ferme actuellement les processus Microsoft Edge au démarrage et à la fermeture. Enregistrez d’abord votre travail.
- L’EXE n’est pas signé numériquement. Windows SmartScreen ou l’antivirus peut afficher un avertissement.
- Windows 10/11 64 bits et Microsoft Edge sont requis.

## Exécuter depuis le code source

### Prérequis

- Windows 10/11 64 bits
- Microsoft Edge
- Python 3.11

```powershell
git clone <url-de-votre-depot>
cd Studocu-Rehelper-main

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## Construire l’EXE

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

Le script crée `.venv`, installe les dépendances nécessaires et génère :

```text
dist\StudocuHack.exe
```

## Structure du projet

```text
studocuhack_desktop.py   Code source de l’application
requirements.txt         Dépendances Python
build_exe.ps1            Script de construction Windows
StudocuHack.spec         Configuration PyInstaller
img/icon128.ico          Icône de l’application
dist/StudocuHack.exe     Exécutable Windows précompilé
```

## Dépannage

- **Edge est introuvable :** installez Microsoft Edge dans son emplacement par défaut.
- **Le document ne charge pas :** ouvrez-le d’abord dans Edge et vérifiez son accessibilité.
- **Windows bloque l’EXE :** utilisez uniquement l’EXE provenant de ce dépôt ou de la page Release officielle.
- **Le premier lancement est lent :** l’EXE monofichier extrait d’abord son environnement.

## Contribution

Les issues, traductions, améliorations de documentation et pull requests sont les bienvenues.

## Licence

Ajoutez un fichier de licence adapté avant de publier le dépôt.
