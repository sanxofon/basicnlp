# Curso básico de Expresiones Regulares (REGEX) y Procesamiento de Lenguaje Natural (NLP) en español con ejemplos.

### Lenguajes de programación utilizados en este curso: PYTHON 2.7 y PYTHON 3.6

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
1. [mediumRegexUTF8.py](#5-mediumregexutf8py)
1. [argumentosSimple.py](#6-argumentossimplepy)
1. [argumentosParsed.py](#7-argumentosparsedpy)
1. [limpiarTexto.py](#8-limpiartextopy)
    1. test/
1. [contarPalabras.py](#9-contarpalabraspy)
1. [contarCaracteres.py](#10-contarcaracterespy)
1. [basicNLTK.py](#11-basicnltkpy)
    1. get-pip.py
    1. nltk_packages.txt
    1. instalar_nltk_data.py
1. [mediumNLTK.py](#12-mediumnltkpy)
1. [stanford-postaggerNLTK.py](#13-stanford-postaggernltkpy)
1. [simple-stanford-corenlp.py](#14-simple-stanford-corenlppy)
1. [medium-stanford-corenlp.py](#15-medium-stanford-corenlppy)
1. [basicFreeling.py](#16-basicfreelingpy)
   1. freelingwrapper.py

### 1. [vacio.py](vacio.py)

> Este script muestra las cabeceras "env" y "UTF8" que debe tener todo script de este repo. El archivo ".py" debe editarse con esta codificación. Además muestra cómo hacer comentarios dentro del código.

En la carpeta **encoding/** escribí un pequeño texto que intenta explicar el porqué de la necesidad de los encodings así como una breve historia de algunos muy famosos:

- [**El ABCii de la codificación de caracteres en un sistema digital**](encoding/README.md)

### 2. [helloWorldUTF8.py](helloWorldUTF8.py)

> Este programa intenta mostrar un ejemplo clásico pero considerando la codificación (UTF8, UNICODE, TERMINAL). Además muestra como solicitar información al usuario y como codificar/decodificar esta.

**Ejemplo de uso:**

	$ python helloWorldUTF8.py

### 3. [simpleEncodingUTF8.py](simpleEncodingUTF8.py) / [simpleEncodingCP1252.py](simpleEncodingCP1252.py)

> El script **simpleEncodingUTF8.py** como trabajar con las distintas codificaciones de texto (UTF8, UNICODE, cp1250, etc.). Además muestra como "decodificar" y como detectar la codificación de las cadenas de texto.
El script **simpleEncodingCP1252.py** es una copia idéntica de la versión UTF pero el archivo está guardado con codificación típica de windows-1252. Se pueden apreciar los errores que el mismo código genera.

**Ejemplos de uso:**

	$ python simpleEncodingUTF8.py

### 4. [simpleRegexUTF8.py](simpleRegexUTF8.py)

> Este script muestra como realizar búsquedas y reemplazos 
	de cadenas de texto mediante Expresiones Regulares (REGEX)
	utilizando caracteres Unicode.

**Ejemplos de uso:**

	$ python simpleRegexUTF8.py

### 5. [mediumRegexUTF8.py](mediumRegexUTF8.py)

> Este script muestra como realizar búsquedas RegEx más complejas 
	sobre palabras y tipos de caracteres Unicode.

**Ejemplos de uso:**

	$ python mediumRegexUTF8.py

| Puedes ver el resultado de la ejecución del archivo [acá](test/mediumRegexUTF8.txt).

### 6. [argumentosSimple.py](argumentosSimple.py)

> Este programa muestra como recibir informacion del usuario al ejecutar el programa por medio de "argumentos", considerando la codificación. (Imposible de resolver en Windows 7)

**Ejemplos de uso:**

	$ python argumentosSimple.py Santiago Chávez
	$ python argumentosSimple.py "Santiago Chávez"
	$ python argumentosSimple.py "Santiago Chávez" utf8 > test.txt


### 7. [argumentosParsed.py](argumentosParsed.py)

> Este programa también muestra como recibir informacion del usuario al ejecutar el programa por medio de "argumentos", pero usando la librería "argparse" que simplifica el proceso además de que provee un mensaje de ayuda a los usuarios.

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python argumentosParsed.py -h

**Ejemplos de uso:**

	$ python argumentosParsed.py -n "Santiago Chávez"
	$ python argumentosParsed.py -n "Santiago Chávez" -e

### 8. [limpiarTexto.py](limpiarTexto.py)

> Este programa intenta rectificar los saltos de línea de un texto mal formateado y/o aplica un reemplazo regex definido por el usuario.

Para este programa (y otros) se utiliza la carpeta **test/** que además contiene dos archivos de texto que se pueden usar para testear el script:

- [texto1.txt](test/texto1.txt) (Textos varios de Groucho Marx)
- [texto2.txt](test/texto2.txt) (*El origen del pensamiento* de Armando Palacio Valdés)

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python limpiarTexto.py -h

**Ejemplos de uso:**

	$ python limpiarTexto.py -f "texto1.txt" -n -u -m 2 > "texto1_limpio.txt"
	$ python limpiarTexto.py -f "texto2.txt" -n -u -m 4 -j -s "(\-\-)" -r "—" > "texto2_limpio.txt"

### 9. [contarPalabras.py](contarPalabras.py)

> Este programa intenta contar la frecuencia de las palabras de un texto.

Para este programa (y otros) se utiliza la carpeta **test/** que además contiene dos archivos de texto que se pueden usar para testear el script:

- [texto1.txt](test/texto1.txt) (Textos varios de Groucho Marx)
- [texto2.txt](test/texto2.txt) (*El origen del pensamiento* de Armando Palacio Valdés)

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python contarPalabras.py -h

**Ejemplos de uso:**

	$ python contarPalabras.py -f "texto2.txt" > "texto2_palabras.txt"
	$ python contarPalabras.py -f "text1o.txt" -q -o af > "texto1_palabras.txt"

### 10. [contarCaracteres.py](contarCaracteres.py)

> Este programa intenta contar la frecuencia de las caracteres de un texto.

Para este programa (y otros) se utiliza la carpeta **test/** que además contiene dos archivos de texto que se pueden usar para testear el script:

- [texto1.txt](test/texto1.txt) (Textos varios de Groucho Marx)
- [texto2.txt](test/texto2.txt) (*El origen del pensamiento* de Armando Palacio Valdés)

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python contarCaracteres.py -h

**Ejemplos de uso:**

	$ python contarCaracteres.py -f "texto2.txt" > "texto2_caracteres.txt"
	$ python contarCaracteres.py -f "text1o.txt" -q -o af > "texto1_caracteres.txt"

### 11. [basicNLTK.py](basicNLTK.py)

> Este script muestra los primeros pasos de uso de la librería "nltk" (Natural Language Toolkit) para procesamiento de lenguaje natural. Incluye instrucciones básicas de instalación, configuración y descarga de Corpora, Diccionarios, etc.
> 
> En los comentarios dentro del código se muestran los usos de los archivos incluídos:

> 1. get-pip.py
> 1. nltk_packages.txt
> 1. instalar_nltk_data.py

**Ejemplos de uso:**

	$ python basicNLTK.py

	$ python basicNLTK.py -u > basicNLTK_test.txt

### 12. [mediumNLTK.py](mediumNLTK.py)

> Este script muestra es una versión un poco más avanzada de uso de NLTK, utilizando el corpus CESS.

**Ejemplos de uso:**

	$ python mediumNLTK.py

	$ python mediumNLTK.py -u > mediumNLTK_test.txt

### 13. [stanford-postaggerNLTK.py](stanford-postaggerNLTK.py)

> En este script mostraré cómo usar NLTK con un programa externo (Stanford POS-Tagger) para "etiquetar" 
las palabras de una frase en español con mejores resultados que los logrados con los ejemplos anteriores.

**Ejemplos de uso:**

	$ python stanford-postaggerNLTK.py

	$ python stanford-postaggerNLTK.py -u > stanford-postaggerNLTK_test.txt

### 14. [simple-stanford-corenlp.py](simple-stanford-corenlp.py)

> En este script se muestra cómo usar el software Stanford CoreNLP. CoreNLP es un programa escrito en leguaje JAVA, sin embargo podemos usar CoreNLP desde Python usando un programa intermedio del tipo "wrapper".

**Ejemplos de uso:**

	$ python simple-stanford-corenlp.py

	$ python simple-stanford-corenlp.py -u > simple-stanford-corenlp_test.txt

### 15. [medium-stanford-corenlp.py](medium-stanford-corenlp.py)

> En este script se muestra cómo usar la API del software Stanford CoreNLP para "anotar" textos en español,
haciendo un us más avanzado de este poderoso sofware de procesamiento de lenguaje natural.

**Ejemplos de uso:**

	$ python medium-stanford-corenlp.py

	$ python medium-stanford-corenlp.py -u > medium-stanford-corenlp.xml

### 16. [basicFreeling.py](basicFreeling.py)

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

- [**MIT License**](LICENSE.md)

***

## Manteiner

- [**Santiago Chávez** (@sanxofon)](http://lengua.la/sanx.php)
 
***

## Testing

- [**Tests**](TESTS.md)