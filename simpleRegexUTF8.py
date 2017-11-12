#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Este script muestra como realizar búsquedas y reemplazos 
	de cadenas de texto mediante Expresiones Regulares (REGEX)
	utilizando caracteres Unicode.

	>> python simpleRegexUTF8.py
"""

# La librería "re" nos permite realizar expresiones regulares en Python
import re

# Siempre que definamos una cadena en código lo haremos con el prefijo (u)
cadena = u"—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!"

# Siempre que definamos un patrón REGEX en código lo haremos con el prefijo (ur)
# Este patrón busca dos palabras separadas por solamente por un espacio
patron = ur"([\w]+) ([\w]+)"



"""
Buscar coincidencias de una cadena

	La librería "re" tiene varios métodos que podemos usar, y para probar si una expresión 
	regular coincide con una cadena específica en Python, puede usar "re.search()". 
	Este método devuelve "None" si el patrón no coincide, o un "re.MatchObject" con información 
	adicional sobre qué parte de la cadena se encontró.

	Tengan en cuenta que este método se detiene después de la primera coincidencia, 
	por lo que es más adecuado para probar una expresión regular más que extraer datos.

	>> re.search(pattern, input_str, flags=0)

	Algunos FLAGS importantes son:

	    re.UNICODE
	    re.IGNORECASE
	    re.MULTILINE
	    re.DOTALL

"""

print u">> RE.SEARCH"
# Buscamos el "patron" en la "cadena"
match = re.search(patron, cadena)
if match:
	print u"Coincidencia en el índice %s, %s" % (match.start(), match.end())
	print u"Grupos:"
	for g in match.groups():
		print "\t",g


"""
Capturar todas las coincidencias de una cadena

	A diferencia del método "re.search()"" anterior, podemos usar "re.findall()"" para realizar 
	una búsqueda global sobre toda la cadena de entrada. 

	Si hay grupos de captura en el patrón, entonces devolverá una lista de todos los casos 
	capturados (lista de tuples), de lo contrario, simplemente devolverá una lista de los 
	mismos, o una lista vacía si no se encuentran coincidencias.

	>> re.findall(pattern, input_str, flags=0)
"""

print
print u">> RE.FINDALL"
# Buscamos TODAS las coincdencias del "patron" en la "cadena"
match = re.findall(patron, cadena)
print u"Coincidencias:"
for m in match:
	print "\t", " ".join(m)

# Buscamos TODAS las coincdencias del "patron" en la "cadena" CON LA BANDERA UNICODE
match = re.findall(patron, cadena, re.UNICODE)
print u"Coincidencias Unicode:"
for m in match:
	print "\t", " ".join(m)


"""
Encontrar y reemplazar cadenas

	Otra tarea común es buscar y reemplazar una parte de una cadena utilizando expresiones regulares.
	Por ejemplo, para el orden de algún texto. Puedes hacer esto en Python con el método "re.sub()"

	El argumento de opcional "count" es el número máximo de reemplazos que se deberán realizar, 
	y si este es el valor menor o igual a cero, entonces se reemplazan todas las coincidencias en la cadena.

	>> re.sub(pattern, replacement_pattern, input_str, count, flags=0)
"""

print
print u">> RE.SUB"
# Definimos un patron de reemplazo que invierte el orden de las palabras
patron_reemplazo = ur"\2 \1"

# Reemplazamos "patron" por "patron_reemplazo" en la "cadena" y guardamos el resultado en "cadena_resultado"
cadena_resultado = re.sub(patron, patron_reemplazo, cadena)

# Reemplazamos "patron" por "patron_reemplazo" en la "cadena" y guardamos el resultado en "cadena_resultado" CON LA BADERA UNICODE
cadena_resultado_unicode = re.sub(patron, patron_reemplazo, cadena, 0, re.UNICODE)

#Imprimimos "cadena" original
print u"Original:", "\t", cadena

#Imprimimos "cadena_resultado"
print u"Resultado:", "\t", cadena_resultado

#Imprimimos "cadena_resultado"
print u"Unicode:", "\t",cadena_resultado_unicode


"""
Compilar patrones de búsqueda

	En Python, crear un nuevo patrón de expresión regular para que coincida con muchas cadenas puede ser lento, 
	por lo que se recomienda compilarlos si necesita probar o extraer información de muchas cadenas de entrada 
	utilizando la misma expresión. Este método devuelve un "re.RegexObject".

	>> regexObject = re.compile(pattern, flags=0)

	El objeto devuelto tiene exactamente los mismos métodos que los anteriores, 
	excepto que ya no requieren el patrón ni las banderas para cada llamada.
"""

print
print u">> RE.COMPILE"
# Compilamos el patrón de búsqueda
patron_compilado = re.compile(patron, re.UNICODE)

print "search:"
# Usamos el objeto "patron_compilado" para buscar (search)
match = patron_compilado.search(cadena)
if match:
    print "\t", match.start(), match.end()

print "findall:"
# Usamos el objeto "patron_compilado" para encontrar todos las coincidencias (findall)
for m in patron_compilado.findall(cadena):
    print "\t", " ".join(m)
    
print "sub:"
# Usamos el objeto "patron_compilado" para reemplazar "patron" por "patron_reemplazo" en "cadena" (sub)
print "\t", patron_compilado.sub(patron_reemplazo, cadena)
