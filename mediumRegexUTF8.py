#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
cadena = u"—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!"
patrones = [
	ur"([\w]+)",
	ur"([\w]+) ([\w]+)",
	ur"([^ ]+) ([^ ]+)",
	ur"([\w]+)[^\w]? [^\w]?([\w]+)",
]
print u"\nCadena:",cadena
for patron in patrones:
	paco = re.compile(patron, re.UNICODE)
	match = paco.findall(cadena)
	print u"\nPatrón:",patron
	if len(match)>0:
		if isinstance(match[0], tuple):
			for m in match:
				print "\t", "\t".join(m)
		else:
			print  "\t", "\n\t".join(match)
	else:
		print "\tNo hubo coincidencias"
print