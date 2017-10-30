#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
En este script se muestra cómo usar el software Stanford CoreNLP
 - https://stanfordnlp.github.io

1. Descargamos el archivo "zip" desde acá:
 - https://stanfordnlp.github.io/CoreNLP/index.html#download

2. También debemos descargar los modelos para el idioma español

3. Una vez descargado, debemos "descomprimir" el archivo zip en una carpeta. Luego movemos el archivo
    con los modelos del idioma español (stanford-spanish-corenlp-2017-06-09-models.jar) a la carpeta que 
    acabamos de crear.
    Para que el programa funcione debemos tener instalado JAVA en nuestra compu, pero eso ya lo vimos 
    en "stanford-postaggerNLTK.py".

4. Ahora podemos probar que el programa funciona ejecutando en la terminal (en la carpeta que creamos):

    $ java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties StanfordCoreNLP-spanish.properties -port 9000 -timeout 15000
    
    Este comando (si no genera errores) inicia un "servidor" en el puerto 9000. Esto significa que ejecuta un 
    programa que abre una puerta en nuestra computadora que recibe preguntas y responde respuestas desde
    otros programas o "clientes", que pueden ser muchos y variados. 
    Debemos dejar abierta la terminal que lo está ejecutando.
    El programa "servidor" se seguirá ejecutando hasta lo cerremos, para parar el servidor apretamos las teclas [ctrl] y "c"

5. Ahora probemos que el servidor de verdad funciona abriendo un "navegador web" (firefox o chrome) que
    hará de "cliente" y visitemos la siguiente dirección web (que está en nuestra propia computadora):
    http://localhost:9000/

CoreNLP es un programa escrito en leguaje JAVA, que es un lenguaje bastante más oscuro que Python.
Sin embargo podemos usar CoreNLP desde Python usando un programa intermedio del tipo "wrapper"
Los programas "wrapper" son scripts sencillos que permiten ejecutar comandos en un lenguaje (en 
este caso uno JAVA) desde otro software (en este caso Python). 

De hecho, en el ejemplo que vimos anteriormente (stanford-postaggerNLTK.py) usamos una parte
de la librería NLTK como "wrapper" de otro programa JAVA (Stanford POS-Tagger), que es el "antececor" 
de coreNLP.

Ahora no usaremos NLTK, vamos a usar "stanfordcorenlp" que es un wrapper para coreNLP en Python
 - https://github.com/Lynten/stanford-corenlp

Podemos instalarlo con "pip" de forma muy simple:
    $ pip install stanfordcorenlp


Hemos terminado, así que podemos ejecutar este script desde la consola:

    $ python simple-stanford-corenlp.py

"""

cadena = u"—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir la Universidad Nacional!"
cadena = cadena.encode("utf-8")

print u"Cadena:"
print "\t",cadena
from stanfordcorenlp import StanfordCoreNLP

# Este comando inicia un servidor similar al que usamos probando la instalación y podemos usar "nlp" como
# "cliente" para preguntarle cosas al sevidor
# Acá debes reemplazar la ruta con la que corresponda en tu compu. Conviene adjudicarle la mitad de la memoria 
# que tenga tu compu al programa ya que los procesos usan mucha memoria RAM
nlp = StanfordCoreNLP(r'/home/jaci/git/corenlp/', lang='es', memory='2g')

# Hay 5 cosas simple que podemos preguntarle
print

# 1- Tokenización
print 'TOK:', nlp.word_tokenize(cadena)
print

# 2- Etiquetado POS / Part Of Speech Tagging
print 'POS:', nlp.pos_tag(cadena)
print

# 3- Entidades nombradas / Named Entities
print 'NER:', nlp.ner(cadena)
print

# 4- Análisis de circunscripciones / Constituency Parsing
print 'COPAR:'
print nlp.parse(cadena).encode('utf-8')
print

# 5- Análisis de dependencias / Dependency Parsing (NO FUNCIONA EN ESPAÑOL!!)
# print 'DEPAR:', nlp.dependency_parse(cadena)