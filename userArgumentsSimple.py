#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Hay diversas maneras de recibir información del usuario en la terminal
	Para pedir información al usuario DURANTE la ejecución de un script
	podemos usar la función "raw_input" y guardar la respuesta en una variable
	como se puede ver en el script: "helloWorldUTF8.py"
	A veces queremos recibir información del usuario desde que EJECUTAMOS el
	script, es decir, desde un principio.
	Ejemplos de ejecución:
	>> python userArgumentsSimple.py Santiago Chávez
	>> python userArgumentsSimple.py "Santiago Chávez"
	>> python userArgumentsSimple.py "Santiago Chávez" utf8 > test.txt
"""

# Importamos una librería para poder usar sus funcionalidades
# La librería "sys" no permite acceder a información del sistema
import sys

# La librería "sys" nos permite acceder a los "argumentos" que fueron invocados al ejecutar este script
nombreScript = sys.argv[0] # El índice "0" siempre contiene el nombre del script actual: "userArgumentsSimple.py"
# Decodificamos los argumentos a UNICODE con ".decode(sys.stdin.encoding)"
argumentos = [] # Definimos la variable "argumentos" como una "lista vacía"
# Recorremos los argumentos del 1 al total de argumentos
for i in range(1,len(sys.argv)):
	argumentos.append(sys.argv[i].decode(sys.stdin.encoding)) # El índice "i" trae el argumento actual (si es que existe)

# Buscamos la cadena "utf8" en los argumentos recibidos
# Si existe creamos una variable "utf8" para acordarnos
utf8 = False
if "utf8" in argumentos:
	utf8 = True
	argumentos.remove("utf8") # Elimina el argumento "utf8" de la lista

# Por último imprimimos los argumentos invocados por el usuario
print u"Argumentos recibidos:"
for i in range(len(argumentos)):
	if utf8:
		# Si se recibió "utf8" en los argumentos codificamos la salida
		print "\t",i+1,".",argumentos[i].encode('utf-8')
	else:
		# De lo contrario imprimimos tal cual
		print "\t",i+1,".",argumentos[i]