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

import nltk.data

cadena = u"—¡Joven «emponzoñado» con el whisky, qué fin… te aguarda exhibir!\nEl veloz murciélago hindú comía feliz cardillo y kiwi.\nLa cigüena tocaba el saxofón detrás del palenque de paja.\nEl pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.\nExhíbanse politiquillos zafios,\ncon orejas kilométricas\n\ty unas de gavilán."

print u"Cadena:"
print "\t",addslashes(cadena)


spanish_frase_tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")
frases = spanish_frase_tokenizer.tokenize(cadena)

# Prepara el tokenizador
from nltk.tokenize import WordPunctTokenizer
palabra_tokenizer = WordPunctTokenizer()

# about the tagger: http://nlp.stanford.edu/software/tagger.shtml 
# about the tagset: nlp.lsi.upc.edu/freeling/doc/tagsets/tagset-es.html

# import nltk
from nltk.tag.stanford import StanfordPOSTagger as POSTagger
spanish_postagger = POSTagger('../postagger/models/spanish.tagger', '../postagger/stanford-postagger.jar', encoding='utf8')
for frase in frases:
    palabras = palabra_tokenizer.tokenize(frase)
    tagged_words = spanish_postagger.tag(palabras)
    for (word, tag) in tagged_words:
        print word,tag

# En inglés
# from nltk.tag.stanford import StanfordPOSTagger as POSTagger
# english_postagger = POSTagger("../postagger/models/english-bidirectional-distsim.tagger", "../postagger/stanford-postagger.jar")
# print english_postagger.tag("this is stanford postagger in nltk for python users".split())