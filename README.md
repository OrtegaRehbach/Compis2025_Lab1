# Lab 1: Introducción a ANTLR – Construcción de Compiladores

Este repositorio contiene el laboratorio 1 del curso “Construcción de Compiladores” en UVG. El objetivo es usar ANTLR para:

* Definir una gramática simple (MiniLang)
* Generar un parser y un lexer en Python
* Validar sintácticamente un programa de ejemplo con un driver dentro de un contenedor Docker

## Contenido

* `MiniLang.g4`: Gramática ANTLR para MiniLang.
* `Driver.py`: Script Python que carga un archivo de programa, ejecuta el lexer y el parser.
* `program_test.txt`: Programa de prueba para validar la gramática.
* `python-venv.sh`: Script opcional para crear un entorno virtual.
* `requirements.txt`: Dependencias Python (`antlr4-python3-runtime`, etc.).
* `commands/antlr` y `commands/grun`: Wrappers para invocar ANTLR y GRUN.
* `Dockerfile`: Imagen con Java, Python y ANTLR preinstalados.

## Requisitos Previos

* Docker (Windows, macOS o Linux).
* Conexión a internet para descargar imágenes y paquetes.

## Construcción de la Imagen Docker

Desde la raíz de este repositorio:

```bash
docker build --rm -t lab1-image .
```

## Ejecución del Contenedor

Para montar la carpeta `program` y abrir un shell interactivo:

```bash
docker run --rm -it -v "${PWD}/program:/program" lab1-image bash
```

> En PowerShell se utiliza `${PWD}`; en CMD se puede usar `%cd%`.

## Generación del Parser

Dentro del contenedor, en `/program`:

```bash
antlr -Dlanguage=Python3 MiniLang.g4
```

## Ejecución del Driver

```bash
python3 Driver.py program_test.txt
```

* **Sin errores**: la sintaxis del programa es válida.
* **Con errores**: ANTLR mostrará mensajes que describen el error junto con su ubicación.

## Video de Demostración

Video con la explicación:

[https://youtu.be/tM59sn8oHd8](https://youtu.be/tM59sn8oHd8)
