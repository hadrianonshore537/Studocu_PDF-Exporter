# Studocu PDF Exporter

[English](README.md) | [简体中文](README.zh-CN.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Tiếng Việt](README.vi.md)

Una herramienta de escritorio multilingüe para Windows que permite exportar como PDF documentos de Studocu a los que estés autorizado a acceder. La aplicación ofrece instrucciones guiadas, carpeta de salida seleccionable, progreso en directo y registros con colores.

> **Solo para fines educativos:** este proyecto está destinado exclusivamente al aprendizaje, la investigación y la referencia técnica. No está afiliado, respaldado ni autorizado por Studocu. No lo utilices para eludir muros de pago, controles de acceso o protecciones de derechos de autor.

## Descargar

- [Última versión](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest)
- [Descarga directa de StudocuHack.exe](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest/download/StudocuHack.exe)

El EXE incluye Python, PyQt5 y el entorno de ejecución Playwright. No es necesario instalar Python.

## Funciones

- Flujo de trabajo claro en tres pasos
- Selector integrado compatible con 10 idiomas
- Tamaño de ventana adaptado automáticamente
- Carpeta de salida PDF seleccionable
- Estado en directo, barra de progreso y registros con colores
- Utiliza Microsoft Edge instalado localmente
- Varias estrategias alternativas de generación de PDF
- EXE independiente para Windows

## Usar el EXE

1. Descarga `StudocuHack.exe` desde la [última versión](https://github.com/liqiheng777/Studocu_PDF-Exporter/releases/latest).
2. Asegúrate de que Microsoft Edge esté instalado.
3. Guarda tu trabajo y cierra todas las ventanas de Edge.
4. Ejecuta `StudocuHack.exe`.
5. Selecciona el idioma de la interfaz.
6. Pega la URL de un documento de Studocu al que estés autorizado a acceder.
7. Selecciona una carpeta de salida e inicia la descarga del PDF.
8. Cuando finalice el proceso, abre el PDF generado.

### Aviso para Windows

- Actualmente, la aplicación cierra los procesos de Edge al iniciarse y salir.
- El EXE no está firmado digitalmente; Windows SmartScreen o el antivirus pueden mostrar una advertencia.
- Descarga el EXE únicamente desde la página Releases oficial de este repositorio.

## Ejecutar desde el código fuente

Requisitos: Windows 10/11 de 64 bits, Microsoft Edge y Python 3.11.

```powershell
git clone https://github.com/liqiheng777/Studocu_PDF-Exporter.git
cd Studocu_PDF-Exporter

py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\studocuhack_desktop.py
```

## Crear el EXE

```powershell
powershell -ExecutionPolicy Bypass -File .\build_exe.ps1
```

El archivo generado se encuentra en `dist\StudocuHack.exe`.

## Uso legal y responsable

- Procesa únicamente documentos que hayas creado, que te pertenezcan o que estés expresamente autorizado a exportar.
- Respeta los derechos de autor, la privacidad, la integridad académica, los términos de Studocu y las leyes aplicables.
- No utilices este proyecto para eludir suscripciones, muros de pago, autenticación o controles de acceso.
- Studocu es una marca de su respectivo propietario. Este proyecto independiente no tiene relación oficial con Studocu.

## Licencia MIT

Copyright (c) 2026 QIHENG

Por la presente se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el «Software»), para utilizar el Software sin restricciones, incluidos, entre otros, los derechos de usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software, y para permitir que las personas a quienes se proporcione el Software hagan lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso deberán incluirse en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA «TAL CUAL», SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUIDAS, ENTRE OTRAS, LAS GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y AUSENCIA DE INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE RECLAMACIONES, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN CONTRACTUAL, EXTRACONTRACTUAL O DE OTRO TIPO, DERIVADAS DEL SOFTWARE, SU USO U OTRAS OPERACIONES RELACIONADAS CON EL SOFTWARE.

El texto oficial de la licencia es el archivo inglés [LICENSE](LICENSE).
