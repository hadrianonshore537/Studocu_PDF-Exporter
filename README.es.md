# StudocuHack

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

StudocuHack es una aplicación de escritorio para Windows que procesa páginas de documentos Studocu compatibles y las guarda como PDF. Ofrece una interfaz clara, carpeta de salida seleccionable, progreso en directo, registros con colores y estrategias de respaldo automáticas.

> Usa este proyecto únicamente con documentos a los que tengas autorización de acceso. Respeta los derechos de autor, las condiciones de la plataforma y la legislación aplicable.

## Funciones

- Interfaz clara con guía paso a paso
- Selector de idioma integrado compatible con 10 idiomas
- Tamaño de ventana adaptado automáticamente a la pantalla
- Carpeta de salida PDF seleccionable
- Estado en directo, barra de progreso y registros con colores
- Utiliza Microsoft Edge instalado localmente
- Varias estrategias de respaldo para extracción y creación de PDF
- EXE independiente para Windows que no requiere instalar Python

## Usar directamente el EXE

1. Descarga `StudocuHack.exe` desde la última GitHub Release o utiliza [`dist/StudocuHack.exe`](dist/StudocuHack.exe).
2. Comprueba que Microsoft Edge esté instalado.
3. Guarda tu trabajo y cierra todas las ventanas de Edge.
4. Ejecuta `StudocuHack.exe`.
5. Pega una URL compatible de un documento Studocu.
6. Selecciona la carpeta de salida y pulsa **Descargar PDF**.
7. Espera a que finalice el proceso y abre el PDF generado.

El EXE ya incluye Python, PyQt5 y el entorno de ejecución de Playwright.

### Avisos para Windows

- La aplicación cierra actualmente los procesos de Microsoft Edge al iniciarse y cerrarse. Guarda primero tu trabajo del navegador.
- El EXE no está firmado digitalmente, por lo que Windows SmartScreen o el antivirus pueden mostrar una advertencia.
- Se requiere Windows 10/11 de 64 bits y Microsoft Edge.

## Ejecutar desde el código fuente

### Requisitos

- Windows 10/11 de 64 bits
- Microsoft Edge
- Python 3.11

```powershell
git clone <url-de-tu-repositorio>
cd Studocu-Rehelper-main

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## Crear el EXE

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

El script crea `.venv`, instala las dependencias necesarias y genera:

```text
dist\StudocuHack.exe
```

## Estructura del proyecto

```text
studocuhack_desktop.py   Código fuente de la aplicación
requirements.txt         Dependencias de Python
build_exe.ps1            Script de compilación para Windows
StudocuHack.spec         Configuración de PyInstaller
img/icon128.ico          Icono de la aplicación
dist/StudocuHack.exe     Ejecutable precompilado para Windows
```

## Solución de problemas

- **No se encuentra Edge:** instala Microsoft Edge en su ubicación predeterminada.
- **El documento no carga:** ábrelo primero en Edge y verifica que sea accesible.
- **Windows bloquea el EXE:** usa únicamente archivos de este repositorio o de la página Release oficial.
- **El primer inicio es lento:** el EXE de un solo archivo extrae primero su entorno interno.

## Contribuir

Se aceptan issues, traducciones, mejoras de documentación y pull requests.

## Licencia

Añade un archivo de licencia adecuado antes de publicar el repositorio.
