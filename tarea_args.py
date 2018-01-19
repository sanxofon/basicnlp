#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, locale, codecs, sys, re

#sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

parser = argparse.ArgumentParser(description=u'TAREA -- Un programa que reciba dos argumentos: 1) Cadena y 2) Patrón de búsqueda en REGEX y que busque el patrón en la cadena')
parser.add_argument("-t", "--texto", help=u"Ingrese una cadena de texto", required=True)
parser.add_argument("-b", "--busqueda", help=u"Ingrese el patrón de búsqueda para la cadena de texto", required=True)

args = parser.parse_args()

cadena = args.texto
patron = args.busqueda

print

if cadena:
	match = re.findall(patron, cadena, re.UNICODE|re.IGNORECASE)
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
print

#Hacer un programa que reciba dos argumentos: 
#uno que sea una expresión regular (patrón de búsqueda) y el otro la cadena (lugar de búsqueda). 