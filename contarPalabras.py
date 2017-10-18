#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" EJEMPLOS DE USO DESDE LA TERMINAL

	Muestra la lista de palabras del "texto_original.txt" y lo guarda en una copia:
	>> python contarPalabras.py -f "texto2.txt" > "texto2_palabras.txt"
	
	Muestra frecuencia de conteos, ordena los resultados arfabeticamente, luego por frecuencia y lo guarda en una copia:
	>> python contarPalabras.py -f "texto1.txt" -q -o af > "texto1_palabras.txt"

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
 
parser = argparse.ArgumentParser(description=u'Este programa intenta contar la frecuencia de las palabras de un texto.\nEjemplo: python contarPalabras.py -f texto1.txt -o aF -i')
parser.add_argument("-f", "--file", type=argparse.FileType('r'), required=True, help=u"Define el archivo de texto a procesar (REQUERIDO).")
parser.add_argument("-o", "--ord", help=u"Ordenar contador: a:Alfabéticamente, f:Frecuencia (Mayúscula=Reversa).")
parser.add_argument("-i", "--interactive", help=u"Contar palabras, consulta interactiva.", action="store_true")
parser.add_argument("-q", "--freq", help=u"Mostrar frecuencia de conteos.", action="store_true")
parser.add_argument("-u", "--utf8", help=u"Codificar la salida como UTF-8.", action="store_true")

args = parser.parse_args()

utf8 = False
if args.utf8:
	utf8 = True


def pru(s):
	global utf8
	if utf8:
		print (u'>> '+s).encode('utf-8')
	else:
		print (u'>> '+s)
	
# ORDER
ordena = None
if args.ord:
	ordena = args.ord
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
	elif ordena[c]=='A':
		contador = sorted(contador, key=lambda i: i[0], reverse=True) # ordena alfabeticamente
	elif ordena[c]=='f':
		contador = sorted(contador, key=lambda i: i[1]) # ordena por frecuencia
	elif ordena[c]=='F':
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
			print i+1,"-",toUnicode(c[0]),c[1] # Siempre salida unicode dado que se trabaja en consola
		print "-------"
		pru(u"Total resultado: "+str(cm))
		pru(u"Total diferentes: "+str(len(contador)))
		pru(u"Total palabras: "+str(totpals))
else:
	print "-------"
	print "id\tfreq\tpal"
	for i,c in enumerate(contador):
		if utf8:
			print str(i+1)+"\t"+str(c[1])+"\t"+c[0].encode('utf-8')
		else:
			print str(i+1)+"\t"+str(c[1])+"\t"+c[0]

#"""