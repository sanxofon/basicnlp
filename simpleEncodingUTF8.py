#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Este script muestra como python trabaja en UNICODE y debemos
	saber como proveerle de la información necesaria para
	que pueda interpretar correctamente la cadena.
	Revise también: "simpleEncodingCP1252.py" para mostrar 
	más claramente algunos posibles errores de codificación
"""

# La librería "sys" no permite acceder a información del sistema
import sys

"""
CADENAS DE TEXTO EN PYTHON

Hay tres "tipos" de cadenas de texto en Python, en realidad todas 
son iguales para Python, la diferencia radica en cómo definimos 
la cadena y con qué codificación está guardada en la memoria.


	1. Cadenas de texto "normales"

		Estas cadenas se definen de la manera más simple:

		>> cadena_normal = "Cadena de texto"

		La "codificación" de esta cadena depende de la codificación del
		archivo mismo ".py" y la cabecera: # -*- coding: -*- del mismo
		archivo. En la mayoría de los casos en este curso se asume que
		una cadena str definida en el código tiene la codificación UTF-8.
		
		Cuando recibimos una variable desde la consola también vendrá 
		codificada como UTF-8 en Linux y Mac, pero normalmente vendrá 
		codificada como cp850 o cp65001 en una terminal Windows.
		
		Para que Python pueda procesar correctamente las cadenas de texto 
		"normales" deben ser "decodificadas", es decir pasadas al formato 
		de codificación universal en que trabaja Pyton: UNICODE.
"""

# Definimos una lista de cadenas de texto con acentos, diéresis y eñe
texto_normal = [
	"El veloz murciélago hindú comía feliz cardillo y kiwi.\nLa cigüena tocaba el saxofón detrás del palenque de paja.",
	"El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.",
	"Exhíbanse politiquillos zafios,\ncon orejas kilométricas\n\ty unas de gavilán.",
	"—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!",
	"عـفقكلمنهوى",
	"\u0639\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649",
	"ᘹᙀᙁᙂᙃᙄᙅᙆᙇᙈᙉ",
	"\u1639\u1640\u1641\u1642\u1643\u1644\u1645\u1646\u1647\u1648\u1649",
]
print ">> IMPRIMIMOS CADENAS DE TEXTO NORMAL DIRECTAMENTE"
# Imprimimos estas cadenas a la consola directamente
for t in texto_normal:
	print t

print
print ">> IMPRIMIMOS CADENAS DE TEXTO NORMAL DECODIFICADAS (UTF-8)"
# Imprimimos estas cadenas a la consola decodificadas (utf-8)
for t in texto_normal:
	print t.decode("utf-8")



"""
	2. Cadenas de texto "unicode"

		Estas cadenas se definen de la siguiente manera en el código:

		>> cadena_unicode = u"Cadena de texto"

		Nótese que hay una letra "u" minúscula antes de las primeras comillas.

		También podemos obtener una "cadena unicode" a partir de una "cadena normal"
		si conocemos la codificación de la cadena usando la propiedad: cadena.decode("codificación")
		Hay varias formas de saber la codificación de una cadena de texto "normal":

		
		CODE. Si la cadena está definida en el código (y no fue usado el prefijo "u")
		podemos estar seguros que la codificación es UTF-8 si el archivo está
		guardado correctamente y la cabecera (# -*- coding: utf-8 -*-) está incluída
		
		>>	cadena_unicode = cadena_normal.decode("utf-8")

		
		INPUT. Si la cadena fue recibida desde la terminal podemos averiguar la codificación
		usando: sys.stdin.encoding

		>>	import sys

		>>	cadena_input = raw_input("Ingrese cadena de texto: ")
		>>	cadena_unicode = cadena_input.decode(sys.stdin.encoding)

		>>	cadena_argumento = sys.argv[1]
		>>	cadena_unicode = cadena_argumento.decode(sys.stdin.encoding)

		
		FILE. Cuando capturamos un texto desde un archivo depende del archivo y si hay
		problemas deberemos usar herramientas más específicas para tratar de averiguarlo.
		
		Normalmente nos encontraremos con archivos ASCII, windows-1252, windows-1252, 
		UTF-16 y UTF-8, siendo este último el que usaremos por default.

		>>	with open('archivo.txt', 'r') as file:
		>>	cadena_file = file.read()
		>>	cadena_unicode = cadena_file('utf-8')

"""

texto_unicode = [
	u"El veloz murciélago hindú comía feliz cardillo y kiwi.\nLa cigüena tocaba el saxofón detrás del palenque de paja.",
	u"El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.",
	u"Exhíbanse politiquillos zafios,\ncon orejas kilométricas\n\ty unas de gavilán.",
	u"—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!",
	u"عـفقكلمنهوى",
	u"\u0639\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649",
	u"ᘹᙀᙁᙂᙃᙄᙅᙆᙇᙈᙉ",
	u"\u1639\u1640\u1641\u1642\u1643\u1644\u1645\u1646\u1647\u1648\u1649",
]

print
print ">> IMPRIMIMOS CADENAS DE TEXTO UNICODE"
# Imprimimos estas cadenas a la consola directamente
for t in texto_unicode:
	print t


"""
	3. Cadenas de texto "crudas" o "raw2

		Estas cadenas se definen de la siguiente manera en el código:

		>> cadena_raw = r"Cadena de texto raw"
		>> cadena_raw_unicode = ur"Cadena de texto raw"

		Nótese que hay una letra "r" minúscula antes de las primeras comillas.
		Nótese que podemos usar el prefijo compuesto "ur" para definir una cadena "raw-unicode".

		Al escribir expresiones regulares en Python, se recomienda utilizar cadenas "crudas" o "raw" en lugar 
		de cadenas Python normales. Las cadenas "raw" comienzan con un prefijo especial (r) y señalan a Python 
		que no debe interpretar las barras invertidas (\) y metacaracteres especiales en la cadena, lo que le 
		permite pasarlos directamente al motor de expresión regular.
		Esto significa que un patrón como "\n \w" no se interpretará y se puede escribir como r"\n \w" en lugar 
		de "\\n \\w" como sería lo correcto si omitimos el prefijo (r), lo que es mucho más fácil de leer.
		Cuando escribamos una expresión regular en este curso siempre usaremos el prefijo compuesto (ur):

		>> patron_regex = ur"Cadena de texto raw"

"""

texto_raw_unicode = [
	ur"El veloz murciélago hindú comía feliz cardillo y kiwi.\nLa cigüena tocaba el saxofón detrás del palenque de paja.",
	ur"El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.",
	ur"Exhíbanse politiquillos zafios,\ncon orejas kilométricas\n\ty unas de gavilán.",
	ur"—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!",
	ur"عـفقكلمنهوى",
	ur"\u0639\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649",
	ur"ᘹᙀᙁᙂᙃᙄᙅᙆᙇᙈᙉ",
	ur"\u1639\u1640\u1641\u1642\u1643\u1644\u1645\u1646\u1647\u1648\u1649",
]

print
print ">> IMPRIMIMOS CADENAS DE TEXTO RAW-UNICODE"
# Imprimimos estas cadenas a la consola directamente
for t in texto_raw_unicode:
	print t