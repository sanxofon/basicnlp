#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tal vez el mejor software de NLP para el idioma español actualmente es FREELING. Está escrito en 
lenguaje C++ que es el lenguaje más poderoso que existe.
Este script muestra cómo podemos analizar un texto con FREELING desde Python usando un wrapper
similar a los que hemos usado en ejemplos antriores. Sin embargo en este caso no tenemos ninguna 
configuración posible en la ejecución del programa, antes de correrlo debemos configurar el 
archivo "es.cfg" como se eplica más abajo.

INSTALAR FREELING:
	0. Debemos tener instalado JAVA como se mostró en el archivo "stanford-postaggerNLTK.py"

	1. Descargar el instalador más reciente de FREELING para nuestro sistema operativo desde:
		- https://github.com/TALP-UPC/FreeLing/releases
	En MAC es un poco más difícil ya que hay que compilarlo desde el código, instrucciones: 
		- https://talp-upc.gitbooks.io/freeling-user-manual/content/installation.html#installing-on-macos
	
	2. Una vez instalado el programa necesitamos saber dónde se creó la carpeta con los archivos 
	de configuración de FREELING. En mi caso (Ubuntu 16), FREELING se instaló en: "/usr/share/freeling/" 
	y los archivos de configuración se encuentran en: "/usr/share/freeling/config/"

	3. En un editor de texto (como Sublime Text) debemos abrir el archivo de configuración del 
	idioma español: "es.json". Este archivo se puede editar para configurar los procedimientos que 
	se aplicarán, el formato de salida y demás. Las instrucciones y opciones están en los comentarios 
	del mismo archivo.

Este script necesita del archivo incluído:
	- freelingwrapper.py

Ejemplos de uso:
	$ python basicFreeling.py > test/basicFreeling.json
Podemos enviar parámetros y realizar el análisis sobre un archivo de texto, este otro
ejemplo puede demorar algo de tiempo si el texto es muy largo pero resulta ser sorprendentemente rápido.

VERSION LINUX
	$ python basicFreeling.py
		-c /usr/share/freeling/config/es.cfg
		-l es -f test/texto1.txt 
		> test/texto1_freeling.json
	$ python basicFreeling.py -f test/texto2.txt > test/texto2_freeling.json

VERSION WINDOWS
	$ python basicFreeling.py
		-c C:\freeling\data\config\es.cfg
		-l es -f test/texto1.txt 
		> test/texto1_freeling.json
	$ python basicFreeling.py -f test/texto2.txt > test/texto2_freeling.json



"""
# MAGICA CONFIGURACIÓN DE CODECS SALIDA ----------------------
# FIX PARA WINDOWS CONSOLE, Usar: chcp 1252
import codecs,locale,sys
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
#--------------------------------------------------------------------------------
import os
# Importamos el wrapper de Freeling
from freelingwrapper import Analyzer

# ESTE PEDAZO CONTROLA LOS ARGUMENTOS QUE ACEPTA EL SCRIPT
import argparse
parser = argparse.ArgumentParser(description=u'FREELING Básico en español')
parser.add_argument("-c", "--cfg", help=u"Definir el archivo de configuración (ruta absoluta)")
parser.add_argument("-l", "--lang", help=u"Idioma en qe se realiza el análisis (debe coincidir con lo definido en la configuración)")
parser.add_argument("-f", "--file",type=argparse.FileType('r'), help=u"Definir el archivo de texto a analizar (en UTF-8)")
args = parser.parse_args()

# Argumentos recibidos o defaults si no se reciben
if args.cfg:
	config_file = args.cfg;
else:
	# Todos las configuraciones, seleccion de idioma y formato de salida se hacen en el archivo "es.cfg"
	if os.name == 'nt':
		config_file = 'C:\\s\\freeling\\data\\config\\es.cfg'
	else:
		config_file = '/usr/share/freeling/config/es.cfg'
if args.lang:
	lang = args.lang;
else:
	lang = 'es'
if args.file:
	text = args.file.read()
else:
	# Acá se puede aregar cualquier texto, nótese que no se declara el texto como unicode ya que FREELING 
	# recibe directamente UTF-8
	text = """La canasta de consumo para un hogar compuesto por un matrimonio con dos hijos e inquilinos de la vivienda, en la ciudad de Buenos Aires, alcanzaba un costo en el mes de mayo de 19.221,70 pesos, de acuerdo a estimaciones oficiales de la Dirección de Estadísticas y Censos del Gobierno de la Ciudad. Dicho valor representa un incremento del 5,05 por ciento con respecto al mes de abril, y muestra una llamativa aceleración desde que se disparó el proceso inflacionario, en noviembre de 2015 con el anuncio anticipado de Cambiemos de una devaluación y quita de retenciones a las exportaciones, al tiempo que crecía la perspectiva de que podría llegar al Gobierno. La inflación para la economía familiar, medida por el costo de la canasta de consumo, prácticamente se triplicó entre los últimos seis meses del gobierno anterior y el medio que lleva Cambiemos en el mando de la economía: del 9,2 por ciento de aumento acumulado entre mayo y noviembre del año pasado, saltó a más del 26 por ciento en el medio año transcurrido entre noviembre de 2015 y mayo pasado. El valor de la canasta de consumo creció 41,3 por ciento para un hogar conformado por una familia tipo en el último año, pero con fuerte aceleración en los útimos tres meses: 3,9 por ciento en marzo, 4,4 por ciento en abril y 5,05 por ciento en mayo.
