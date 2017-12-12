#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FIX PARA WINDOWS CONSOLE, Usar: chcp 1252
import codecs,locale,sys

# Json out
import json

# Importamos la librería de expresiones regulares (re)
import re
# Importamos la librería "argparse" que nos permite acceder de forma ordenada a los argumentos
# además de generar un texto de ayuda cuando ejecutamos: "python argumentosParsed.py -h"
import argparse

"""
	EJEMPLO WINDOWS:
python .\txtFileRegEx.py -u -f .\test\texto1.txt -i 9 > .\test\txtFileRegEx_texto1_2gramx.csv
python .\txtFileRegEx.py -u -f .\test\txtFileRegEx_texto1_2gramx.csv -s "\t(\w+)(?=\t*\n\1(\t[^\n]+))" -r "\t\1\2" > .\test\txtFileRegEx_texto1_3gramx.csv
python .\txtFileRegEx.py -u -f .\test\txtFileRegEx_texto1_3gramx.csv -s "\t(\w+)(?=\t*\n[^\n]+\n\1(\t[^\n]+))" -r "\t\1\2" > .\test\txtFileRegEx_texto1_5gramx.csv
python .\txtFileRegEx.py -u -f .\test\txtFileRegEx_texto1_5gramx.csv -s "(?:_|\\n|\t|\W)+\t(\w+)\t+\n" -r "\n" > .\test\txtFileRegEx_texto1_4gramx.csv

python .\txtFileRegEx.py -u -f .\test\txtFileRegEx_texto1_2gramx.csv -s "([\t\n]\w+)\t{3}" -r "\1" -o > .\test\txtFileRegEx_texto1_2gram.csv
python .\txtFileRegEx.py -u -f .\test\txtFileRegEx_texto1_3gramx.csv -s "([\t\n]\w+)\t{3}" -r "\1" -o > .\test\txtFileRegEx_texto1_3gram.csv
python .\txtFileRegEx.py -u -f .\test\txtFileRegEx_texto1_4gramx.csv -s "([\t\n]\w+)\t{3}" -r "\1" -o > .\test\txtFileRegEx_texto1_4gram.csv
python .\txtFileRegEx.py -u -f .\test\txtFileRegEx_texto1_5gramx.csv -s "([\t\n]\w+)\t{3}" -r "\1" -o > .\test\txtFileRegEx_texto1_5gram.csv
rm .\test\txtFileRegEx_texto1_2gramx.csv .\test\txtFileRegEx_texto1_3gramx.csv .\test\txtFileRegEx_texto1_4gramx.csv .\test\txtFileRegEx_texto1_5gramx.csv

"""


# Definimos una lista de patrones RegEx
# Cada elemento de la lista es una sublista de dos elementos
# el primer elemento [0] es els patrón RegEx
# el segundo elemento [1] es una descripción de lo que hace
# patrones = [
# 	(ur"(\w)",u"Busca todos los caracteres de palabra"),
# 	(ur"(\W)",u"Busca todos los caracteres que no son de palabra"),
# 	(ur"(\s)",u"Busca todos los caracteres de espaciado"),
# 	(ur"(\S)",u"Busca todos los caracteres que no son de espaciado"),
# 	(ur"(\w+)",u"Busca todas las palabras"),
# 	(ur"(\w+)\s+(\w+)",u"Busca pares de palabras separadas por un espacio"),
# 	(ur"([^\s]+)\s+([^\s]+)",u"Busca dos grupos de caracteres que no sean espacios seguidos, separados por un espacio"),
# 	(ur"(\w+)\s+(?=(\w+))",u"Busca todos los pares de palabras (separadas por espacio) con lookahead"),
# 	(ur"(\w+)(?=(?:(\s+)([^\w\s]+)?(\w+))|([^\w\s]+)(\s+)?(\w+))",u"Busca pares de palabras, con o sin separador/signo o signo/separador entre ambas"),
# ]
# Abre la lista de patrones definidos
with open("patrones.json","r") as jsonfile:
	patrones = json.load(jsonfile)

# Inicializamos el "parser" de argumentos con la descripción general
parser = argparse.ArgumentParser(description=u"Este programa permite ejecutar una expresión regular sobre un archivo de texto.")
parser.add_argument("-f", "--fil", type=argparse.FileType('r'), help=u"Define el archivo de texto a procesar.")
parser.add_argument("-i", "--ind", type=int, help=u"Define el índice de RegEx a ejecutar.")
parser.add_argument("-e", "--emp", help=u"Elimina resultados vacíos.", action="store_true")
parser.add_argument("-l", "--lis", help=u"Muestra un listado con los patrones RegEx definidos.", action="store_true")
parser.add_argument("-v", "--ver", help=u"Verbose. Muestra más datos en la salida.", action="store_true")
parser.add_argument("-s", "--search", help=u"Cadena de búsqueda REGEX definidas por el usuario.")
parser.add_argument("-r", "--replace", help=u"Cadena de reemplazo REGEX definidas por el usuario.")
parser.add_argument("-a", "--append", help=u"Descripción del REGEX para agregarlo a los patrones predefinidos.")
parser.add_argument("-o", "--recursive", help=u"El reemplazo REGEX se aplicará recursivamente.", action="store_true")
parser.add_argument("-u", "--utf", help=u"Forzar salida UTF-8.", action="store_true")
args = parser.parse_args()

