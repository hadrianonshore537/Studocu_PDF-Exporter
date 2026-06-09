# Studocu PDF Exporter

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

Un outil de bureau Windows multilingue permettant d’exporter au format PDF les documents Studocu auxquels vous êtes autorisé à accéder. L’application propose une utilisation guidée, un dossier de sortie personnalisable, une progression en direct et des journaux colorés.

> **Usage éducatif uniquement :** ce projet est destiné exclusivement à l’apprentissage, à la recherche et à la référence technique. Il n’est ni affilié, ni approuvé, ni autorisé par Studocu. Ne l’utilisez pas pour contourner des paywalls, des contrôles d’accès ou des protections du droit d’auteur.

## Télécharger

- [Dernière version](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)
- [Téléchargement direct de StudocuHack.exe](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest/download/StudocuHack.exe)

L’EXE inclut Python, PyQt5 et l’environnement Playwright. Il n’est pas nécessaire d’installer Python.

## Fonctionnalités

- Parcours clair en trois étapes
- Sélecteur intégré prenant en charge 10 langues
- Taille de fenêtre adaptée automatiquement
- Dossier de sortie PDF personnalisable
- État en direct, barre de progression et journaux colorés
- Utilise Microsoft Edge installé localement
- Plusieurs stratégies alternatives de génération PDF
- EXE Windows autonome

## Utiliser l’EXE

1. Téléchargez `StudocuHack.exe` depuis la [dernière version](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest).
2. Vérifiez que Microsoft Edge est installé.
3. Enregistrez votre travail et fermez toutes les fenêtres Edge.
4. Lancez `StudocuHack.exe`.
5. Choisissez la langue de l’interface.
6. Collez l’URL d’un document Studocu auquel vous êtes autorisé à accéder.
7. Choisissez un dossier de sortie et démarrez le téléchargement PDF.
8. Ouvrez le PDF généré une fois le traitement terminé.

### Avis Windows

- L’application ferme actuellement les processus Edge lors de son démarrage et de sa fermeture.
- L’EXE n’est pas signé numériquement ; Windows SmartScreen ou l’antivirus peut afficher un avertissement.
- Téléchargez uniquement l’EXE depuis la page Releases officielle de ce dépôt.

## Exécuter depuis le code source

Prérequis : Windows 10/11 64 bits, Microsoft Edge et Python 3.11.

```powershell
git clone https://github.com/liqiheng777/Studocu_PDF-Exporter.git
cd Studocu_PDF-Exporter

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## Construire l’EXE

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

Le fichier généré se trouve dans `dist\StudocuHack.exe`.

## Utilisation légale et responsable

- Traitez uniquement les documents que vous avez créés, que vous possédez ou que vous êtes explicitement autorisé à exporter.
- Respectez le droit d’auteur, la vie privée, l’intégrité académique, les conditions de Studocu et les lois applicables.
- N’utilisez pas ce projet pour contourner des abonnements, paywalls, authentifications ou contrôles d’accès.
- Studocu est une marque de son propriétaire respectif. Ce projet indépendant n’a aucune relation officielle avec Studocu.

## Licence MIT

Copyright (c) 2026 QIHENG

L’autorisation est accordée gratuitement à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le « Logiciel »), d’utiliser le Logiciel sans restriction, notamment les droits d’utiliser, copier, modifier, fusionner, publier, distribuer, sous-licencier et/ou vendre des copies du Logiciel, ainsi que d’autoriser les personnes auxquelles le Logiciel est fourni à le faire, sous réserve des conditions suivantes :

La notice de copyright ci-dessus et la présente notice d’autorisation doivent être incluses dans toutes les copies ou parties substantielles du Logiciel.

LE LOGICIEL EST FOURNI « EN L’ÉTAT », SANS GARANTIE D’AUCUNE SORTE, EXPRESSE OU IMPLICITE, NOTAMMENT SANS GARANTIE DE QUALITÉ MARCHANDE, D’ADÉQUATION À UN USAGE PARTICULIER ET D’ABSENCE DE CONTREFAÇON. EN AUCUN CAS LES AUTEURS OU TITULAIRES DU COPYRIGHT NE POURRONT ÊTRE TENUS RESPONSABLES DE TOUTE RÉCLAMATION, DOMMAGE OU AUTRE RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D’UN CONTRAT, D’UN DÉLIT OU AUTREMENT, DÉCOULANT DU LOGICIEL, DE SON UTILISATION OU D’AUTRES OPÉRATIONS PORTANT SUR LE LOGICIEL.

Le texte officiel de la licence est le fichier anglais [LICENSE](LICENSE).
