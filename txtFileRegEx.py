#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MAGICA CONFIGURACIÓN DE CODECS SALIDA ----------------------
# FIX PARA WINDOWS CONSOLE, Usar: chcp 1252
import codecs,locale,sys
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
# ------------------------------------------------------------
# Importamos la librería de expresiones regulares (re)
import re
# Importamos la librería "argparse" que nos permite acceder de forma ordenada a los argumentos
# además de generar un texto de ayuda cuando ejecutamos: "python argumentosParsed.py -h"
import argparse



# Definimos una lista de patrones RegEx
# Cada elemento de la lista es un "tuple" de dos elementos
# el primer elemento [0] es el patrón RegEx
# el segundo elemento [1] es una descripción de lo que hace
patrones = [
	(ur"(\w)", u"Busca todos los caracteres de palabra"),
	(ur"(\W)", u"Busca todos los caracteres que no son de palabra"),
	(ur"(\s)", u"Busca todos los caracteres de espaciado"),
	(ur"(\S)", u"Busca todos los caracteres que no son de espaciado"),
	(ur"(\w+)", u"Busca todas las palabras"),
	(ur"(\w+)\s+(\w+)", u"Busca pares de palabras separadas por un espacio"),
	(ur"([^\s]+)\s+([^\s]+)", u"Busca dos grupos de caracteres que no sean espacios seguidos, separados por un espacio"),
	(ur"(\w+)[^\w\s]?\s+[^\w\s]?(\w+)", u"Busca dos palabras separadas por un espacio que pueden o no tener un caractes no de palabra a los lados"),
	(ur"(\w+)\s+(?=(\w+))", u"Busca todos los pares de palabras (separadas por espacio) con lookahead"),
	(ur"(\w+)(?=(?:([^\r\n\S]+)(\W*)(\w+))|([^\w\s]+)(\s+)?(\w+)?)", u"Busca pares de palabra/palabra o palabra/otro(s)/palabra, puede incluir caracteres o separadores entre la primera y la segunda palabra"),
]



# Inicializamos el "parser" de argumentos con la descripción general
parser = argparse.ArgumentParser(description=u"""
Este programa permite ejecutar una expresión regular sobre un archivo de texto.
La lista de patrones RegEx definidos es:"""+"\n".join([x[1] fox x in patrones])+"""
""")
parser.add_argument("-f", "--file", type=argparse.FileType('r'), required=True, help=u"Define el archivo de texto a procesar (REQUERIDO).")
parser.add_argument("-n", "--newline", help=u"Rectificar saltos de línea de un texto.", action="store_true")
parser.add_argument("-i", "--index", type=int, required=True, help=u"Define el índice de RegEx a ejecutar.")





# Definimos la cadena sobre la que vamos a trabajar a partir del archvo de texto texto
if args.file:
	cadena = args.file.read().decode('utf-8')

# Imprimimos la cadena definida tal cual
print "\n",u"Cadena:",cadena
print "\n",u"Número de patrones RegEx: ", len(patrones),"\n"

# Recorremos un loop de la lista de (patrones, descripciones)
for i,patron in enumerate(patrones):
	# En cada paso del loop, la variable "i" va aumentanto: 0, 1, 2, 3...
	# 	hasta el número total de patrones menos uno (ya que el primero es 0)
	# En cada paso la variable "patron" contiene un tuple con el patrón [0] y la descripción [1]

	# Este es un hack que permite ejecutar el archivo enviando un argumento
	# El argumento es el número de patrón a ejecutar (para no ejecutar todos)
	# Para usarlo corremos el programa de la siguiente forma:
	#    $ python mediumRegexUTF8.py 4
	# En el ejemplo anterior se ejecutaría solamente el patrón número 5 (que tiene el índice [4]): (ur"(\w+)", u"Busca todas las palabras")
	if (len(sys.argv)>1 and sys.argv[1]!=str(i)):
		continue

	# Imprimimos la descrpción "patron[1]"
	print "\n",patron[1]
	# Imprimimos el patrón RegEx "patron[0]"
	print "\t",patron[0],"\n"


	# Como mostramos en el archivo simpleRegexUTF8, se puede compilar un patrón antes de ejecutarlo
	# "paco" será un objeto que puede ejecutar todas las funciones regex sobre cualquier cadena y
	#     no es necesario volver a definir el patrón cada vez
	paco = re.compile(patron[0], re.UNICODE)

	# Usamos la función "findall" para encontrar todas la coincidencias en la cadena
	# La variable "match" guardará la lista de todas las coincidencias encontradas
	match = paco.findall(cadena)

	# Nos fijamos si se encontró algo, es decir, si el tamaño de la lista en mayor que 0
	if len(match)>0:

		# Recorremos la lista de coincidencias encontradas
		for ii,m in enumerate(match):

			# Nos fijamos si el tipo de resultado es un tuple, o sea que contiene varias cadenas (varios grupos)
			if isinstance(m, tuple):

				# Elimina los valores vacíos de una lista o tuple, la función "filter" hace eso
				m = filter(None, m)

				# El re.sub un poco confuso es simplemente para "escapar" los caracteres de salto de línea y tabulación
				# Además uso un "join" para unir la lista de cadenas que trae el tuple m
				print ii,"\t", "\t".join([re.sub(r'\n',r'\\n',re.sub(r'\t',r'\\t',x)) for x in m])
				# La vesión simplificada sería
				# print ii,"\t", "\t".join(m)

			# En caso contrario es una cadena (un sólo grupo) así que simplemente la imprimimos
			else:

				# El mismo re.sub de arriba...
				print ii,"\t", re.sub(r'\n',r'\\n',re.sub(r'\t',r'\\t',m))
				# La vesión simplificada sería
				# print ii,"\t", m

	# Caso contrario avisamos que no hubo coincidencias
	else:
		print "\t",u"No hubo coincidencias"

# Por elegancia en la salida imprimimos un salto de line al final
print