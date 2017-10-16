#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Una manera más eficaz para capurar varios argumentos con beneficios añadidos
	es usar la librería especial para ese fin: "argparse"
	Ejemplos de ejecución:
	>> python argumentosParsed.py -n "Santiago Chávez"
	>> python argumentosParsed.py -n "Santiago Chávez" -e
"""

# Importamos la librería "argparse" que nos permite acceder de forma ordenada a los argumentos
# además de generar un texto de ayuda cuando ejecutamos: "python argumentosParsed.py -h"
import argparse

# La librería "sys" no permite acceder a información del sistema
import sys

# Inicializamos el "parser" de argumentos con la descripción general
parser = argparse.ArgumentParser(description=u'Este programa muestra como recibir datos del usuario como argumentos\nEjemplo: python argumentosParsed.py -n "Santiago Chávez"')

# Define la "bandera" de nombre (corta: "-n", larga: "-name") y su texto de ayuda (help=""). Es un argumento obligatorio (required=True)
parser.add_argument("-n", "--name", help=u"Nombre del usuario", required=True)

# Define la bandera booleana extra (corta: "-e", larga: "-extra"). BOOLEANO: no recibe valores extra (action="store_true")
parser.add_argument("-e", "--extra", help=u"Extra: Booleano, no recibe valor", action="store_true")

# Finalizamos el proceso de parceo, guardamos los argumentos en la variable "args"
args = parser.parse_args()

name = args.name.decode(sys.stdin.encoding)

extra = "No"
if args.extra:
	extra = "Si"

# Por último imprimimos el argumento "name" recibido
print u"Argumentos recibidos:"
print "\tNombre: ",name
print "\tExtra: ",extra