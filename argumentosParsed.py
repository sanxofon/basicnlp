#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Una manera más eficaz para capurar varios argumentos con beneficios añadidos
	es usar la librería especial para ese fin: "argparse"
	Ejemplos de ejecución:
	>> python argumentosParsed.py -a "Santiago Chávez"
	>> python argumentosParsed.py -a "Santiago Chávez" -m
	>> python argumentosParsed.py -a "Santiago Chávez" -M
	Este ejemplo debe mostrar error de codificación en Windows
	>> python argumentosParsed.py -a "Santiago Chávez" -M > test,txt
"""

# Importamos la librería "argparse" que nos permite acceder de forma ordenada a los argumentos
# además de generar un texto de ayuda cuando ejecutamos: "python argumentosParsed.py -h"
import argparse

# La librería "sys" no permite acceder a información del sistema
import sys

# Inicializamos el "parser" de argumentos con la descripción general
parser = argparse.ArgumentParser(description=u'Este programa muestra como recibir datos del usuario como argumentos\nEjemplo: python argumentosParsed.py -n "Santiago Chávez"')

# Define la "bandera" de nombre (corta: "-a", larga: "-arg") y su texto de ayuda (help=""). Es un argumento obligatorio (required=True)
parser.add_argument("-a", "--arg", help=u"Argumento, acepta una cadena de texto", required=True)

# Define la bandera booleana de convertir a minúsculas (corta: "-m", larga: "-min"). BOOLEANO: no recibe valores extra (action="store_true")
parser.add_argument("-m", "--min", help=u"Convertir a minúsculas: Booleano, no recibe valor", action="store_true")

# Define la bandera booleana de convertir a MAYÚSCULAS (corta: "-M", larga: "-may"). BOOLEANO: no recibe valores extra (action="store_true")
parser.add_argument("-M", "--may", help=u"Convertir a MAYÚSCULAS: Booleano, no recibe valor", action="store_true")

# Finalizamos el proceso de parceo, guardamos los argumentos en la variable "args"
args = parser.parse_args()

# Codificación (encoding) del sistema (terminal)
cds = sys.stdin.encoding
print u"Encoding:",cds
arg = args.arg.decode(cds)

# Por último imprimimos el argumento "name" recibido
print u"Argumentos recibidos:"
print u"\tArgumento:",arg
if args.min:
	print u"\tminúsculas:",arg.lower()
if args.may:
	print u"\tMAYÚSCULAS:",arg.upper()