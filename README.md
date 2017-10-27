# Curso básico de Expresiones Regulares (REGEX) y Procesamiento de Lenguaje Natural (NLP) en español con ejemplos.

### Lenguaje de programación utilizado en este curso: PYTHON 2.7

**ENGLISH READERS: This repo, README, code comments and examples are in spanish*

En este REPO incluímos varios scripts básicos que sirven como introducción al uso de PYTHON para el Procesamiento de Lenguaje Natural.

Los archivos están ordenados como un curso y ampliamente comentados. En los comentarios dentro del código se explica como instalar, cofigurar y ejecutar las librerías desde python, siempre tomando en cuenta las consideraciones especiales para el idioma español, si bien se puede usar de guía para otros idioma.

#### En los comentarios del código de cada ejemplo encontrarás instrucciones detalladas para entender el código, además de guías paso a paso para descargar gratuitamente e instalar todos los programas que puedas necesitar en cada caso.

***

## Archivos incluídos hasta ahora:

1. [vacio.py](#1-vaciopy)
1. [helloWorldUTF8.py](#2-helloworldutf8py)
1. [simpleEncodingUTF8.py / simpleEncodingCP1252.py](#3-simpleencodingutf8py--simpleencodingcp1252py)
1. [simpleRegexUTF8.py](#4-simpleregexutf8py)
1. [argumentosSimple.py](#5-argumentossimplepy)
1. [argumentosParsed.py](#6-argumentosparsedpy)
1. [limpiarTexto.py](#7-limpiartextopy)
1. [contarPalabras.py](#8-contarpalabraspy)
1. [contarCaracteres.py](#9-contarcaracterespy)
1. [basicNLTK.py](#10-basicnltkpy)
    1. get-pip.py
    1. nltk_packages.txt
    1. instalar_nltk_data.py
1. [mediumNLTK.py](#11-mediumnltkpy)
1. [stanford-postaggerNLTK.py](#12-stanford-postaggernltkpy)
1. [simple-stanford-corenlp.py](#13-simple-stanford-corenlppy)
1. [medium-stanford-corenlp.py](#14-medium-stanford-corenlppy)
1. [basicFreeling.py](#15-basicfreelingpy)
   1. freelingwrapper.py

### 1. [vacio.py](https://github.com/sanxofon/basicnlp/vacio.py)

> Este script muestra las cabeceras "env" y "UTF8" que debe tener todo script de este repo. El archivo ".py" debe editarse con esta codificación. Además muestra cómo hacer comentarios dentro del código.

### 2. [helloWorldUTF8.py](https://github.com/sanxofon/basicnlp/helloWorldUTF8.py)

> Este programa intenta mostrar un ejemplo clásico pero considerando la codificación (UTF8, UNICODE, TERMINAL). Además muestra como solicitar información al usuario y como codificar/decodificar esta.

**Ejemplos de uso:**

	$ python helloWorldUTF8.py
		Hola, Anónimo
		¿Cómo te llamas?
		>> Santiago Chávez
		¡Hola, Santiago Chávez!

### 3. [simpleEncodingUTF8.py](https://github.com/sanxofon/basicnlp/simpleEncodingUTF8.py) / [simpleEncodingCP1252.py](https://github.com/sanxofon/basicnlp/simpleEncodingCP1252.py)

> El script **simpleEncodingUTF8.py** como trabajar con las distintas codificaciones de texto (UTF8, UNICODE, cp1250, etc.). Además muestra como "decodificar" y como detectar la codificación de las cadenas de texto.
El script **simpleEncodingCP1252.py** es una copia idéntica de la versión UTF pero el archivo está guardado con codificación típica de windows-1252. Se pueden apreciar los errores que el mismo código genera.

**Ejemplos de uso:**

	$ python simpleEncodingUTF8.py

### 4. [simpleRegexUTF8.py](https://github.com/sanxofon/basicnlp/simpleRegexUTF8.py)

> Este script muestra como realizar búsquedas y reemplazos 
	de cadenas de texto mediante Expresiones Regulares (REGEX)
	utilizando caracteres Unicode.

**Ejemplos de uso:**

	$ python simpleRegexUTF8.py

### 5. [argumentosSimple.py](https://github.com/sanxofon/basicnlp/argumentosSimple.py)

> Este programa muestra como recibir informacion del usuario al ejecutar el programa por medio de "argumentos", considerando la codificación. (Imposible de resolver en Windows 7)

**Ejemplos de uso:**

	$ python argumentosSimple.py Santiago Chávez
	$ python argumentosSimple.py "Santiago Chávez"
	$ python argumentosSimple.py "Santiago Chávez" utf8 > test.txt

### 6. [argumentosParsed.py](https://github.com/sanxofon/basicnlp/argumentosParsed.py)

> Este programa también muestra como recibir informacion del usuario al ejecutar el programa por medio de "argumentos", pero usando la librería "argparse" que simplifica el proceso además de que provee un mensaje de ayuda a los usuarios.

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python argumentosParsed.py -h
		usage: argumentosParsed.py [-h] -a ARG [-m] [-M]
		
		Este programa muestra como recibir datos del usuario como argumentos Ejemplo:
		python argumentosParsed.py -n "Santiago Chávez"
		
		optional arguments:
		  -h, --help         show this help message and exit
		  -a ARG, --arg ARG  Argumento, acepta una cadena de texto
		  -m, --min          Convertir a minúsculas: Booleano, no recibe valor
		  -M, --may          Convertir a MAYÚSCULAS: Booleano, no recibe valor

**Ejemplos de uso:**

	$ python argumentosParsed.py -n "Santiago Chávez"
	$ python argumentosParsed.py -n "Santiago Chávez" -e

### 7. [limpiarTexto.py](https://github.com/sanxofon/basicnlp/limpiarTexto.py)

> Este programa intenta rectificar los saltos de línea de un texto mal formateado y/o aplica un reemplazo regex definido por el usuario.

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python limpiarTexto.py -h
		usage: limpiarTexto.py [-h] -f FILE [-n] [-s SEARCH [SEARCH ...]]
				       [-r REPLACE [REPLACE ...]] [-j] [-m MAXLN] [-e] [-u]

		Este programa intenta rectificar los saltos de línea de un texto mal
		formateado y/o aplica un reemplazo regex definido por el usuario. Ejemplo:
		python limpiarTexto.py -f "texto1.txt" -n -u -m 2 > "texto1_limpio.txt"

		optional arguments:
		  -h, --help            show this help message and exit
		  -f FILE, --file FILE  Define el archivo de texto a procesar (REQUERIDO).
		  -n, --newline         Rectificar saltos de línea de un texto.
		  -s SEARCH [SEARCH ...], --search SEARCH [SEARCH ...]
				        Cadena(s) de búsqueda REGEX definidas por el usuario.
		  -r REPLACE [REPLACE ...], --replace REPLACE [REPLACE ...]
				        Cadena(s) de reemplazo REGEX definidas por el usuario.
		  -j, --join            Une dos líneas no vacías consecutivas con un espacio.
		  -m MAXLN, --maxln MAXLN
				        Define el máximo de líneas vacías consecutivas.
		  -e, --explode         Separa todos los enunciados con salto d línea.
		  -u, --utf8            Codificar la salida como UTF-8.

**Ejemplos de uso:**

	$ python limpiarTexto.py -f "texto1.txt" -n -u -m 2 > "texto1_limpio.txt"
	$ python limpiarTexto.py -f "texto2.txt" -n -u -m 4 -j -s "(\-\-)" -r "—" > "texto2_limpio.txt"

### 8. [contarPalabras.py](https://github.com/sanxofon/basicnlp/contarPalabras.py)

> Este programa intenta contar la frecuencia de las palabras de un texto.

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python contarPalabras.py -h
		usage: contarPalabras.py [-h] -f FILE [-o ORD] [-i] [-q] [-u]

		Este programa intenta contar la frecuencia de las palabras de un texto.
		Ejemplo: python contarPalabras.py -f texto1.txt -o aF -i

		optional arguments:
		  -h, --help            show this help message and exit
		  -f FILE, --file FILE  Define el archivo de texto a procesar (REQUERIDO).
		  -o ORD, --ord ORD     Ordenar contador: a:Alfabéticamente, f:Frecuencia
				        (Mayúscula=Reversa).
		  -i, --interactive     Contar palabras, consulta interactiva.
		  -q, --freq            Mostrar frecuencia de conteos.
		  -u, --utf8            Codificar la salida como UTF-8.

**Ejemplos de uso:**

	$ python contarPalabras.py -f "texto2.txt" > "texto2_palabras.txt"
	$ python contarPalabras.py -f "text1o.txt" -q -o af > "texto1_palabras.txt"

### 9. [contarCaracteres.py](https://github.com/sanxofon/basicnlp/contarCaracteres.py)

> Este programa intenta contar la frecuencia de las caracteres de un texto.

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python contarCaracteres.py -h
		usage: contarCaracteres.py [-h] -f FILE [-o ORD] [-q] [-u]

		Este programa intenta contar la frecuencia de las caracteres de un texto.
		Ejemplo: python contarCaracteres.py -f texto1.txt -o aF -i

		optional arguments:
		  -h, --help            show this help message and exit
		  -f FILE, --file FILE  Define el archivo de texto a procesar (REQUERIDO).
		  -o ORD, --ord ORD     Ordenar contador: a:Alfabéticamente, f:Frecuencia
				        (Mayúscula=Reversa).
		  -q, --freq            Mostrar frecuencia de conteos.
		  -u, --utf8            Codificar la salida como UTF-8.

**Ejemplos de uso:**

	$ python contarCaracteres.py -f "texto2.txt" > "texto2_caracteres.txt"
	$ python contarCaracteres.py -f "text1o.txt" -q -o af > "texto1_caracteres.txt"

### 10. [basicNLTK.py](https://github.com/sanxofon/basicnlp/basicNLTK.py)

> Este script muestra los primeros pasos de uso de la librería "nltk" (Natural Language Toolkit) para procesamiento de lenguaje natural. Incluye instrucciones básicas de instalación, configuración y descarga de Corpora, Diccionarios, etc.
> 
> En los comentarios dentro del código se muestran los usos de los archivos incluídos:

> 1. get-pip.py
> 1. nltk_packages.txt
> 1. instalar_nltk_data.py

**Ejemplos de uso:**

	$ python basicNLTK.py

	$ python basicNLTK.py -u > basicNLTK_test.txt

### 11. [mediumNLTK.py](https://github.com/sanxofon/basicnlp/mediumNLTK.py)

> Este script muestra es una versión un poco más avanzada de uso de NLTK, utilizando el corpus CESS.

**Ejemplos de uso:**

	$ python mediumNLTK.py

	$ python mediumNLTK.py -u > mediumNLTK_test.txt

### 12. [stanford-postaggerNLTK.py](https://github.com/sanxofon/basicnlp/stanford-postaggerNLTK.py)

> En este script mostraré cómo usar NLTK con un programa externo (Stanford POS-Tagger) para "etiquetar" 
las palabras de una frase en español con mejores resultados que los logrados con los ejemplos anteriores.

**Ejemplos de uso:**

	$ python stanford-postaggerNLTK.py

	$ python stanford-postaggerNLTK.py -u > stanford-postaggerNLTK_test.txt

### 13. [simple-stanford-corenlp.py](https://github.com/sanxofon/basicnlp/simple-stanford-corenlp.py)

> En este script se muestra cómo usar el software Stanford CoreNLP. CoreNLP es un programa escrito en leguaje JAVA, sin embargo podemos usar CoreNLP desde Python usando un programa intermedio del tipo "wrapper".

**Ejemplos de uso:**

	$ python simple-stanford-corenlp.py

	$ python simple-stanford-corenlp.py -u > simple-stanford-corenlp_test.txt

### 14. [medium-stanford-corenlp.py](https://github.com/sanxofon/basicnlp/medium-stanford-corenlp.py)

> En este script se muestra cómo usar la API del software Stanford CoreNLP para "anotar" textos en español,
haciendo un us más avanzado de este poderoso sofware de procesamiento de lenguaje natural.

**Ejemplos de uso:**

	$ python medium-stanford-corenlp.py

	$ python medium-stanford-corenlp.py -u > medium-stanford-corenlp.xml

### 15. [basicFreeling.py](https://github.com/sanxofon/basicnlp/basicFreeling.py)

**EN DESARROLLO...**

> Este script necesita del archivo incluído:
> 
> 1. freelingwrapper.py

***

## License

- [**MIT License**](LICENSE.md)

***

## Manteiner

- [**Santiago Chávez** (@sanxofon)](http://lengua.la/sanx.php)
 
***

## Testing

	echo Testing "helloWorldUTF8"
	python helloWorldUTF8.py
	
	echo Testing "simpleEncodingUTF8"
	python simpleEncodingUTF8.py
	echo Testing "simpleEncodingCP1252"
	python simpleEncodingCP1252.py
	echo Testing "simpleRegexUTF8"
	python simpleRegexUTF8.py
	echo Testing "argumentosSimple"
	python argumentosSimple.py Santiago Chávez
	python argumentosSimple.py "Santiago Chávez"
	python argumentosSimple.py "Santiago Chávez" utf8 > "test/test_argumentosSimple.txt"
	echo Testing "argumentosParsed"
	python argumentosParsed.py -a "Santiago Chávez"
	python argumentosParsed.py -a "Santiago Chávez" -m
	python argumentosParsed.py -a "Santiago Chávez" -M
	echo Este ejemplo debe mostrar error de codificación
	python argumentosParsed.py -a "Santiago Chávez" -M > "test/test_argumentosParsed.txt"
	echo Testing "limpiarTexto"
	python limpiarTexto.py -f "test/texto1.txt" -n -u -m 2 > "test/texto1_limpio.txt"
	python limpiarTexto.py -f "test/texto2.txt" -n -u -m 4 -j -s "(\-\-)" -r "—" > "test/texto2_limpio.txt"
	python limpiarTexto.py -f "test/texto1.txt" -n -u -m 1 -e > "test/texto1_enunciados.txt"
	python limpiarTexto.py -f "test/texto2.txt" -n -u -m 1 -j -e -s "(\-\-)" -r "—" > "test/texto2_enunciados.txt"
	echo Testing "contarPalabras"
	python contarPalabras.py -f "test/texto1.txt" -q -o af -u > "test/texto1_palabras.txt"
	python contarPalabras.py -f "test/texto2.txt" -q -o af -u > "test/texto2_palabras.txt"
	echo Testing "contarCaracteres"
	python contarCaracteres.py -f "test/texto2.txt" -o aF -u > "test/texto2_caracteres.txt"
	python contarCaracteres.py -f "test/texto1.txt" -o aF -u > "test/texto1_caracteres.txt"
	echo Testing "basicNLTK"
	python basicNLTK.py
	echo Testing "mediumNLTK"
	python mediumNLTK.py
	echo Testing "stanford-postaggerNLTK"
	python stanford-postaggerNLTK.py
	echo Testing "simple-stanford-corenlp"
	python simple-stanford-corenlp.py
	echo Testing "medium-stanford-corenlp"
	python medium-stanford-corenlp.py
