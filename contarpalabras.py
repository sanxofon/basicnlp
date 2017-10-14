#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" EJEMPLOS DE USO DESDE LA TERMINAL

	Muestra la lista de palabras del "texto_original.txt" y lo guarda en una copia:
	>> python contarpalabras.py -f "texto_original.txt" > "texto_palabras.txt"
	
	Muestra frecuencia de conteos, ordena los resultados arfabeticamente, luego por frecuencia y lo guarda en una copia:
	>> python contarpalabras.py -f "texto.txt" -q -o af > "texto3.txt"

"""

# Importa las librerías
import re
import collections
import argparse

def toUnicode(s):
	if isinstance(s, str):
		return s.decode('utf-8')
	else:
		return s
 
parser = argparse.ArgumentParser(description=u'Este programa intenta contar la frecuencia de las palabras de un texto.')
# parser.add_argument("-h", "--help", help=u"Mostrar este mensaje y salir", action="store_true")
parser.add_argument("-f", "--file", type=argparse.FileType('r'), required=True, help=u"Define el archivo de texto a procesar (REQUERIDO)")
parser.add_argument("-i", "--interactive", help=u"Contar palabras interactivamente", action="store_true")
parser.add_argument("-q", "--freq", help=u"Mostrar frecuencia de conteos", action="store_true")
parser.add_argument("-o", "--ord", help=u"Ordenar contador: a:Alfabéticamente, f:Frecuencia")

args = parser.parse_args()

def pru(s):
	print (u'>> '+s).encode('utf-8')
# ORDER
ordena = None
if args.ord:
	ordena = args.ord.lower()
else:
	ordena = ''
# Contar palabras
contint = False
freq = False
# Mostrar frecuencia de conteos
if args.freq:
	freq = True
# Contar palabra interactivamente
if args.interactive:
	contint = True

s=args.file.read()
s = toUnicode(s)

pattern = re.compile(ur'(\w+)', re.UNICODE)

pals = pattern.findall(s.lower())
totpals = len(pals)

contador = collections.Counter(pals).items()
for c in xrange(len(ordena)):
	if ordena[c]=='a':
		contador = sorted(contador, key=lambda i: i[0]) # ordena alfabeticamente
	elif ordena[c]=='f':
		contador = sorted(contador, key=lambda i: i[1], reverse=True) # ordena por frecuencia

pru(u"Total palabras: "+str(totpals))
pru(u"Total diferentes: "+str(len(contador)))
if freq:
	print "-------"
	print "cnt\tfreq"
	cc = []
	for i,c in enumerate(contador):
		cc.append(c[1])
	ccc = collections.Counter(cc).items()
	ccc = sorted(ccc, key=lambda i: i[0])
	ccc = sorted(ccc, key=lambda i: i[1], reverse=True) 
	for c in ccc:
		print str(c[0])+"\t"+str(c[1])
if contint:
	print "-----------------"
	while (True):
		m = raw_input("Mostrar: ")
		if m=='':
			break
		print "-------"
		cm=0
		for i,c in enumerate(contador):
			if m[0]=="=":
				if c[1]!=int(m[1:]):
					continue
			elif m[0]==">":
				if c[1]<=int(m[1:]):
					continue
			elif m[0]=="<":
				if c[1]>=int(m[1:]):
					continue
			elif i>=int(m):
				break
			cm+=1
			print i+1,"-",toUnicode(c[0]),c[1]
		print "-------"
		pru(u"Total resultado: "+str(cm))
		pru(u"Total diferentes: "+str(len(contador)))
		pru(u"Total palabras: "+str(totpals))
else:
	print "-------"
	print "id\tpal\tfreq"
	for i,c in enumerate(contador):
		print str(i+1)+"\t"+c[0].encode('utf-8')+"\t"+str(c[1])

#"""