# Ejemplos básicos en PYTHON de REGEX y NLP en español

En este REPO incluímos varios scripts básicos que sirven como introducción al uso de PYTHON para el Procesamiento de Lenguaje Natural.

*All comments and examples are in spanish*

***

## Archivos incluídos hasta ahora:

1. vacio.py
1. helloWorldUTF8.py
1. simpleEncodingUTF8.py / simpleEncodingCP1252.py
1. simpleRegexUTF8.py
1. argumentosSimple.py
1. argumentosParsed.py
1. limpiarTexto.py
1. contarPalabras.py

### 1. vacio.py

> Este script muestra las cabeceras "env" y "UTF8" que debe tener todo script de este repo. El archivo ".py" debe editarse con esta codificación.

### 2. helloWorldUTF8.py

> Este programa intenta mostrar un ejemplo clásico pero considerando la codificación (UTF8, UNICODE, TERMINAL). Además muestra como solicitar información al usuario y como codificar/decodificar esta.

**Ejemplos de uso:**

	$ python helloWorldUTF8.py
		Hola, Anónimo
		¿Cómo te llamas?
		>> Santiago Chávez
		¡Hola, Santiago Chávez!

### 3. simpleEncodingUTF8.py / simpleEncodingCP1252.py

> El script **simpleEncodingUTF8.py** como trabajar con las distintas codificaciones de texto (UTF8, UNICODE, cp1250, etc.). Además muestra como "decodificar" y como detectar la codificación de las cadenas de texto.
El script **simpleEncodingCP1252.py** es una copia idéntica de la versión UTF pero el archivo está guardado con codificación típica de windows-1252. Se pueden apreciar los errores que el mismo código genera.

**Ejemplos de uso:**

	$ python simpleEncodingUTF8.py

### 4. simpleRegexUTF8.py

> Este script muestra como realizar búsquedas y reemplazos 
	de cadenas de texto mediante Expresiones Regulares (REGEX)
	utilizando caracteres Unicode.

**Ejemplos de uso:**

	$ python simpleRegexUTF8.py

### 5. argumentosSimple.py

> Este programa muestra como recibir informacion del usuario al ejecutar el programa por medio de "argumentos", considerando la codificación. (Imposible de resolver en Windows 7)

**Ejemplos de uso:**

	$ python argumentosSimple.py Santiago Chávez
	$ python argumentosSimple.py "Santiago Chávez"
	$ python argumentosSimple.py "Santiago Chávez" utf8 > test.txt

### 6. argumentosParsed.py

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

### 7. limpiarTexto.py

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

### 8. contarPalabras.py

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
 
***

## Testing

Se puede guardar este script en un archivo .sh o .bat y ejecutar el testeo de un jalón. En Linux/Mac guardamos con el nombre "**testeo.sh**" y el Windows con el nombre "**testeo.bat**".
Para ejecutar el testeo desde la terminal, ya estando en el mismo directorio:

	$ testeo.bat

**testeo.sh** ó **testeo.bat**

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
	echo Este ejemplo debe mostrar error de codificación en Windows
	python argumentosParsed.py -a "Santiago Chávez" -M > "test/test_argumentosParsed.txt"
	echo Testing "limpiarTexto"
	python limpiarTexto.py -f "test/texto1.txt" -n -u -m 2 > "test/texto1_limpio.txt"
	python limpiarTexto.py -f "test/texto2.txt" -n -u -m 4 -j -s "(\-\-)" -r "—" > "test/texto2_limpio.txt"
	python limpiarTexto.py -f "test/texto1.txt" -n -u -m 1 -e > "test/texto1_enunciados.txt"
	python limpiarTexto.py -f "test/texto2.txt" -n -u -m 1 -j -e -s "(\-\-)" -r "—" > "test/texto2_enunciados.txt"
	echo Testing "contarPalabras"
	python contarPalabras.py -f "test/texto1.txt" -q -o af -u > "test/texto1_palabras.txt"
	python contarPalabras.py -f "test/texto2.txt" -q -o af -u > "test/texto2_palabras.txt"
***

## License

- [**MIT License**](LICENSE.md)

***

## Manteiner

- [**Santiago Chávez** (@sanxofon)](http://lengua.la/sanx.php)
