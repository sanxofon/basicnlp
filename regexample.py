#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import argparse

# Define los argumentos de usuario y la ayuda
parser = argparse.ArgumentParser(description=u'Ejecutar expresiones regulares sobre un archivo de texto')
parser.add_argument("-f", "--file", type=argparse.FileType('r'), required=True, help=u"Define el archivo de texto a procesar (REQUERIDO).")
args = parser.parse_args()

# Abre texto de entrada
if args.file:
	cadena = args.file.read().decode('utf-8')

patron = ur"([\w]+) ([\w]+)"

match = re.findall(patron, cadena, re.UNICODE)
print u"Coincidencias:"
for m in match:
	print "\t", " ".join(m)

