#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
"""
	USO:
python reduce2grams.py -f muchos_textos_2gramx.csv

"""
import datetime

# FIX PARA WINDOWS CONSOLE, Usar: chcp 1252
import codecs,locale,sys

# Json out
import json

# Importamos la librería de expresiones regulares (re)
import re
# Importamos la librería "argparse" que nos permite acceder de forma ordenada a los argumentos
# además de generar un texto de ayuda cuando ejecutamos: "python argumentosParsed.py -h"
import argparse

# Inicializamos el "parser" de argumentos con la descripción general
parser = argparse.ArgumentParser(description=u"Este programa cuenta la frecuencia de una lista de 2gramas.")
parser.add_argument("-f", "--fil", type=argparse.FileType('r'), required=True, help=u"Define el archivo de 2gramas a procesar.")
parser.add_argument("-u", "--utf", help=u"Forzar salida UTF-8.", action="store_true")
args = parser.parse_args()

# MAGICA CONFIGURACIÓN DE CODECS SALIDA ----------------------
# FIX PARA WINDOWS CONSOLE, Usar: chcp 1252
import codecs,locale,sys
if args.utf:
	sys.stdout = codecs.getwriter("utf8")(sys.stdout)
else:
	sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

# Definimos la cadena sobre la que vamos a trabajar a partir del archvo de texto texto
cadena = args.fil.read().decode('utf-8')

# Elimina retorno de carro: \r (windows files)
reca = re.compile(ur'\r', re.UNICODE)
cadena = reca.sub(ur'',cadena)

# Separa la cadena por saltos de linea
lista = cadena.split("\n")

# Recorremos la lista, linea por linea
ml = ""
cl = len(lista)
grams = {}
for i,l in enumerate(lista):
	while True:
		l = re.sub(ur'\t{3}','',l)
		if l==ml:
			break
		ml = l
	l = l.split("\t")
	p1 = l[0]
	p2 = l[len(l)-1]
	l = l[1:-1]
	l = "\t".join(l)
	if l in grams.keys():
		grams[l][0] += 1
		if len(grams[l][1])<10:
			grams[l][1].append((p1,p2))
	else:
		grams[l] = [1,[(p1,p2)]]
	print(cl-i," "*10, end='\r')

	# if i>10000:
	# 	break

# Abrimos archivos de 2gramas
with open("2gramas.json","r") as jsonfile:
	gramsx = json.load(jsonfile)

gramso = {}
for g in gramsx:
	gramso[g[0]] = g[1]

for l in gramso.keys():
	if l in grams.keys():
		grams[l][0] += gramso[l][0]
		grams[l][1] = grams[l][1]+gramso[l][1]
	else:
		grams[l] = gramso[l]

grams = sorted(grams.items(), key=lambda x: x[1], reverse=True)


# Guardamos cambios a la lista de patrones definidos
with open("2gramas.json","w") as jsonfile:
	json.dump(grams,jsonfile)