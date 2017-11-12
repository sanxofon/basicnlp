#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FIX PARA WINDOWS CONSOLE ----------------------
import codecs,sys
sys.stdout = codecs.getwriter("utf8")(sys.stdout)
# -----------------------------------------------

import re
cadena = u"""—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!
El pingüino Wenceslao hizo kilómetros bajo exhaustiva 
lluvia y frío, añoraba a su querido cachorro."""
patrones = [
	(ur"(\w)", u"Busca todos los caracteres de palabra"),
	(ur"(\W)", u"Busca todos los caracteres que no son de palabra"),
	(ur"(\s)", u"Busca todos los caracteres de espaciado"),
	(ur"(\S)", u"Busca todos los caracteres que no son de espaciado"),
	(ur"(\w+)", u"Busca todas las palabras"),
	(ur"(\w+)\s+(\w+)", u"Busca pares de palabras separadas por un espacio"),
	(ur"([^\s]+)\s+([^\s]+)", u"Busca dos grupos de caracteres que no sean espacios seguidos, separados por un espacio"),
	(ur"(\w+)[^\w\s]?\s+[^\w\s]?(\w+)", u"Busca dos palabras separadas por un espacio que pueden o no tener un caractes no de palabra a los lados"),
	(ur"(\w+)\s+(?=(\w+))","Busca todos los pares de palabras (separadas por espacio) con lookahead"),
	(ur"(\w+)(?=(?:\s+(\W*)(\w+))|([^\w\r\n]+))","Busca pares de palabra/palabra o palabra/otro, puede incluir caracteres que anteceden la segunda palabra"),
]
print u"\nCadena:",cadena
for i,patron in enumerate(patrones):
	if (len(sys.argv)>1 and sys.argv[1]!=str(i)):
		continue
	paco = re.compile(patron[0], re.UNICODE)
	match = paco.findall(cadena)
	print "\n",patron[1]
	print "\t",patron[0],"\n"
	if len(match)>0:
		for ii,m in enumerate(match):
			if isinstance(match[0], tuple):
				m = filter(None, m) # Elimina los valores vacíos
				print ii,"\t", "\t".join(m)
			else:
				print ii,"\t", m
	else:
		print "\tNo hubo coincidencias"
print