#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tipos de variables y constantes
"""

# Números

# Enteros -n, ...,-1, 0, 1,..., n
entero = 5

# Si tengo una cadena u otra cosa y quiero convertirla a entero
cadena = "5"
entero = int(cadena)

# Comprobar si una variable es un entero
if isinstance(cadena, int):
	print cadena, "Es entero"
else:
	print cadena, "No es entero"

if isinstance(entero, int):
	print entero, "Es entero"
else:
	print entero, "No es entero"

# Racionales: 0.5, 0,6534, etc
flotante = 5.0982319237

# Si tengo una cadena u otra cosa y quiero convertirla a entero
cadena = "5.0982319237"
flotante = float(cadena)

# Comprobar si una variable es un entero
if isinstance(cadena, float):
	print cadena, "Es flotante"
else:
	print cadena, "No es flotante"

if isinstance(entero, float):
	print entero, "Es flotante"
else:
	print entero, "No es flotante"

if isinstance(flotante, float):
	print flotante, "Es flotante"
else:
	print flotante, "No es flotante"

# Diferencias en operaciones
entero = 5/7
flotante = 5./7

if isinstance(entero, float):
	print entero, "Es flotante"
else:
	print entero, "No es flotante"

if isinstance(flotante, float):
	print flotante, "Es flotante"
else:
	print flotante, "No es flotante"


# CADENAS DE TEXTO
cadenaUTF8 = "Aquí va un texto" # Como el archivo está en UTF-8 esta cadena también
print cadenaUTF8
cadena = cadenaUTF8.decode('utf-8') # Cadena ya está decodificada
print cadena
cadena = u"Aquí va un texto"
print cadena

# Convertir a cadena
cadena = str(entero)
cadena = str(flotante).encode('utf-8')


# LISTAS SIMPLES
lista_simple = [
	entero,
	flotante,
	cadena,
	cadena,
	"Pepito le dijo a su maestra que ¡aguas! bla bla...",
	# u"Pepito le dijo a su maestra que ¡aguas! bla bla...",
]

# Imprime la lista en formato "soy muy conocedor"
print lista_simple

# Imprime la lista datos por dato en limpio, línea por línea
for l in lista_simple:
	print l

# Implrime la UNION de la lista con un "pegamento"
lista_cadenas = []
for l in lista_simple:
	# Convertimos a cadena y agragamos a lista_cadenas
	lista_cadenas.append( str( l ) )

# Imprimimos sim problemas!!
print ", ".join(lista_cadenas)


# DICCIONARIO SIMPLES
diccionario = {
	"entero": entero,
	"flotante": flotante,
	"cadena": cadena,
	"constante": "Pepito le dijo a su maestra que ¡aguas! bla bla...",
}

# Imprimir a la brava
print diccionario

# Imprimir UNION de CLAVES (keys) << Siempre funciona !!
print ", ".join( diccionario.keys() )

# Imprimir UNION de VALORES (values) << NO Siempre funciona !!
# print ", ".join( diccionario.values() )

# OJO
# diccionario.values() es una lista!!!

# Implrime la UNION de la lista con un "pegamento"
lista_cadenas = []
for l in diccionario.values():
	# Convertimos a cadena y agragamos a lista_cadenas
	lista_cadenas.append( str( l ) )

print lista_cadenas

print ", ".join(lista_cadenas)