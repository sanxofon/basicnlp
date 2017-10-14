# Ejemplos básicos de PYTHON para NLP

En este REPO incluímos varios scripts básicos que sirven como introducción al uso de PYTHON para el Procesamiento de Lenguaje Natural.

*All comments and examples are in spanish*

***

## Archivos incluídos hasta ahora:

## limpiartexto.py

> Este programa intenta rectificar los saltos de línea de un texto mal formateado y/o aplica un reemplazo regex definido por el usuario.

**Ejemplos de uso:**

        python limpiartexto.py -f "texto.txt" -n -u -m 2 > "texto2.txt"
        
        python limpiartexto.py -f "texto_original.txt" -n -u -m 4 -j -s "(\-\-)" -r "—" > "texto_modificado.txt"

## contarpalabras.py

> Este programa intenta contar la frecuencia de las palabras de un texto.

**Ejemplos de uso:**

        python contarpalabras.py -f "texto_original.txt" > "texto_palabras.txt"
        
        python contarpalabras.py -f "texto.txt" -q -o af > "texto3.txt"
 
***

## License

- [**MIT License**](LICENSE.md)

***

## Manteiner

- [**Santiago Chávez** (@sanxofon)](http://lengua.la/sanx.php)