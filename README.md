# Curso básico de Expresiones Regulares (REGEX) y Procesamiento de Lenguaje Natural (NLP) en español con ejemplos.

### Lenguaje de programación utilizado en este curso: PYTHON 2.7

> *ENGLISH READERS: This repo, README, code comments and examples are in spanish*

En este REPO incluímos varios scripts básicos que sirven como introducción al uso de PYTHON para el Procesamiento de Lenguaje Natural.

Los archivos están ordenados como un curso y ampliamente comentados. En los comentarios dentro del código se explica como instalar, cofigurar y ejecutar las librerías desde python, siempre tomando en cuenta las consideraciones especiales para el idioma español, si bien se puede usar de guía para otros idioma.

#### En los comentarios del código de cada ejemplo encontrarás instrucciones detalladas para entender el código, además de guías paso a paso para descargar gratuitamente e instalar todos los programas que puedas necesitar en cada caso.

### Guías anexas

El curso está acompañado por algunos artículos que puedes leer independientemente y aportan conocimientos necesarios para poder llevar a cabo el curso a través de los archivos incluídos:

1. **[El ABCii de la codificación de caracteres en un sistema digital](encoding/README.md)**
1. **[En el principio fue la línea de comandos: Curso básico de uso de la terminal o consola.](terminal/README.md)**
	1. [Guía rápida de búsqueda avanzada en Google](terminal/BuscarEnGoogle.md)
1. **[Curso rápido de expresiones regulares en español](regexbasico/README.md)**
	1. [Regex CheatSheet - Guía rápida de expresiones regulares](regexbasico/cheatsheet.md)

