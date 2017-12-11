#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MAGICA CONFIGURACIÓN DE CODECS SALIDA ----------------------
# FIX PARA WINDOWS CONSOLE, Usar: chcp 1252
import codecs,locale,sys
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
# ------------------------------------------------------------
""" EJEMPLOS DE USO DESDE LA TERMINAL

	Muestra la lista de palabras del "texto_original.txt":
	>> python limpiarTexto.py -f "texto2.txt" -n -m 1 -s "[^\w]" -r "\n"
	
	Corrije el formato de saltos de linea de un texto en una copia (variantes):
	>> python limpiarTexto.py -f "texto1.txt" -n -u -m 2 > "texto1_limpio.txt"
	>> python limpiarTexto.py -f "texto2.txt" -n -u -m 4 -j -s "(\-\-)" -r "—" > "texto2_limpio.txt"
	
	Separa todos los enunciados de un texto por lineas (variantes):
	>> python limpiarTexto.py -f "texto1.txt" -n -u -m 1 -e > "texto1_enunciados.txt"
	>> python limpiarTexto.py -f "texto2.txt" -n -u -m 1 -j -e -s "(\-\-)" -r "—" > "texto2_enunciados.txt"

python limpiarTexto.py -f .\test\txtFileRegEx_texto1.csv -s "\t(\w+)(?=\n\1(\t[^\n]+))" -r "\t\1\2" > .\test\txtFileRegEx_texto1x.csv
"""

# Importa las librerías
import re
import argparse

# Define los argumentos de usuario y la ayuda
parser = argparse.ArgumentParser(description=u'Este programa intenta rectificar los saltos de línea de un texto mal formateado y/o aplica un reemplazo regex definido por el usuario.\nEjemplo: python limpiarTexto.py -f "texto1.txt" -n -u -m 2 > "texto1_limpio.txt"')
parser.add_argument("-f", "--file", type=argparse.FileType('r'), required=True, help=u"Define el archivo de texto a procesar (REQUERIDO).")
parser.add_argument("-n", "--newline", help=u"Rectificar saltos de línea de un texto.", action="store_true")
parser.add_argument("-s", "--search", nargs='+', help=u"Cadena(s) de búsqueda REGEX definidas por el usuario.")
parser.add_argument("-r", "--replace", nargs='+', help=u"Cadena(s) de reemplazo REGEX definidas por el usuario.")
parser.add_argument("-j", "--join", help=u"Une dos líneas no vacías consecutivas con un espacio.", action="store_true")
parser.add_argument("-m", "--maxln", type=int, help=u"Define el máximo de líneas vacías consecutivas.")
parser.add_argument("-e", "--explode", help=u"Separa todos los enunciados con salto d línea.", action="store_true")
parser.add_argument("-u", "--utf8", help=u"Codificar la salida como UTF-8.", action="store_true")
args = parser.parse_args()

# Abre texto de entrada
if args.file:
	s = args.file.read().decode('utf-8')

# Elimina retorno de carro: \r
pattern = re.compile(ur'\r', re.UNICODE)
s = pattern.sub(ur'',s)

# Elimina caracteres invisibles en lineas vacias
pattern = re.compile(ur'\n[\t ]+\n', re.UNICODE)
s = pattern.sub(ur'\n\n',s)

# Clean text
if args.newline:
	# REGEX PARA ELIMINAR SALTOS DE LINEA: ([a-záéíóúüñ,])\n([¿¡«\(A-ZÁÉÍÓÚÜÑ]?[a-záéíóúüñ])

	pattern = re.compile(ur'([a-záéíóúüñ0-9,;\:\?!»]) ?\n([¿¡«\(A-ZÁÉÍÓÚÜÑ—]?[a-záéíóúüñ0-9\-])', re.UNICODE)
	s = pattern.sub(r'\1 \2',s)
	pattern = re.compile(ur'([A-ZÁÉÍÓÚÜÑa-záéíóúüñ0-9,;\?!»\.\:]) ?\n(([a-záéíóúüñ0-9,;\?!]))', re.UNICODE)
	s = pattern.sub(r'\1 \2',s)
	pattern = re.compile(ur'([a-záéíóúüñ0-9,;] ?)\n([—])', re.UNICODE)
	s = pattern.sub(r'\1\2',s)

# Separa todos los enunciados son salto d línea
if args.explode:
	pattern = re.compile(ur'([\:\?!»\)\.]) ?([¿¡«\(—]?[A-ZÁÉÍÓÚÜÑ])', re.UNICODE)
	s = pattern.sub(r'\1\n\2',s)

# USER REGEX search/replace
if args.search and args.replace:
	arse = args.search
	arre = args.replace
	for i in range(len(arse)):
		if not arre[i]:
			arre[i] = ""
		pattern = re.compile(arse[i].decode('utf-8'), re.UNICODE)
		s = pattern.sub(arre[i].decode('utf-8'),s)

# Une dos líneas no vacías
if args.join:
	pattern = re.compile(ur'([^\n])\n([^\n])', re.UNICODE)
	s = pattern.sub(r'\1 \2',s)

# Reduce saltos d linea consecutivos
if args.maxln:
	m = args.maxln
	pattern = re.compile(ur'[\n]{'+str(m+1)+',}', re.UNICODE)
	s = pattern.sub(r'\n'*m,s)

# Imprime texto de salida
if args.utf8:
	print s.encode('utf-8')
else:
	print s