#!/usr/bin/env python -W ignore::DeprecationWarning
# -*- coding: utf-8 -*-

######################################################
# ESTE PEDAZO CONTROLA LA SALIDA UTF-8 Y LA AYUDA
import argparse
parser = argparse.ArgumentParser(description=u'Stanford POS Tagger en español desde Python')
parser.add_argument("-u", "--utf8", help=u"Codificar la salida como UTF-8.", action="store_true")
args = parser.parse_args()
import codecs,locale,sys
if args.utf8:
    sys.stdout = codecs.getwriter("utf8")(sys.stdout)
else:
    sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
######################################################
# Función de ayuda de impresión (no le hagan caso)
def addslashes(s):
    ech = [
        ("\r","\\r"),
        ("\n","\\n"),
        ("\t","\\t"),
    ]
    for e in ech:
        if e[0] in s:
            s = s.replace(e[0], e[1])
    return s
######################################################

"""
En este script mostraré cómo usar NLTK con un programa externo (Stanford POS-Tagger) para "etiquetar" 
las palabras de una frase en español de mejor manera que hasta ahora.
La librería externa (Stanford POS-Tagger) que usaremos no está en PYTHON sino en otro lenguaje muy 
conocido llamado JAVA.
Por suerte todo es muy fácil de instalar siguiendo estas instrucciones:

1- Debemos tener instalado el intérprete de JAVA en nuestra computadoram de forma similar a como instalamos
    el intérprete de python. La instalación varía dependiendo del sistema operativo que usemos.

    1.1- INSTALAR JAVA EN LINUX:

        1.1.1- Ejecutamos el siguiente comando desde la terminal:

            $ sudo apt-get install default-jre

        1.1.2- Probamos que la instalación funcionó ejecutando en la misma terminal:

            $ java -version

    1.2- INSTALAR JAVA EN WINDOWS / MAC:

        1.2.1- Descargamos el arcivo apropiado desde:

            https://www.java.com/es/download/

        1.2.2- Seguimos las instrucciones de instalación ;)

        1.2.3- Probamos que la instalación funcionó ejecutando en una terminal:

            $ java -version

2- Ahora debemos descargar y descomprimir el programa Stanford POS-Tagger en la carpeta adecuada.

    2.1- Descarga el programa desde aquí:

        https://nlp.stanford.edu/software/tagger.shtml#Download

    2.2- Fíjate de descargar la version completa (FULL) que la otra sólo funciona en inglés.

    2.3- El archivo "zip" descargado debemos descomprimirlo en una carpeta de nuestra compu.

3- Ahora podemos probar el script actual desde una terminal:

    $ python stanford-postaggerNLTK.py

NOTAS:
# Más acerca del "tagger": http://nlp.stanford.edu/software/tagger.shtml 
# Más acerca del "tagset": nlp.lsi.upc.edu/freeling/doc/tagsets/tagset-es.html

P.D. Cuando ejecutemos este script se nos mostrará un mensaje como este:

        .../dist-packages/nltk/tag/stanford.py:149: DeprecationWarning: 
        The StanfordTokenizer will be deprecated in version 3.2.5.
        Please use nltk.tag.corenlp.CoreNLPPOSTagger or nltk.tag.corenlp.CoreNLPNERTagger instead.

    Esto sucede aunque el programa se ejecute correctamente, el mensaje nos está avisando
    que conviene usar una versión más reciente del mismo paquete de programas llamado
    "Stanford Core NLP". En el siguiente script (simple-stanford-corenlp.py) veremos como instalar 
    y usar esa versión más actualizada.

"""

# Importamos una parte de nltk (para tokenizar en frases)
import nltk.data
# Importamos otra parte de nltk (para tokenizar en palabras y signos)
from nltk.tokenize import WordPunctTokenizer

# Definimos una cadena de texto (con varias frases) para probar
cadena = u"—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!\nEl veloz murciélago hindú comía feliz cardillo y kiwi.\nLa cigüena tocaba el saxofón detrás del palenque de paja.\nEl pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.\nExhíbanse politiquillos zafios,\ncon orejas kilométricas\n\ty unas de gavilán."
print u"Cadena:"
print "\t",addslashes(cadena)

# Versión en español del tokenizador por frases
spanish_frase_tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")
frases = spanish_frase_tokenizer.tokenize(cadena)
print u"Frases:"
for f in frases:
    print "\t",addslashes(f)

# Prepara el Tokenizador que separa las palabras y luego los signos de puntuación
palabra_tokenizer = WordPunctTokenizer()

# import nltk
from nltk.tag.stanford import StanfordPOSTagger as POSTagger
# En esa línea debemos cambiar la ruta por la adecuada en nuestra compu
spanish_postagger = POSTagger('../postagger/models/spanish.tagger', '../postagger/stanford-postagger.jar', encoding='utf8')
## Recorre frase por frase
for frase in frases:
    # Tokeniza cada frase
    palabras = palabra_tokenizer.tokenize(frase)
    # Taggea la frase tokenizada
    tagged_words = spanish_postagger.tag(palabras)
    for (word, tag) in tagged_words:
        print word,tag