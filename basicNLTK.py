#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Este script muestra los primeros pasos de uso de la 
	librería "nltk" (Natural Language Toolkit) para procesamiento de 
	lenguaje natural. Incluye instrucciones básicas de instalación, 
	configuración y descarga de Corpora, Diccionarios, etc.

	Para importar la librería solo usaremos:

	>> import nltk

	Sin embargo, hasta ahora hemos usado librerías que ya vienen incluídas 
	en el paquete básico de Python 2.7.
	
	La librería NLTK no viene incluída por default así que debemos instalarla, 
	para esto usamos la herramienta "pip".

	Lo primero que debemos hacer es comprobar que tenemos instalado "pip" que 
	nos ayudará a instalar fácilmente cualquier librería python. Para esto
	he incluído en el repo el script "get-pip.py" que se puede encontrar en:
	https://bootstrap.pypa.io/get-pip.py

	INSTRUCCIONES DE INSTALACIÓN

	1. Abrimos nuestra consola en la carpeta del proyecto y escribimos:

		$ python get-pip.py

	Este procedimiento instalará, actualizará o nos dirá si ya teníamos "pip"

	2. Una vez que "pip" está correctamente instalado podemos comprobarlo con:

		$ pip --version

	3. Ahora podemos instalar cualquier librería python con "pip".
	Ĺa librería NLTK conviene instalarla al lado de otra llamada: NumPy
	Instalamos las librerías NumPy y NLTK de la siguiente manera:

	En windows:

		$ pip pip install -U numpy
		$ pip install -U nltk

	En Linux:

	El comando anterior comando nos muestra un error de permisos
	que se resuelven añadiendo el comando "sudo" al principio. De esta
	manera indicamos que somos administradores.

		$ sudo pip install -U numpy
        $ sudo pip install -U nltk

	El sistema Linux nos preguntará el password de administrador que es el mismo
	que el password de usuario que se usa al iniciar la compu (casi siempre).

"""

# Si ya está instalada la librería NLTK, podemos importarla sin errores
import nltk

"""
	Si llegaste hasta aquí ¡felicidades! ya que lograste instalar NLTK, pero la lista 
	de instalaciones aún no ha terminado desgraciadamente.
	Lo que hemos instalado de NLTK es apenas un pqueño pedazo de funcionalidades
	pero la librería NLTK viene con muchos corpus, gramáticas de juguete, 
	modelos entrenados, etc. con los cuales podemos jugar. Luego veremos cómo
	incorporar otros, pero es fácil comenzar a usar NLTK con los que ya trae 
	disponibles. Algunos son muy grandes y de varios idiomas así que debemos
	descargar sólo los que queremos usar.

	Esto se logra abriendo una terminal y escribiendo:

		$ python

	Así, solito. Se mostrará la interfaz de comandos de Python. Ahi debemos importar 
	la librería y luego ejecutar un download() con ella:

		>>> import nltk
		>>> nltk.download()

	Esto mostrará una interfaz de descarga de materiales gratuitos, en concreto se
	muestra un menú como este:

	---------------------------------------------------------------------------
	    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
	---------------------------------------------------------------------------

	Si apretamos la tecla "l" (list) se mostrará la lista completa de paquetes
	que se pueden descargar libremente. La lista completa la incluyo en el
	archivo: "nltk_packages.txt" en este mismo repo, aqií listo algunos que usaremos
	y que vamos a instalar.

	Son pocos los que sirven para español específicamente:

	  [ ] cess_esp............ CESS-ESP Treebank
	  [ ] spanish_grammars.... Grammars for Spanish

	Y otros que son multidioma e incluyen elementos en español:

	  [ ] crubadan............ Crubadan Corpus
	  [ ] conll2002........... CONLL 2002 Named Entity Recognition Corpus
	  [ ] omw................. Open Multilingual Wordnet
	  [ ] stopwords........... Stopwords Corpus
	  [ ] swadesh............. Swadesh Wordlists
	  [ ] universal_tagset.... Mappings to the Universal Part-of-Speech Tagset
	  [ ] universal_treebanks_v20 Universal Treebanks Version 2.0
	  [ ] words............... Word Lists

	Para salir de la interfaz de NLTK apretamos la letra "q".
	Para salir del intérprete de Pythos escribimos:

		>>> quit()

	Podemos instalar todos los paquetes de la lista ejecutando el script 
	"instalar_nltk_data.py" que se incluye en este repo:

		$ python instalar_nltk_data.py

	Una vez instalado podremos ejecutar este script con:

		$ python basicNLTK.py
	
"""

##############################################################
# Ahora sigamos un ejemplo similar al que se muestra la página
# de NLTK (nltk.org) pero "traducido" al español.
##############################################################
# "Tokenizar" y "taggear" un texto:

import nltk
sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
tokens
['At', 'eight', "o'clock", 'on', 'Thursday', 'morning',
'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']
tagged = nltk.pos_tag(tokens)
tagged[0:6]
[('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),
('Thursday', 'NNP'), ('morning', 'NN')]

# Identify named entities:

entities = nltk.chunk.ne_chunk(tagged)
entities
Tree('S', [('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'),
           ('on', 'IN'), ('Thursday', 'NNP'), ('morning', 'NN'),
       Tree('PERSON', [('Arthur', 'NNP')]),
           ('did', 'VBD'), ("n't", 'RB'), ('feel', 'VB'),
           ('very', 'RB'), ('good', 'JJ'), ('.', '.')])

# Display a parse tree:

from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
##############################################################
