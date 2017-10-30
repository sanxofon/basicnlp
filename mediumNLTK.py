#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
# ESTE PEDAZO CONTROLA LA SALIDA UTF-8 Y LA AYUDA
import argparse
parser = argparse.ArgumentParser(description=u'NLTK Básico en español')
parser.add_argument("-u", "--utf8", help=u"Codificar la salida como UTF-8.", action="store_true")
args = parser.parse_args()
if args.utf8:
    # import codecs,locale,sys
    # sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
    import codecs,sys
    sys.stdout = codecs.getwriter("utf8")(sys.stdout)
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

# Si ya está instalada la librería NLTK, podemos importarla sin errores
import nltk

"""
    Este script muestra es una versión un poco más avanzada de uso de NLTK, utilizando el corpus CESS.

    Podemos ejecutar este script con:

        $ python mediumNLTK.py
    
"""

##############################################################
# "Tokenizar" y "taggear" un texto:
# nltk.download("maxent_ne_chunker")
# Siempre que definamos una cadena en código lo haremos con el prefijo (u)
cadena = u"—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!\nEl veloz murciélago hindú comía feliz cardillo y kiwi.\nLa cigüena tocaba el saxofón detrás del palenque de paja.\nEl pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.\nExhíbanse politiquillos zafios,\ncon orejas kilométricas\n\ty unas de gavilán."

print u"Cadena:"
print "\t",cadena

# Ejemplo normal de tokenizador por palabras (las palabras se capturan con los signos de puntuación adyacentes)
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(cadena)
# print u"\nPalabras:"
# print "\t","\n\t".join([addslashes(t) for t in tokens])

# Tokenizador que separa las palabras y luego los signos de puntuación
from nltk.tokenize import WordPunctTokenizer
word_punct_tokenizer = WordPunctTokenizer()
palabras = word_punct_tokenizer.tokenize(cadena)
# print u"\nPalabras/Puntuación:"
# print "\t","\n\t".join([addslashes(t) for t in palabras])

# Versión en español del tokenizador por frases
import nltk.data
spanish_tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")
frases = spanish_tokenizer.tokenize(cadena)
# print u"\nFrases:"
# print "\t","\n\t".join([addslashes(t) for t in frases])

# POS-Tagging (en ingés, no funciona en español)
# tagged = nltk.pos_tag(tokens)
# print "Tagged:"
# for t in tagged:
#     print "\t", "\t".join(t)

# POS-Tagging sencillo (en español)
# Para poder taggear en español necesitamos primero entrenar 
# al tagger con un corpus de frases ya calificadas.
from nltk.corpus import cess_esp as cess # El corpus
from nltk import UnigramTagger as ut # El tagger (de una palabra)
from nltk import BigramTagger as bt # El tagger (de a dos palabras)

# Leemos el corpus a una lista
# Cada entrada de la lista es una frase
cess_sents = cess.tagged_sents()

# Dividimos el corpus en dos partes: entrenamiento y testeo
train = int(len(cess_sents)*90/100) # 90% entrenamiento

import pickle
crear_taggers = True
if crear_taggers:
    # Entrenamos el tagger de unigramas (no tiene caso el testeo con unigramas)
    uni_tag = ut(cess_sents)
    # Entramos el tagger de bigramas con sólamente la data de entrenamiento
    bi_tag = bt(cess_sents[:train])

    # Guardamos los taggers en archivos para ahorrar tiempo la siguiente vez
    with open('test/cess_unigram.tagger.pkl', 'wb') as output:
        pickle.dump(uni_tag, output, pickle.HIGHEST_PROTOCOL)
    with open('test/cess_bigram.tagger.pkl', 'wb') as output:
        pickle.dump(bi_tag, output, pickle.HIGHEST_PROTOCOL)

    # Evaluamos en los datos de testeo, el 10% restante
    evaluacion = bi_tag.evaluate(cess_sents[train+1:])
    print u"\nEvaluación:"
    print evaluacion
else:
    # Si ya están generados los taggers podemos simplemente abrirlos
    with open('test/cess_unigram.tagger.pkl', 'rb') as input:
        uni_tag = pickle.load(input)
    with open('test/cess_bigram.tagger.pkl', 'rb') as input:
        bi_tag = pickle.load(input)


# Tagger lee una lista de tokens: las "palabras" de "cadena"
tagged1 = uni_tag.tag(palabras)

# Tagger lee una lista de tokens: las "palabras" de "cadena"
tagged2 = bi_tag.tag(palabras)

# Imprimimos
print u"\nTagged Unigram:"
for t in tagged1:
    print "\t",t[1], t[0]
print u"\nTagged Bigram:"
for t in tagged2:
    print "\t",t[1], t[0]
