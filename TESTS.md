## Testing

```Shell
	echo Testing "helloWorldUTF8"
	python helloWorldUTF8.py
	
	echo Testing "simpleEncodingUTF8"
	python simpleEncodingUTF8.py
	echo Testing "simpleEncodingCP1252"
	python simpleEncodingCP1252.py
	echo Testing "simpleRegexUTF8"
	python simpleRegexUTF8.py
	echo Testing "mediumRegexUTF8"
	python mediumRegexUTF8.py > "test/mediumRegexUTF8.txt"
	echo Testing "argumentosSimple"
	python argumentosSimple.py Santiago Chávez
	python argumentosSimple.py "Santiago Chávez"
	python argumentosSimple.py "Santiago Chávez" utf8 > "test/argumentosSimple.txt"
	echo Testing "argumentosParsed"
	python argumentosParsed.py -a "Santiago Chávez"
	python argumentosParsed.py -a "Santiago Chávez" -m
	python argumentosParsed.py -a "Santiago Chávez" -M
	echo Este ejemplo debe mostrar error de codificación
	python argumentosParsed.py -a "Santiago Chávez" -M > "test/test_argumentosParsed.txt"
	echo Testing "limpiarTexto"
	python limpiarTexto.py -f "test/texto1.txt" -n -u -m 2 > "test/texto1_limpio.txt"
	python limpiarTexto.py -f "test/texto2.txt" -n -u -m 4 -j -s "(\-\-)" -r "—" > "test/texto2_limpio.txt"
	python limpiarTexto.py -f "test/texto1.txt" -n -u -m 1 -e > "test/texto1_enunciados.txt"
	python limpiarTexto.py -f "test/texto2.txt" -n -u -m 1 -j -e -s "(\-\-)" -r "—" > "test/texto2_enunciados.txt"
	echo Testing "contarPalabras"
	python contarPalabras.py -f "test/texto1.txt" -q -o af -u > "test/texto1_palabras.txt"
	python contarPalabras.py -f "test/texto2.txt" -q -o af -u > "test/texto2_palabras.txt"
	echo Testing "contarCaracteres"
	python contarCaracteres.py -f "test/texto2.txt" -o aF -u > "test/texto2_caracteres.txt"
	python contarCaracteres.py -f "test/texto1.txt" -o aF -u > "test/texto1_caracteres.txt"
	echo Testing "basicNLTK"
	python basicNLTK.py -u > "test/basicNLTK.txt"
	echo Testing "mediumNLTK"
	python mediumNLTK.py -u > "test/mediumNLTK.txt"
	echo Testing "stanford-postaggerNLTK"
	python stanford-postaggerNLTK.py -u > "test/stanford-postaggerNLTK.txt"
	echo Testing "simple-stanford-corenlp"
    python simple-stanford-corenlp.py -u > test/simple-stanford-corenlp.txt
	echo Testing "medium-stanford-corenlp"
	python medium-stanford-corenlp.py -u -j > test/medium-stanford-corenlp.json
	python medium-stanford-corenlp.py -u -x > test/medium-stanford-corenlp.xml
	echo Testing "basicFreeling"
	python basicFreeling.py > test/basicFreeling.json
	python basicFreeling.py -c /usr/share/freeling/config/es.cfg -l es -f test/texto1.txt > test/texto1_freeling.json
	python basicFreeling.py -f test/texto2.txt > test/texto2_freeling.json
```
