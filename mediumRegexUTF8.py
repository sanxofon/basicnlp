#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FIX PARA WINDOWS CONSOLE ----------------------
# Usar: chcp 1252
import codecs,locale,sys
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
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
	(ur"(\w+)(?=(?:([^\r\n\S]+)(\W*)(\w+))|([^\w\s]+)(\s+)?(\w+)?)","Busca pares de palabra/palabra o palabra/otro, puede incluir caracteres o separadores entre la primera y la segunda palabra"),
]
print "\n",u"Cadena:",cadena,"\n"
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
				print ii,"\t", "\t".join([re.sub(r'\n',r'\\n',re.sub(r'\t',r'\\t',x)) for x in m])
			else:
				print ii,"x\t", re.sub(r'\n',r'\\n',re.sub(r'\t',r'\\t',m))
	else:
		print "\t"+u"No hubo coincidencias"
print