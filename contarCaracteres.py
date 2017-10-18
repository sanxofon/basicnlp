#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" EJEMPLOS DE USO DESDE LA TERMINAL

    Muestra la lista de caracteres del "texto_original.txt" y lo guarda en una copia:
    >> python contarCaracteres.py -f "test/texto2.txt" -u > "test/texto2_caracteres.txt"
    
    Muestra frecuencia de conteos, ordena los resultados alfabeticamente, luego por frecuencia y lo guarda en una copia:
    >> python contarCaracteres.py -f "test/texto1.txt" -q -o af -u > "test/texto1_caracteres.txt"

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

def addslashes(s):
    ech = [
        ("\r","\\r"),
        ("\n","\\n"),
        ("\t","\\t"),
    ]
    for e in ech:
        if e[0] in s:
            s = s.replace(e[0], e[1])
    return s
 
parser = argparse.ArgumentParser(description=u'Este programa intenta contar la frecuencia de las caracteres de un texto.\nEjemplo: python contarCaracteres.py -f texto1.txt -o aF -i')
parser.add_argument("-f", "--file", type=argparse.FileType('r'), required=True, help=u"Define el archivo de texto a procesar (REQUERIDO).")
parser.add_argument("-o", "--ord", help=u"Ordenar contador: a:Alfabéticamente, f:Frecuencia (Mayúscula=Reversa).")
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

# Mostrar frecuencia de conteos
freq = False
if args.freq:
    freq = True

s=args.file.read()
s = toUnicode(s)

pattern = re.compile(ur'(.)', re.UNICODE | re.DOTALL)

chars = pattern.findall(s.lower())
totchars = len(chars)

contador = collections.Counter(chars).items()
for c in xrange(len(ordena)):
    if ordena[c]=='a':
        contador = sorted(contador, key=lambda i: i[0]) # ordena alfabeticamente
    elif ordena[c]=='A':
        contador = sorted(contador, key=lambda i: i[0], reverse=True) # ordena alfabeticamente
    elif ordena[c]=='f':
        contador = sorted(contador, key=lambda i: i[1]) # ordena por frecuencia
    elif ordena[c]=='F':
        contador = sorted(contador, key=lambda i: i[1], reverse=True) # ordena por frecuencia

pru(u"Total caracteres: "+str(totchars))
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

print "-------"
print "id\tfreq\tpal\trepr"
for i,c in enumerate(contador):
    if utf8:
        print str(i+1)+"\t"+str(c[1])+"\t"+addslashes(c[0].encode('utf-8'))+"\t"+repr(c[0].encode('utf-8'))
    else:
        print str(i+1)+"\t"+str(c[1])+"\t"+addslashes(c[0])+"\t"+repr(c[0])