**¿Dudas? ¿Comentarios? Contáctamen por twitter: [@sanxofon](https://twitter.com/sanxofon)**

***

## Archivos incluídos hasta ahora:

1. [vacio.py](#1-vaciopy)
    1. encoding/ ([El ABCii de la codificación de caracteres en un sistema digital](encoding/))
1. [helloWorldUTF8.py](#2-helloworldutf8py)
1. [simpleEncodingUTF8.py / simpleEncodingCP1252.py](#3-simpleencodingutf8py--simpleencodingcp1252py)
1. [simpleRegexUTF8.py](#4-simpleregexutf8py)
1. [argumentosSimple.py](#5-argumentossimplepy)
1. [argumentosParsed.py](#6-argumentosparsedpy)
1. [limpiarTexto.py](#7-limpiartextopy)
    1. test/
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

### 1. [vacio.py](https://github.com/sanxofon/basicnlp/blob/master/vacio.py)

> Este script muestra las cabeceras "env" y "UTF8" que debe tener todo script de este repo. El archivo ".py" debe editarse con esta codificación. Además muestra cómo hacer comentarios dentro del código.

En la carpeta **encoding/** escribí un pequeño texto que intenta explicar el porqué de la necesidad de los encodings así como una breve historia de algunos muy famosos:

- [**El ABCii de la codificación de caracteres en un sistema digital**](encoding/README.md)

### 2. [helloWorldUTF8.py](https://github.com/sanxofon/basicnlp/blob/master/helloWorldUTF8.py)

> Este programa intenta mostrar un ejemplo clásico pero considerando la codificación (UTF8, UNICODE, TERMINAL). Además muestra como solicitar información al usuario y como codificar/decodificar esta.

**Ejemplo de uso:**

	$ python helloWorldUTF8.py
```Diff
+	Hola, Anónimo
+	¿Cómo te llamas?
-	>> Santiago Chávez
+	¡Hola, Santiago Chávez!
```

### 3. [simpleEncodingUTF8.py](https://github.com/sanxofon/basicnlp/blob/master/simpleEncodingUTF8.py) / [simpleEncodingCP1252.py](https://github.com/sanxofon/basicnlp/blob/master/simpleEncodingCP1252.py)

> El script **simpleEncodingUTF8.py** como trabajar con las distintas codificaciones de texto (UTF8, UNICODE, cp1250, etc.). Además muestra como "decodificar" y como detectar la codificación de las cadenas de texto.
El script **simpleEncodingCP1252.py** es una copia idéntica de la versión UTF pero el archivo está guardado con codificación típica de windows-1252. Se pueden apreciar los errores que el mismo código genera.

**Ejemplos de uso:**

	$ python simpleEncodingUTF8.py
```Diff
-		>> IMPRIMIMOS CADENAS DE TEXTO NORMAL DIRECTAMENTE
+		El veloz murciélago hindú comía feliz cardillo y kiwi.
+		La cigüena tocaba el saxofón detrás del palenque de paja.
+		El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.
+		Exhíbanse politiquillos zafios,
+		con orejas kilométricas
+			y unas de gavilán.
+		—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!
+		عـفقكلمنهوى
+		\u0639\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649
+		ᘹᙀᙁᙂᙃᙄᙅᙆᙇᙈᙉ
+		\u1639\u1640\u1641\u1642\u1643\u1644\u1645\u1646\u1647\u1648\u1649

-		>> IMPRIMIMOS CADENAS DE TEXTO NORMAL DECODIFICADAS (UTF-8)
+		El veloz murciélago hindú comía feliz cardillo y kiwi.
+		La cigüena tocaba el saxofón detrás del palenque de paja.
+		El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.
+		Exhíbanse politiquillos zafios,
+		con orejas kilométricas
+			y unas de gavilán.
+		—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!
+		عـفقكلمنهوى
+		\u0639\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649
+		ᘹᙀᙁᙂᙃᙄᙅᙆᙇᙈᙉ
+		\u1639\u1640\u1641\u1642\u1643\u1644\u1645\u1646\u1647\u1648\u1649

-		>> IMPRIMIMOS CADENAS DE TEXTO UNICODE
+		El veloz murciélago hindú comía feliz cardillo y kiwi.
+		La cigüena tocaba el saxofón detrás del palenque de paja.
+		El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.
+		Exhíbanse politiquillos zafios,
+		con orejas kilométricas
+			y unas de gavilán.
+		—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!
+		عـفقكلمنهوى
+		عـفقكلمنهوى
+		ᘹᙀᙁᙂᙃᙄᙅᙆᙇᙈᙉ
+		ᘹᙀᙁᙂᙃᙄᙅᙆᙇᙈᙉ

-		>> IMPRIMIMOS CADENAS DE TEXTO RAW-UNICODE
+		El veloz murciélago hindú comía feliz cardillo y kiwi.\nLa cigüena tocaba el saxofón detrás del palenque de paja.
+		El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.
+		Exhíbanse politiquillos zafios,\ncon orejas kilométricas\n\ty unas de gavilán.
+		—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!
+		عـفقكلمنهوى
+		عـفقكلمنهوى
+		ᘹᙀᙁᙂᙃᙄᙅᙆᙇᙈᙉ
+		ᘹᙀᙁᙂᙃᙄᙅᙆᙇᙈᙉ
```

### 4. [simpleRegexUTF8.py](https://github.com/sanxofon/basicnlp/blob/master/simpleRegexUTF8.py)

> Este script muestra como realizar búsquedas y reemplazos 
	de cadenas de texto mediante Expresiones Regulares (REGEX)
	utilizando caracteres Unicode.

**Ejemplos de uso:**

	$ python simpleRegexUTF8.py
```Diff
-		>> RE.SEARCH
+		Coincidencia en el índice 22, 28
+		Grupos:
+			con
+			el

-		>> RE.FINDALL
+		Coincidencias:
+			con el
+			te aguarda
+		Coincidencias Unicode:
+			con el
+			qué fin
+			te aguarda

-		>> RE.SUB
+		Original: 	—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!
+		Resultado: 	—¡Joven «emponzoñado» el con whisky, qué fin… aguarda te exhibir!
+		Unicode: 	—¡Joven «emponzoñado» el con whisky, fin qué… aguarda te exhibir!

-		>> RE.COMPILE
+		search:
+			22 28
+		findall:
+			con el
+			te aguarda
+		sub:
+			—¡Joven «emponzoñado» el con whisky, qué fin… aguarda te exhibir!
```

### 5. [argumentosSimple.py](https://github.com/sanxofon/basicnlp/blob/master/argumentosSimple.py)

> Este programa muestra como recibir informacion del usuario al ejecutar el programa por medio de "argumentos", considerando la codificación. (Imposible de resolver en Windows 7)

**Ejemplos de uso:**

	$ python argumentosSimple.py Santiago Chávez
```Diff
+		Argumentos recibidos:
+			1 . Santiago
+			2 . Chávez
```
	$ python argumentosSimple.py "Santiago Chávez"
```Diff
+		Argumentos recibidos:
+			1 . Santiago Chávez
```
	$ python argumentosSimple.py "Santiago Chávez" utf8 > test.txt
```Python
		# No devuelve nada, los resultados se guardan en el archivo "test.txt"
```

### 6. [argumentosParsed.py](https://github.com/sanxofon/basicnlp/blob/master/argumentosParsed.py)

> Este programa también muestra como recibir informacion del usuario al ejecutar el programa por medio de "argumentos", pero usando la librería "argparse" que simplifica el proceso además de que provee un mensaje de ayuda a los usuarios.

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python argumentosParsed.py -h
```Diff
+		usage: argumentosParsed.py [-h] -a ARG [-m] [-M]
+		
+		Este programa muestra como recibir datos del usuario como argumentos Ejemplo:
+		python argumentosParsed.py -n "Santiago Chávez"
+		
+		optional arguments:
+		  -h, --help         show this help message and exit
+		  -a ARG, --arg ARG  Argumento, acepta una cadena de texto
+		  -m, --min          Convertir a minúsculas: Booleano, no recibe valor
+		  -M, --may          Convertir a MAYÚSCULAS: Booleano, no recibe valor
```

**Ejemplos de uso:**

	$ python argumentosParsed.py -n "Santiago Chávez"
	$ python argumentosParsed.py -n "Santiago Chávez" -e

### 7. [limpiarTexto.py](https://github.com/sanxofon/basicnlp/blob/master/limpiarTexto.py)

> Este programa intenta rectificar los saltos de línea de un texto mal formateado y/o aplica un reemplazo regex definido por el usuario.

Para este programa (y otros) se utiliza la carpeta **test/** que además contiene dos archivos de texto que se pueden usar para testear el script:

- [texto1.txt](https://github.com/sanxofon/basicnlp/blob/master/test/texto1.txt) (Textos varios de Groucho Marx)
- [texto2.txt](https://github.com/sanxofon/basicnlp/blob/master/test/texto2.txt) (*El origen del pensamiento* de Armando Palacio Valdés)

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python limpiarTexto.py -h
```Diff
+		usage: limpiarTexto.py [-h] -f FILE [-n] [-s SEARCH [SEARCH ...]]
+				       [-r REPLACE [REPLACE ...]] [-j] [-m MAXLN] [-e] [-u]
+
+		Este programa intenta rectificar los saltos de línea de un texto mal
+		formateado y/o aplica un reemplazo regex definido por el usuario. Ejemplo:
+		python limpiarTexto.py -f "texto1.txt" -n -u -m 2 > "texto1_limpio.txt"
+
+		optional arguments:
+		  -h, --help            show this help message and exit
+		  -f FILE, --file FILE  Define el archivo de texto a procesar (REQUERIDO).
+		  -n, --newline         Rectificar saltos de línea de un texto.
+		  -s SEARCH [SEARCH ...], --search SEARCH [SEARCH ...]
+				        Cadena(s) de búsqueda REGEX definidas por el usuario.
+		  -r REPLACE [REPLACE ...], --replace REPLACE [REPLACE ...]
+				        Cadena(s) de reemplazo REGEX definidas por el usuario.
+		  -j, --join            Une dos líneas no vacías consecutivas con un espacio.
+		  -m MAXLN, --maxln MAXLN
+				        Define el máximo de líneas vacías consecutivas.
+		  -e, --explode         Separa todos los enunciados con salto d línea.
+		  -u, --utf8            Codificar la salida como UTF-8.
```

**Ejemplos de uso:**

	$ python limpiarTexto.py -f "texto1.txt" -n -u -m 2 > "texto1_limpio.txt"
	$ python limpiarTexto.py -f "texto2.txt" -n -u -m 4 -j -s "(\-\-)" -r "—" > "texto2_limpio.txt"

### 8. [contarPalabras.py](https://github.com/sanxofon/basicnlp/blob/master/contarPalabras.py)

> Este programa intenta contar la frecuencia de las palabras de un texto.

Para este programa (y otros) se utiliza la carpeta **test/** que además contiene dos archivos de texto que se pueden usar para testear el script:

- [texto1.txt](https://github.com/sanxofon/basicnlp/blob/master/test/texto1.txt) (Textos varios de Groucho Marx)
- [texto2.txt](https://github.com/sanxofon/basicnlp/blob/master/test/texto2.txt) (*El origen del pensamiento* de Armando Palacio Valdés)

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python contarPalabras.py -h
```Diff
+		usage: contarPalabras.py [-h] -f FILE [-o ORD] [-i] [-q] [-u]
+
+		Este programa intenta contar la frecuencia de las palabras de un texto.
+		Ejemplo: python contarPalabras.py -f texto1.txt -o aF -i
+
+		optional arguments:
+		  -h, --help            show this help message and exit
+		  -f FILE, --file FILE  Define el archivo de texto a procesar (REQUERIDO).
+		  -o ORD, --ord ORD     Ordenar contador: a:Alfabéticamente, f:Frecuencia
+				        (Mayúscula=Reversa).
+		  -i, --interactive     Contar palabras, consulta interactiva.
+		  -q, --freq            Mostrar frecuencia de conteos.
+		  -u, --utf8            Codificar la salida como UTF-8.
```

**Ejemplos de uso:**

	$ python contarPalabras.py -f "texto2.txt" > "texto2_palabras.txt"
	$ python contarPalabras.py -f "text1o.txt" -q -o af > "texto1_palabras.txt"

### 9. [contarCaracteres.py](https://github.com/sanxofon/basicnlp/blob/master/contarCaracteres.py)

> Este programa intenta contar la frecuencia de las caracteres de un texto.

Para este programa (y otros) se utiliza la carpeta **test/** que además contiene dos archivos de texto que se pueden usar para testear el script:

- [texto1.txt](https://github.com/sanxofon/basicnlp/blob/master/test/texto1.txt) (Textos varios de Groucho Marx)
- [texto2.txt](https://github.com/sanxofon/basicnlp/blob/master/test/texto2.txt) (*El origen del pensamiento* de Armando Palacio Valdés)

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python contarCaracteres.py -h
```Diff
+		usage: contarCaracteres.py [-h] -f FILE [-o ORD] [-q] [-u]
+
+		Este programa intenta contar la frecuencia de las caracteres de un texto.
+		Ejemplo: python contarCaracteres.py -f texto1.txt -o aF -i
+
+		optional arguments:
+		  -h, --help            show this help message and exit
+		  -f FILE, --file FILE  Define el archivo de texto a procesar (REQUERIDO).
+		  -o ORD, --ord ORD     Ordenar contador: a:Alfabéticamente, f:Frecuencia
+				        (Mayúscula=Reversa).
+		  -q, --freq            Mostrar frecuencia de conteos.
+		  -u, --utf8            Codificar la salida como UTF-8.
```

**Ejemplos de uso:**

	$ python contarCaracteres.py -f "texto2.txt" > "texto2_caracteres.txt"
	$ python contarCaracteres.py -f "text1o.txt" -q -o af > "texto1_caracteres.txt"

### 10. [basicNLTK.py](https://github.com/sanxofon/basicnlp/blob/master/basicNLTK.py)

> Este script muestra los primeros pasos de uso de la librería "nltk" (Natural Language Toolkit) para procesamiento de lenguaje natural. Incluye instrucciones básicas de instalación, configuración y descarga de Corpora, Diccionarios, etc.
> 
> En los comentarios dentro del código se muestran los usos de los archivos incluídos:

> 1. get-pip.py
> 1. nltk_packages.txt
> 1. instalar_nltk_data.py

**Ejemplos de uso:**

	$ python basicNLTK.py

	$ python basicNLTK.py -u > basicNLTK_test.txt

### 11. [mediumNLTK.py](https://github.com/sanxofon/basicnlp/blob/master/mediumNLTK.py)

> Este script muestra es una versión un poco más avanzada de uso de NLTK, utilizando el corpus CESS.

**Ejemplos de uso:**

	$ python mediumNLTK.py

	$ python mediumNLTK.py -u > mediumNLTK_test.txt

### 12. [stanford-postaggerNLTK.py](https://github.com/sanxofon/basicnlp/blob/master/stanford-postaggerNLTK.py)

> En este script mostraré cómo usar NLTK con un programa externo (Stanford POS-Tagger) para "etiquetar" 
las palabras de una frase en español con mejores resultados que los logrados con los ejemplos anteriores.

**Ejemplos de uso:**

	$ python stanford-postaggerNLTK.py

	$ python stanford-postaggerNLTK.py -u > stanford-postaggerNLTK_test.txt

### 13. [simple-stanford-corenlp.py](https://github.com/sanxofon/basicnlp/blob/master/simple-stanford-corenlp.py)

> En este script se muestra cómo usar el software Stanford CoreNLP. CoreNLP es un programa escrito en leguaje JAVA, sin embargo podemos usar CoreNLP desde Python usando un programa intermedio del tipo "wrapper".

**Ejemplos de uso:**

	$ python simple-stanford-corenlp.py

	$ python simple-stanford-corenlp.py -u > simple-stanford-corenlp_test.txt

### 14. [medium-stanford-corenlp.py](https://github.com/sanxofon/basicnlp/blob/master/medium-stanford-corenlp.py)

> En este script se muestra cómo usar la API del software Stanford CoreNLP para "anotar" textos en español,
haciendo un us más avanzado de este poderoso sofware de procesamiento de lenguaje natural.

**Ejemplos de uso:**

	$ python medium-stanford-corenlp.py

	$ python medium-stanford-corenlp.py -u > medium-stanford-corenlp.xml

### 15. [basicFreeling.py](https://github.com/sanxofon/basicnlp/blob/master/basicFreeling.py)

> Tal vez el mejor software de NLP para el idioma españon es FREELING (en JAVA, como CoreNLP). Este script muestra cómo podemos analizar un texto con FREELING desde Python usando un wrapper.

> Este script necesita del archivo incluído:
> 
> 1. freelingwrapper.py

**Ejemplos de uso:**

	$ python basicFreeling.py > test/basicFreeling.json
	$ python basicFreeling.py -c /usr/share/freeling/config/es.cfg -l es -f test/texto1.txt > test/texto1_freeling.json
	$ python basicFreeling.py -f test/texto2.txt > test/texto2_freeling.json

***

## License

- [**MIT License**](https://github.com/sanxofon/basicnlp/blob/master/LICENSE.md)

***

## Manteiner

- [**Santiago Chávez** (@sanxofon)](http://lengua.la/sanx.php)
 
***

## Testing

```Shell
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
	python argumentosSimple.py "Santiago Chávez" utf8 > "test/argumentosSimple.txt"
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
	python basicNLTK.py -u > "test/basicNLTK.txt"
	echo Testing "mediumNLTK"
	python mediumNLTK.py -u > "test/mediumNLTK.txt"
	echo Testing "stanford-postaggerNLTK"
	python stanford-postaggerNLTK.py -u > "test/stanford-postaggerNLTK.txt"
	echo Testing "simple-stanford-corenlp"
    python simple-stanford-corenlp.py -u > test/simple-stanford-corenlp.txt
	echo Testing "medium-stanford-corenlp"
	python medium-stanford-corenlp.py -u -j > test/medium-stanford-corenlp.json
	python medium-stanford-corenlp.py -u -x > test/medium-stanford-corenlp.xml
	echo Testing "basicFreeling"
	python basicFreeling.py > test/basicFreeling.json
	python basicFreeling.py -c /usr/share/freeling/config/es.cfg -l es -f test/texto1.txt > test/texto1_freeling.json
	python basicFreeling.py -f test/texto2.txt > test/texto2_freeling.json
```
