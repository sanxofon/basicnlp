#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
En este script se muestra cómo usar la API del software Stanford CoreNLP para "anotar" textos en español
 - https://stanfordnlp.github.io

En el script anterior (simple-stanford-corenlp.py) vimos como instala y usar la librería 
desde python usando el wrapper:
 - https://github.com/Lynten/stanford-corenlp

Podemos ejecutar este script desde la consola:

    $ python medium-stanford-corenlp.py

"""

cadena = u"—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir la Universidad Nacional!"
cadena = cadena.encode("utf-8")

print u"Cadena:"
print "\t",cadena
from stanfordcorenlp import StanfordCoreNLP

# Este comando inicia un servidor similar al que usamos probando la instalación y podemos usar "nlp" como
# "cliente" para "anotar" texto en español
# Acá debes reemplazar la ruta con la que corresponda en tu compu. Conviene adjudicarle la mitad de la memoria 
# que tenga tu compu al programa ya que los procesos usan mucha memoria RAM (se recomiendan 8g])
nlp = StanfordCoreNLP(r'/home/jaci/git/corenlp/', lang='es', memory='2g')

# Podemos probar de la manera más simple que nos dará una salida en formato JSON (más adelante veremos qué es eso)
print nlp.annotate(cadena)#.encode('utf-8')

# # Podemos especificar las propiedades que queremos extraer y el formato de salida:
# props={'annotators': 'tokenize,ssplit,pos','pipelineLanguage':'es','outputFormat':'xml'}
# print nlp.annotate(cadena, properties=props)

"""

    Anotadores / annotators:

        tokenize, ssplit, pos, ner, parse
    
    Idioma / pipelineLanguage: 

        en, zh, ar, fr, de, es
        (English, Chinese, Arabic, French, German, Spanish)

    Formato de salida / outputFormat: 

        json, xml, text
    
VER TODOS LOS ANOTADORES DISPONIBLES EN:
    https://stanfordnlp.github.io/CoreNLP/annotators.html
Ojo que muchas funcionalidades que aparecen en la página sólo están disponibles en inglés

VER QUÉ FUNCIONALIDADES ESTÁN DISPONIBLES EN CADA LENGUAJE EN:
    https://stanfordnlp.github.io/CoreNLP/human-languages.html

"""


# ## También podemos usar un servidor que ya esté corriendo (ver instalación de CoreNLP 
# ## en "simple-stanford-corenlp.py").
# nlp = StanfordCoreNLP('http://127.0.0.1', port=9000)

# ## Debug
# import logging
# from stanfordcorenlp import StanfordCoreNLP
# ## Debug del wrapper
# nlp = StanfordCoreNLP(r'path_or_host', logging_level=logging.DEBUG)

# ## Ver más información del servidor CoreNLP 
# nlp = StanfordCoreNLP(r'path_or_host', quiet=False, logging_level=logging.DEBUG)