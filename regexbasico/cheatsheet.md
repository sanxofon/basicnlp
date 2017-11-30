# Regex CheatSheet - Guía rápida de expresiones regulares
---

### ¿Necesitas ayuda con las expresiones regulares?

- **Consulta el [Curso rápido de expresiones regulares en español](https://github.com/sanxofon/basicnlp/blob/master/regexbasico/README.md)**

## Caracteres

Caracter|Desc|Ejemplo|Match
| ----- | ----- | ----- | ----- |
\d|Un dígito entre 0 y 9|file_\d\d|file_25
\d|.NET, Python 3: Un dígito Unicode en cualquier escritura|file_\d\d|file_9੩
\w|"caracter de palabra": Letra ASCII, dígito o guión bajo|\w-\w\w\w|A-b_1
\w|.Python 3: "Caracter de palabra": Letra Unicode, ideograma, dígito, o guión bajo|\w-\w\w\w|字-ま_۳
\w|.NET: "Caracter de palabra": Letra Unicode, ideograma, dígito, o conector|\w-\w\w\w|字-ま‿۳
\s|"Caracter de espacio en blanco": espacio, tab, nueva línea, retorno de carro, tab vertical|a\sb\sc|a b<br>c
\s|.NET, Python 3, JavaScript: "Caracter de espacio en blanco": cualquier separador Unicode|a\sb\sc|a b<br>c
\D|Un caracter que no sea un _dígito_ según esté definido _\d_|\D\D\D|ABC
\W|Un caracter que no sea un _caracter de palabra_ según esté definido _\w_|\W\W\W\W\W|*-+=)
\S|Un caracter que no sea un _caracter de espacio en blanco_ según esté definido _\s_|\S\S\S\S|Yoyo


## Cuantificadores

Cuantificador|Desc|Ejemplo|Match
| ----- | ----- | ----- | ----- |
+|Uno o más|Version \w-\w+|Version A-b1_1
{3}|Exactamente tres veces|\D{3}|ABC
{2,4}|Dos o cuatro veces|\d{2,4}|156
{3,}|Tres o más veces|\w{3,}|regex_tutorial
\*|Cero o más veces|A\*B\*C\*|AAACC
?|Una vez o ninguna|libros?|libro


## Más Caracteres

Caracter|Desc|Ejemplo|Match
| ----- | ----- | ----- | ----- |
.|Cualquier caracter excepto salto de línea|a.c|abc
.|Cualquier caracter excepto salto de línea|.*|whatever, man.
\\.|Un punto (Caracter especial: debe ser escapado con un \\)|a\\.c|a.c
\\ |Escapa un caracter especial|\\.\\*\\+\\?\\$\\/\\\\ |.*+?$\/\\
\\ |Escapa un caracter especial|\\[\\{\\(\\)\\}\\]|[{()}]


## Lógicos

Lógico|Desc|Ejemplo|Match
| ----- | ----- | ----- | ----- |
\||Opciones / operando OR|22\|33|33
( … )|Capturar grupo|A(nt\|pple)|Apple (captura "pple")
\1|Contenido del Grupo 1|r(\w)g\1x|regex
\2|Contenido del Grupo 2|(\d\d)\+(\d\d)=\2\+\1|12+65=65+12
(?: … )|Grupo que no es capturado|A(?:nt|pple)|Apple


## Espacios vacíos

Caracter|Desc|Ejemplo|Match
| ----- | ----- | ----- | ----- |
\t|Tab|T\t\w{2}|T &nbsp;&nbsp; ab
\r|Caracter de retorno de carro|ver abajo
\n|Caracter de nueva linea|ver abajo
\r\n|Separador de nueva linea en Windows|AB\r\nCD|AB<br>CD
\N|Perl, PCRE (C, PHP, R…): Un caracter que no es un salto de línea|\N+|ABC
\h|Perl, PCRE (C, PHP, R…), Java: un caracter de espacio en blanco horizontal: tab o un separador de espacio Unicode
\H|Un caracter que no es de espacio en blanco horizontal
\v|.NET, JavaScript, Python, Ruby: tab vertical
\v|Perl, PCRE (C, PHP, R…), Java: un caracter de espacio en blanco vertical: salto de línea, retorno de carro, tab vertical, envío de formulario, párrafo o separador de línea
\V|Perl, PCRE (C, PHP, R…), Java: Cualquier caracter que no sea de espacio en blanco vertical
\R|Perl, PCRE (C, PHP, R…), Java: Un salto de línea (el par retorno de carro + salto de línea, y todos los caracteres que coincidan con \v)


## Más Cuantificadores