Del valor total de la canasta de consumo de mayo, 6622,10 pesos (34,5 por ciento) correspondieron a la canasta de alimentos. El presupuesto familiar debió destinar, en ese mismo mes, otros 6251,46 pesos (32,5 por ciento) a los gastos de mantenimiento y servicios del hogar: alquiler, expensas, gas, electricidad, agua, bienes durables para el equipamiento del hogar y artículos de limpieza. El resto de la canasta corresponde a gastos de transporte, comunicaciones, educación, esparcimiento, salud y cuidado personal, e indumentaria, que suman en conjunto, aproximadamente otro tercio del presupuesto.
La canasta de alimentos, de acuerdo al seguimiento del organismo porteño, evolucionó en forma proporcional a la canasta total de consumo, con un incremento del 26,2 por ciento en los últimos seis meses, contra un incremento en los seis meses previos (de noviembre de 2015 a mayo de 2016) del 9,2 por ciento, siempre según datos de la Dirección de Estadísticas del gobierno de la CABA. Allí se refleja el fuerte impacto que la política de ajustes y devaluación del gobierno de Cambiemos tuvo sobre la economía popular.
El encarecimiento de los bienes y servicios básicos de la canasta de consumo familiar fue reflejada por el índice, a lo largo de los últimos meses, retratando lo que fueron los tarifazos y su impacto sobre la economía del hogar. El costo de la electricidad para el hogar de una familia tipo aumentó 253,3 por ciento en febrero; en abril, los mismos hogares sufrieron un incremento en el precio del gas de 194,7 por ciento según las estadísticas mensuales del organismo. El mazazo del aumento de la factura del agua impactó en los índices con un aumento de 107,3 por ciento en abril y otro, sobre el valor actualizado del aumento anterior, de 67,4 por ciento en mayo. De ese modo, entre los dos meses el incremento acumulado en este servicio esencial resultó de 246,9 por ciento. El ajuste del transporte público, en tanto, se vio reflejado en un aumento acumulado entre abril y mayo del 68,2 por ciento, siempre en función de su impacto sobre un hogar con familia tipo (matrimonio con dos hijos en edad escolar primaria). En enero de este año, los cuatro rubros de servicios mencionados representaban un costo mensual, para un hogar tipo, de 412,42 pesos en su conjunto. Cuatro meses después, en mayo, a esos mismos servicios la misma familia debía dedicar 980,22 pesos, un 137,7 por ciento más.
Entre los productos alimenticios, se destaca el incremento de los productos lácteos en mayo (leche, yogurt y otros), que alcanzó el 8,2 por ciento, en el marco de un aumento en el costo de la canasta alimenticia del 4,8 por ciento en el mes. De 6319,39 pesos en abril, pasó a un costo de 6622,10 pesos en mayo.
El informe de canastas de consumo del Gobierno de la Ciudad presenta seis casos diferentes, según la composición del hogar: parejas de adultos activos con o sin hijos; adultos mayores inactivos y propietarios, hogar unipersonal. En algunos de estos casos el incremento de la canasta de consumo resultó superior al del propio índice que elabora la Ciudad: 5,9 por ciento, en el caso del matrimonio de adultos mayores propietarios. El caso que fue tomado como referencia para esta nota es el de familia tipo en hogar alquilado, al considerarlo el más representativo. En el mismo se observa que, con dos sueldos medios, no se llega a cubrir el valor de una canasta de consumos media del hogar. Pero tampoco es el caso del grupo familiar “en peor situación”: los ejemplos ofrecidos no toman ningún caso de familias con más de dos hijos, que incrementaría sensiblemente la demanda en los rubros de mayor peso del presupuesto, como alimentos, educación, salud y equipamiento del hogar.
El aumento de la canasta de consumo que registra el gobierno de la Ciudad supera en mayo el incremento del índice de precios al consumidor que informó el Indec y refleja el deterioro progresivo del poder adquisitivo de las familias, con un proceso inflacionario incesante que se volvió a acelerar en los últimos tres meses. Esto último, el Indec no lo reflejó, por el apagón estadístico por decisión propia que el gobierno dispuso en diciembre y que, cuando volvieron a encenderse, no se recuperó con la reconstrucción de la serie de indicadores de precios mes a mes, como técnicamente hubiera sido esperable.
"""

# Ejecutamos en wrapper y freeling en el fondo
analyzer = Analyzer(config=config_file, lang=lang)
output = analyzer.run(text)

# Imprimimos la salida
print(output.decode('utf-8'))