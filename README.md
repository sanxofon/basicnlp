# Ejemplos básicos de PYTHON para NLP

En este REPO incluímos varios scripts básicos que sirven como introducción al uso de PYTHON para el Procesamiento de Lenguaje Natural.

*All comments and examples are in spanish*

***

## Archivos incluídos hasta ahora:

## 1. helloWorldUTF8.py

> Este programa intenta mostrar un ejemplo clásico pero considerando la codificación (UTF8, UNICODE, TERMINAL). Además muestra como solicitar información al usuario y como codificar/decodificar esta.

**Ejemplos de uso:**

	$ python helloWorldUTF8.py
		Hola, Anónimo
		¿Cómo te llamas?
		>> Santiago Chávez
		¡Hola, Santiago Chávez!


## 2. userArgumentsSimple.py

> Este programa muestra como recibir informacion del usuario al ejecutar el programa por medio de "argumentos", considerando la codificación. (Imposible de resolver en Windows 7)

**Ejemplos de uso:**

	$ python userArgumentsSimple.py Santiago Chávez
	$ python userArgumentsSimple.py "Santiago Chávez"
	$ python userArgumentsSimple.py "Santiago Chávez" utf8 > test.txt

## 3. userArgumentsParsed.py

> Este programa también muestra como recibir informacion del usuario al ejecutar el programa por medio de "argumentos", pero usando la librería "argparse" que simplifica el proceso además de que provee un mensaje de ayuda a los usuarios.

**Ayuda:**
Para desplegar la ayuda en terminal ejecute:

	$ python userArgumentsParsed.py -h
		usage: userArgumentsParsed.py [-h] -n NAME [-e]

		Este programa muestra como recibir datos del usuario como argumentos Ejemplo:
		python userArgumentsParsed.py -n "Santiago Chávez"

		optional arguments:
		  -h, --help            show this help message and exit
		  -n NAME, --name NAME  Nombre del usuario
		  -e, --extra           Extra: Booleano, no recibe valor

**Ejemplos de uso:**

	$ python userArgumentsParsed.py -n "Santiago Chávez"
	$ python userArgumentsParsed.py -n "Santiago Chávez" -e

## 4. limpiarTexto.py

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

## 5. contarPalabras.py

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

## TESTING

	python limpiarTexto.py -f "texto1.txt" -n -u -m 2 > "texto1_limpio.txt"
	python limpiarTexto.py -f "texto2.txt" -n -u -m 4 -j -s "(\-\-)" -r "—" > "texto2_limpio.txt"
	python limpiarTexto.py -f "texto1.txt" -n -u -m 1 -e > "texto1_enunciados.txt"
	python limpiarTexto.py -f "texto2.txt" -n -u -m 1 -j -e -s "(\-\-)" -r "—" > "texto2_enunciados.txt"
	python contarPalabras.py -f "texto1.txt" -q -o af -u > "texto1_palabras.txt"
	python contarPalabras.py -f "texto2.txt" -q -o af -u > "texto2_palabras.txt"
***

## License

- [**MIT License**](LICENSE.md)

***

## Manteiner

- [**Santiago Chávez** (@sanxofon)](http://lengua.la/sanx.php)