Cuantificador|Desc|Ejemplo|Match
| ----- | ----- | ----- | ----- |
+|El + (uno o más) es "codicioso"|\d+|12345
?|Hace los cuantificadores "perezosos"|\d+?|1 en **1**2345
\*|El \* (cero o más) es "codicioso"|A*|AAA
?|Hace los cuantificadores "perezosos"|A*?|vacío en AAA
{2,4}|Dos a cuatro veces, "codicioso"|\w{2,4}|abcd
?|Hace los cuantificadores "perezosos"|\w{2,4}?|ab en **ab**cd


## Clases de caracteres

Caracter|Desc|Ejemplo|Match
| ----- | ----- | ----- | ----- |
[ … ]|Uno de los caracteres entre los corchetes|[AEIOU]|Una vocal mayúscula sin acento
[ … ]|Uno de los caracteres entre los corchetes|T[ao]p|_Tap_ o _Top_
-|Range indicator|[a-z]|Una letra minúscula sin acento
[x-y]|Uno de los caracteres en el rango de x a y|[A-Z]+|GREAT
[ … ]|Uno de los caracteres entre los corchetes|[AB1-5w-z]|Uno de los siguientes: A,B,1,2,3,4,5,w,x,y,z
[x-y]|Uno de los caracteres entre el rango de x a y|[ -~]+|Caracteres en la sección imprimible de la tabla ASCII.
[^x]|Un caracter que no es *x*|[^a-z]{3}|A1!
[^x-y]|Uno de los caracteres que **no** está en en rango de x a y|[^ -~]+|Caracteres que **no** están en la sección imprimible de la tabla ASCII.
[\d\D]|Un caracter que es un dígito o un no-dígito|[\d\D]+|Cualquier caracter, uncluyendo nueva línea que el punto regular no hace coincidencia
[\x41]|Coincide con el caracter en la posición hexadecimal 41 de la tabla ASCII, p.ej. A|[\x41-\x45]{3}|ABE


## Anclas (anchors) y fronteras (boundaries)

Ancla|Desc|Ejemplo|Match
| ----- | ----- | ----- | ----- |
^|Start of string or start of line depending on multiline mode. (But when [^inside corchetes], it means "not")|^abc .*|abc (line start)
$|End of string or end of line depending on multiline mode. Many engine-dependent subtleties.|.*? the end$|this is the end
\A|Beginning of string   (all major engines except JS)|\Aabc[\d\D]*|abc (string...  ...start)
\z|Very end of the string   Not available in Python and JS|the end\z|this is...\n...**the end**
\Z|End of string or (except Python) antes del salto de línea final   Not available in JS|the end\Z|this is...\n...**the end**\n
\G|Beginning of String or End of Previous Match  .NET, Java, PCRE (C, PHP, R…), Perl, Ruby
\b|Word boundary. Position where one side only is an letra ASCII, dígito o guión bajo|Bob.*\bcat\b|Bob ate the cat
\b|Word boundary   .NET, Java, Python 3, Ruby: position where one side only is a Letra Unicode, dígito o guión bajo|Bob.*\b\кошка\b|Bob ate the кошка
\B|Not a word boundary|c.*\Bcat\B.*|copycats


## Modificadores internos (inline)
None of these are supported in JavaScript. In Ruby, beware of (?s) and (?m).  

Modificador|Desc|Ejemplo|Match
| ----- | ----- | ----- | ----- |
(?i)|Case-insensitive mode   (except JavaScript)|(?i)Monday|monDAY
(?s)|DOTALL mode (except JS and Ruby). The dot (.) matches new line characters (\r\n). Also known as "single-line mode" because the dot treats the entire input as a single line|(?s)From A.*to Z|From A to Z
(?m)|Multiline mode   (except Ruby and JS) ^ and $ match at the beginning and end of every line|(?m)1\r\n^2$\r\n^3$|1<br>2<br>3
(?m)|In Ruby: the same as (?s) in other engines, i.e. DOTALL mode, i.e. dot matches saltos de línea|(?m)From A.*to Z|From A to Z
(?x)|Free-Spacing Mode mode   (except JavaScript). Also known as comment mode or whitespace mode|(?x) # this is a<br># comment<br>abc # write on multiple<br># lines<br>[ ]d # spaces must be<br># in corchetes|abc d


## Mirar adelante y atrás (Lookarounds)

Lookaround|Desc|Ejemplo|Match
| ----- | ----- | ----- | ----- |
(?=…)|Positive lookahead|(?=\d{10})\d{5}|01234 in **01234**56789
(?|Positive lookbehind|(?<=\d)cat|cat in 1**cat**
(?!…)|Negative lookahead|(?!theatre)the\w+|theme
(?|Negative lookbehind|\w{3}(?<!mon)ster|Munster

