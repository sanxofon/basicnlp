cls
chcp 1252
echo "Busca todos los caracteres de palabra"
python .\txtFileRegEx.py -f .\test\texto1.txt -i 1 > .\txtFileRegEx_1.csv
wc -l .\txtFileRegEx_1.csv
echo "Busca todos los caracteres que no son de palabra"
python .\txtFileRegEx.py -f .\test\texto1.txt -i 2 > .\txtFileRegEx_2.csv
wc -l .\txtFileRegEx_2.csv
echo "Busca todos los caracteres de espaciado"
python .\txtFileRegEx.py -f .\test\texto1.txt -i 3 > .\txtFileRegEx_3.csv
wc -l .\txtFileRegEx_3.csv
echo "Busca todos los caracteres que no son de espaciado"
python .\txtFileRegEx.py -f .\test\texto1.txt -i 4 > .\txtFileRegEx_4.csv
wc -l .\txtFileRegEx_4.csv
echo "Busca todas las palabras"
python .\txtFileRegEx.py -f .\test\texto1.txt -i 5 > .\txtFileRegEx_5.csv
wc -l .\txtFileRegEx_5.csv
echo "Busca pares de palabras separadas por un espacio"
python .\txtFileRegEx.py -f .\test\texto1.txt -i 6 > .\txtFileRegEx_6.csv
wc -l .\txtFileRegEx_6.csv
echo "Busca dos grupos de caracteres que no sean espacios seguidos, separados por un espacio"
python .\txtFileRegEx.py -f .\test\texto1.txt -i 7 > .\txtFileRegEx_7.csv
wc -l .\txtFileRegEx_7.csv
echo "Busca dos palabras separadas por un espacio que pueden o no tener un caractes no de palabra a los lados"
python .\txtFileRegEx.py -f .\test\texto1.txt -i 8 > .\txtFileRegEx_8.csv
wc -l .\txtFileRegEx_8.csv
echo "Busca todos los pares de palabras (separadas por espacio) con lookahead"
python .\txtFileRegEx.py -f .\test\texto1.txt -i 9 > .\txtFileRegEx_9.csv
wc -l .\txtFileRegEx_9.csv
echo "Busca pares de palabra/palabra o palabra/otro(s)/palabra, puede incluir caracteres o separadores entre la primera y la segunda palabra"
python .\txtFileRegEx.py -f .\test\texto1.txt -i 10 > .\txtFileRegEx_10.csv
wc -l .\txtFileRegEx_10.csv
echo "Busca pares de palabra/palabra o palabra/otro(s)/palabra, puede incluir caracteres o separadores entre la primera y la segunda palabra (sin capturas vacías)"
python .\txtFileRegEx.py -f .\test\texto1.txt -i 10 -e > .\txtFileRegEx_10e.csv
wc -l .\txtFileRegEx_10e.csv