# MAGICA CONFIGURACIÓN DE CODECS SALIDA ----------------------
# FIX PARA WINDOWS CONSOLE, Usar: chcp 1252
import codecs,locale,sys
if args.utf:
	sys.stdout = codecs.getwriter("utf8")(sys.stdout)
else:
	sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

# ------------------------------------------------------------

# Se recibió solucitud de listado de patrones RegEx
if args.lis:
	# Imprime una lista con los patrones definidos
	print "La lista de patrones RegEx definidos es:\n\t"+"\n\t".join([str(i+1)+". "+x[1] for i,x in enumerate(patrones)])

# Se recibió archivo e índice de patrón RegEx
elif args.fil:

	# Definimos la cadena sobre la que vamos a trabajar a partir del archvo de texto texto
	cadena = args.fil.read().decode('utf-8')

	# Elimina retorno de carro: \r (windows files)
	reca = re.compile(ur'\r', re.UNICODE)
	cadena = reca.sub(ur'',cadena)
	

	# Define patron de busqueda y  reemplazo definido por el usuario
	arse = None
	if args.ind:
		# Si recibimos índice de patrón, definimos a partir de eso
		indice = int(args.ind)-1
	elif args.search:
		# Si recibimos un patrón de búsqueda definido por el usuario
		indice = len(patrones)
		if args.append:
			a = args.append.decode('utf-8')
			patrones.append((args.search.decode('utf-8'),a))
			# Guardar cambios a la lista de patrones definidos
			with open("patrones.json","w") as jsonfile:
				json.dump(patrones,jsonfile)
			if args.ver:
				# Imprimimos la descripción del patrón agregado
				print u"\tPatrón agregado:",patrones[indice][1]
		else:
			patrones.append((args.search.decode('utf-8'),u"Patrón definido por el usuario."))
	else:
		sys.exit(u"No se recibió patrón de búsqueda o índice.\nPuedo mostrar más ayuda con:\n\tpython txtFileRegEx.py -h\nPuedo mostrar la lista de patrones RegEx definidos con:\n\tpython txtFileRegEx.py -l")

	# Compila el patrón elegido
	arse = re.compile(patrones[indice][0], re.UNICODE)

	# Imprimimos la cadena definida tal cual
	# if args.ver:
	# 	print "\n",u"Cadena:",cadena

	if args.ver:
		# Imprimimos la descripción "patron[1]"
		print u"\tDescripción:",patrones[indice][1]
		# Imprimimos el patrón RegEx "patron[0]"
		print u"\tPatrón:",patrones[indice][0],"\n"

	# Asigna el patrón de reemplazo si está definido por el usuario
	arre = None
	if args.replace:
		arre = args.replace.decode('utf-8')
		recursive = 0
		if args.recursive:
			recursive = 1
		if args.ver:
			# Imprimimos la descripción reemplazo
			print u"\tPatrón de reemplazo:",arre,"\n"
		cadenaMem = ""
		while True:
			cadena = arse.sub(arre,cadena)
			if cadena == cadenaMem or recursive<1:
				break
			cadenaMem = cadena
		print cadena

	else:
		# Usamos la función "findall" para encontrar todas la coincidencias en la cadena
		# La variable "match" guardará la lista de todas las coincidencias encontradas
		match = arse.findall(cadena)

		# Nos fijamos si se encontró algo, es decir, si el tamaño de la lista en mayor que 0
		if len(match)>0:

			# Recorremos la lista de coincidencias encontradas
			for ii,m in enumerate(match):

				# Nos fijamos si el tipo de resultado es un tuple, o sea que contiene varias cadenas (varios grupos)
				if isinstance(m, tuple):

					# Elimina los valores vacíos de una lista o tuple, la función "filter" hace eso
					if args.emp:
						m = filter(None, m)

					# El re.sub un poco confuso es simplemente para "escapar" los caracteres de salto de línea y tabulación
					# Además uso un "join" para unir la lista de cadenas que trae el tuple m
					mm = "\t".join([re.sub(r'\n',r'\\n',re.sub(r'\t',r'\\t',re.sub(r' ',r'_',x))) for x in m])
					if args.ver:
						print ii,"\t", mm
					else:
						print mm
					# La vesión simplificada sería
					# print ii,"\t", "\t".join(m)

				# En caso contrario es una cadena (un sólo grupo) así que simplemente la imprimimos
				else:

					# El mismo re.sub de arriba...
					mm = re.sub(r'\n',r'\\n',re.sub(r'\t',r'\\t',re.sub(r' ',r'_',m)))
					if args.ver:
						print ii,"\t", mm
					else:
						print mm
					# La vesión simplificada sería
					# print ii,"\t", m

		# Caso contrario avisamos que no hubo coincidencias
		elif args.ver:
			print "\t",u"No hubo coincidencias"

# Salida cuando no se recibieron argumentos mínimos
else:
	sys.exit(u"No se recibió archivo o índice.\nPuedo mostrar más ayuda con:\n\tpython txtFileRegEx.py -h\nPuedo mostrar la lista de patrones RegEx definidos con:\n\tpython txtFileRegEx.py -l")