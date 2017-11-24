## Caracteres

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Caracter</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="brown">

<td><span class="mono">\d</span></td>

<td>Most engines: one digit  
from 0 to 9</td>

<td>file_\d\d</td>

<td>file_25</td>

</tr>

<tr class="beige">

<td><span class="mono">\d</span></td>

<td>.NET, Python 3: one Unicode digit in any script</td>

<td>file_\d\d</td>

<td>file_9੩</td>

</tr>

<tr class="brown">

<td><span class="mono">\w</span></td>

<td>Most engines: "word character": ASCII letter, digit or underscore</td>

<td>\w-\w\w\w</td>

<td>A-b_1</td>

</tr>

<tr class="beige">

<td><span class="mono">\w</span></td>

<td>.Python 3: "word character": Unicode letter, ideogram, digit, or underscore</td>

<td>\w-\w\w\w</td>

<td>字-ま_۳</td>

</tr>

<tr class="brown">

<td><span class="mono">\w</span></td>

<td>.NET: "word character": Unicode letter, ideogram, digit, or connector</td>

<td>\w-\w\w\w</td>

<td>字-ま‿۳</td>

</tr>

<tr class="beige">

<td><span class="mono">\s</span></td>

<td>Most engines: "whitespace character": space, tab, newline, carriage return, vertical tab</td>

<td>a\sb\sc</td>

<td>a b  
c</td>

</tr>

<tr class="brown">

<td><span class="mono">\s</span></td>

<td>.NET, Python 3, JavaScript: "whitespace character": any Unicode separator</td>

<td>a\sb\sc</td>

<td>a b  
c</td>

</tr>

<tr class="beige">

<td><span class="mono">\D</span></td>

<td>One character that is not a _digit_ as defined by your engine's _\d_</td>

<td>\D\D\D</td>

<td>ABC</td>

</tr>

<tr class="brown">

<td><span class="mono">\W</span></td>

<td>One character that is not a _word character_ as defined by your engine's _\w_</td>

<td>\W\W\W\W\W</td>

<td>*-+=)</td>

</tr>

<tr class="beige">

<td><span class="mono">\S</span></td>

<td>One character that is not a _whitespace character_ as defined by your engine's _\s_</td>

<td>\S\S\S\S</td>

<td>Yoyo</td>

</tr>

</tbody>

</table>

## Cuantificadores

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Cuantificador</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="wasabi">

<td><span class="mono">+</span></td>

<td>One or more</td>

<td>Version \w-\w+</td>

<td>Version A-b1_1</td>

</tr>

<tr class="greentea">

<td><span class="mono">{3}</span></td>

<td>Exactly three times</td>

<td>\D{3}</td>

<td>ABC</td>

</tr>

<tr class="wasabi">

<td><span class="mono">{2,4}</span></td>

<td>Two to four times</td>

<td>\d{2,4}</td>

<td>156</td>

</tr>

<tr class="greentea">

<td><span class="mono">{3,}</span></td>

<td>Three or more times</td>

<td>\w{3,}</td>

<td>regex_tutorial</td>

</tr>

<tr class="wasabi">

<td><span class="mono">*</span></td>

<td>Zero or more times</td>

<td>A*B*C*</td>

<td>AAACC</td>

</tr>

<tr class="greentea">

<td><span class="mono">?</span></td>

<td>Once or none</td>

<td>plurals?</td>

<td>plural</td>

</tr>

</tbody>

</table>

## Más Caracteres

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Caracter</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="brown">

<td><span class="mono">**.**</span></td>

<td>Any character except line break</td>

<td>a.c</td>

<td>abc</td>

</tr>

<tr class="beige">

<td><span class="mono">**.**</span></td>

<td>Any character except line break</td>

<td>.*</td>

<td>whatever, man.</td>

</tr>

<tr class="brown">

<td><span class="mono">\**.**</span></td>

<td>A period (special character: needs to be escaped by a \)</td>

<td>a\.c</td>

<td>a.c</td>

</tr>

<tr class="beige">

<td><span class="mono">\</span></td>

<td>Escapes a special character</td>

<td>\.\*\+\?    \$\^\/\\</td>

<td>.*+?    $^/\</td>

</tr>

<tr class="brown">

<td><span class="mono">\</span></td>

<td>Escapes a special character</td>

<td>\[\{\(\)\}\]</td>

<td>[{()}]</td>

</tr>

</tbody>

</table>

## Logic

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Logic</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="wasabi">

<td><span class="mono">|</span></td>

<td>Alternation / OR operand</td>

<td>22|33</td>

<td>33</td>

</tr>

<tr class="greentea">

<td><span class="mono">( … )</span></td>

<td>Capturing group</td>

<td>A(nt|pple)</td>

<td>Apple (captures "pple")</td>

</tr>

<tr class="wasabi">

<td><span class="mono">\1</span></td>

<td>Contents of Group 1</td>

<td>r(\w)g\1x</td>

<td>regex</td>

</tr>

<tr class="greentea">

<td><span class="mono">\2</span></td>

<td>Contents of Group 2</td>

<td>(\d\d)\+(\d\d)=\2\+\1</td>

<td>12+65=65+12</td>

</tr>

<tr class="wasabi">

<td><span class="mono">(?: … )</span></td>

<td>Non-capturing group</td>

<td>A(?:nt|pple)</td>

<td>Apple</td>

</tr>

</tbody>

</table>

## Más White-Space

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Caracter</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="brown">

<td><span class="mono">\t</span></td>

<td>Tab</td>

<td>T\t\w{2}</td>

<td>T     ab</td>

</tr>

<tr class="beige">

<td><span class="mono">\r</span></td>

<td>Carriage return character</td>

<td>see below</td>

</tr>

<tr class="brown">

<td><span class="mono">\n</span></td>

<td>Line feed character</td>

<td>see below</td>

</tr>

<tr class="beige">

<td><span class="mono">\r\n</span></td>

<td>Line separator on Windows</td>

<td>AB\r\nCD</td>

<td>AB  
CD</td>

</tr>

<tr class="brown">

<td><span class="mono">\N</span></td>

<td>Perl, PCRE (C, PHP, R…): one character that is not a line break</td>

<td>\N+</td>

<td>ABC</td>

</tr>

<tr class="beige">

<td><span class="mono">\h</span></td>

<td>Perl, PCRE (C, PHP, R…), Java: one horizontal whitespace character: tab or Unicode space separator</td>

</tr>

<tr class="brown">

<td><span class="mono">\H</span></td>

<td>One character that is not a horizontal whitespace</td>

</tr>

<tr class="beige">

<td><span class="mono">\v</span></td>

<td>.NET, JavaScript, Python, Ruby: vertical tab</td>

</tr>

<tr class="brown">

<td><span class="mono">\v</span></td>

<td>Perl, PCRE (C, PHP, R…), Java: one vertical whitespace character: line feed, carriage return, vertical tab, form feed, paragraph or line separator</td>

</tr>

<tr class="beige">

<td><span class="mono">\V</span></td>

<td>Perl, PCRE (C, PHP, R…), Java: any character that is not a vertical whitespace</td>

</tr>

<tr class="brown">

<td><span class="mono">\R</span></td>

<td>Perl, PCRE (C, PHP, R…), Java: one line break (carriage return + line feed pair, and all the characters matched by \v)</td>

</tr>

</tbody>

</table>

## Más Cuantificadores

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Cuantificador</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="wasabi">

<td><span class="mono">+</span></td>

<td>The + (one or more) is "greedy"</td>

<td>\d+</td>

<td>12345</td>

</tr>

<tr class="greentea">

<td><span class="mono">?</span></td>

<td>Makes cuantificadores "lazy"</td>

<td>\d+?</td>

<td>1 in **1**2345</td>

</tr>

<tr class="wasabi">

<td><span class="mono">*</span></td>

<td>The * (zero or more) is "greedy"</td>

<td>A*</td>

<td>AAA</td>

</tr>

<tr class="greentea">

<td><span class="mono">?</span></td>

<td>Makes cuantificadores "lazy"</td>

<td>A*?</td>

<td>empty in AAA</td>

</tr>

<tr class="wasabi">

<td><span class="mono">{2,4}</span></td>

<td>Two to four times, "greedy"</td>

<td>\w{2,4}</td>

<td>abcd</td>

</tr>

<tr class="greentea">

<td><span class="mono">?</span></td>

<td>Makes cuantificadores "lazy"</td>

<td>\w{2,4}?</td>

<td>ab in **ab**cd</td>

</tr>

</tbody>

</table>

## Caracter Classes

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Caracter</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="brown">

<td><span class="mono">[ … ]</span></td>

<td>One of the characters in the brackets</td>

<td>[AEIOU]</td>

<td>One uppercase vowel</td>

</tr>

<tr class="beige">

<td><span class="mono">[ … ]</span></td>

<td>One of the characters in the brackets</td>

<td>T[ao]p</td>

<td>_Tap_ or _Top_</td>

</tr>

<tr class="brown">

<td><span class="mono">-</span></td>

<td>Range indicator</td>

<td>[a-z]</td>

<td>One lowercase letter</td>

</tr>

<tr class="beige">

<td><span class="mono">[x-y]</span></td>

<td>One of the characters in the range from x to y</td>

<td>[A-Z]+</td>

<td>GREAT</td>

</tr>

<tr class="brown">

<td><span class="mono">[ … ]</span></td>

<td>One of the characters in the brackets</td>

<td>[AB1-5w-z]</td>

<td>One of either: A,B,1,2,3,4,5,w,x,y,z</td>

</tr>

<tr class="beige">

<td><span class="mono">[x-y]</span></td>

<td>One of the characters in the range from x to y</td>

<td>[ -~]+</td>

<td>Caracteres in the printable section of the ASCII table.</td>

</tr>

<tr class="brown">

<td><span class="mono">[^x]</span></td>

<td>One character that is not x</td>

<td>[^a-z]{3}</td>

<td>A1!</td>

</tr>

<tr class="beige">

<td><span class="mono">[^x-y]</span></td>

<td>One of the characters **not** in the range from x to y</td>

<td>[^ -~]+</td>

<td>Caracteres that are **not** in the printable section of the ASCII table.</td>

</tr>

<tr class="brown">

<td><span class="mono">[\d\D]</span></td>

<td>One character that is a digit or a non-digit</td>

<td>[\d\D]+</td>

<td>Any characters, inc-  
luding new lines, which the regular dot doesn't match</td>

</tr>

<tr class="beige">

<td><span class="mono">[\x41]</span></td>

<td>Matches the character at hexadecimal position 41 in the ASCII table, i.e. A</td>

<td>[\x41-\x45]{3}</td>

<td>ABE</td>

</tr>

</tbody>

</table>

## Anchors and Boundaries

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Anchor</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="wasabi">

<td><span class="mono">^</span></td>

<td>Start of string or start of line depending on multiline mode. (But when [^inside brackets], it means "not")</td>

<td>^abc .*</td>

<td>abc (line start)</td>

</tr>

<tr class="greentea">

<td><span class="mono">$</span></td>

<td>End of string or end of line depending on multiline mode. Many engine-dependent subtleties.</td>

<td>.*? the end$</td>

<td>this is the end</td>

</tr>

<tr class="wasabi">

<td><span class="mono">\A</span></td>

<td>Beginning of string  
(all major engines except JS)</td>

<td>\Aabc[\d\D]*</td>

<td>abc (string...  
...start)</td>

</tr>

<tr class="greentea">

<td><span class="mono">\z</span></td>

<td>Very end of the string  
Not available in Python and JS</td>

<td>the end\z</td>

<td>this is...\n...**the end**</td>

</tr>

<tr class="wasabi">

<td><span class="mono">\Z</span></td>

<td>End of string or (except Python) before final line break  
Not available in JS</td>

<td>the end\Z</td>

<td>this is...\n...**the end**\n</td>

</tr>

<tr class="greentea">

<td><span class="mono">\G</span></td>

<td>Beginning of String or End of Previous Match  
.NET, Java, PCRE (C, PHP, R…), Perl, Ruby</td>

</tr>

<tr class="wasabi">

<td><span class="mono">\b</span></td>

<td>Word boundary  
Most engines: position where one side only is an ASCII letter, digit or underscore</td>

<td>Bob.*\bcat\b</td>

<td>Bob ate the cat</td>

</tr>

<tr class="greentea">

<td><span class="mono">\b</span></td>

<td>Word boundary  
.NET, Java, Python 3, Ruby: position where one side only is a Unicode letter, digit or underscore</td>

<td>Bob.*\b\кошка\b</td>

<td>Bob ate the кошка</td>

</tr>

<tr class="wasabi">

<td><span class="mono">\B</span></td>

<td>Not a word boundary</td>

<td>c.*\Bcat\B.*</td>

<td>copycats</td>

</tr>

</tbody>

</table>

## POSIX Classes

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Caracter</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="brown">

<td><span class="mono">[:alpha:]</span></td>

<td>PCRE (C, PHP, R…): ASCII letters A-Z and a-z</td>

<td>[8[:alpha:]]+</td>

<td>WellDone88</td>

</tr>

<tr class="beige">

<td><span class="mono">[:alpha:]</span></td>

<td>Ruby 2: Unicode letter or ideogram</td>

<td>[[:alpha:]\d]+</td>

<td>кошка99</td>

</tr>

<tr class="brown">

<td><span class="mono">[:alnum:]</span></td>

<td>PCRE (C, PHP, R…): ASCII digits and letters A-Z and a-z</td>

<td>[[:alnum:]]{10}</td>

<td>ABCDE12345</td>

</tr>

<tr class="beige">

<td><span class="mono">[:alnum:]</span></td>

<td>Ruby 2: Unicode digit, letter or ideogram</td>

<td>[[:alnum:]]{10}</td>

<td>кошка90210</td>

</tr>

<tr class="brown">

<td><span class="mono">[:punct:]</span></td>

<td>PCRE (C, PHP, R…): ASCII punctuation mark</td>

<td>[[:punct:]]+</td>

<td>?!.,:;</td>

</tr>

<tr class="beige">

<td><span class="mono">[:punct:]</span></td>

<td>Ruby: Unicode punctuation mark</td>

<td>[[:punct:]]+</td>

<td>‽,:〽⁆</td>

</tr>

</tbody>

</table>

## Inline Modifiers

None of these are supported in JavaScript. In Ruby, beware of <span class="socode">(?s)</span> and <span class="socode">(?m)</span>.  

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Modifier</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="wasabi">

<td><span class="mono">(?i)</span></td>

<td>Case-insensitive mode  
(except JavaScript)</td>

<td>(?i)Monday</td>

<td>monDAY</td>

</tr>

<tr class="greentea">

<td><span class="mono">(?s)</span></td>

<td>DOTALL mode (except JS and Ruby). The dot (.) matches new line characters (\r\n). Also known as "single-line mode" because the dot treats the entire input as a single line</td>

<td>(?s)From A.*to Z</td>

<td>From A  
to Z</td>

</tr>

<tr class="wasabi">

<td><span class="mono">(?m)</span></td>

<td>Multiline mode  
(except Ruby and JS) ^ and $ match at the beginning and end of every line</td>

<td>(?m)1\r\n^2$\r\n^3$</td>

<td>1  
2  
3</td>

</tr>

<tr class="greentea">

<td><span class="mono">(?m)</span></td>

<td>In Ruby: the same as (?s) in other engines, i.e. DOTALL mode, i.e. dot matches line breaks</td>

<td>(?m)From A.*to Z</td>

<td>From A  
to Z</td>

</tr>

<tr class="wasabi">

<td><span class="mono">(?x)</span></td>

<td>Free-Spacing Mode mode  
(except JavaScript). Also known as comment mode or whitespace mode</td>

<td>(?x) # this is a  
# comment  
abc # write on multiple  
# lines  
[ ]d # spaces must be  
# in brackets</td>

<td>abc d</td>

</tr>

<tr class="greentea">

<td><span class="mono">(?n)</span></td>

<td>.NET: named capture only</td>

<td>Turns all (parentheses) into non-capture groups. To capture, use named groups.</td>

</tr>

<tr class="wasabi">

<td><span class="mono">(?d)</span></td>

<td>Java: Unix linebreaks only</td>

<td>The dot and the ^ and $ anchors are only affected by \n</td>

</tr>

</tbody>

</table>

## Lookarounds

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Lookaround</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="brown">

<td><span class="mono">(?=…)</span></td>

<td>Positive lookahead</td>

<td>(?=\d{10})\d{5}</td>

<td>01234 in **01234**56789</td>

</tr>

<tr class="beige">

<td><span class="mono">(?<=…)</span></td>

<td>Positive lookbehind</td>

<td>(?<=\d)cat</td>

<td>cat in 1**cat**</td>

</tr>

<tr class="brown">

<td><span class="mono">(?!…)</span></td>

<td>Negative lookahead</td>

<td>(?!theatre)the\w+</td>

<td>theme</td>

</tr>

<tr class="beige">

<td><span class="mono">(?<!…)</span></td>

<td>Negative lookbehind</td>

<td>\w{3}(?<!mon)ster</td>

<td>Munster</td>

</tr>

</tbody>

</table>

## Caracter Class Operations

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Class Operation</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="wasabi">

<td><span class="mono">[…-[…]]</span></td>

<td>.NET: character class subtraction. One character that is in those on the left, but not in the subtracted class.</td>

<td>[a-z-[aeiou]]</td>

<td>Any lowercase consonant</td>

</tr>

<tr class="greentea">

<td><span class="mono">[…-[…]]</span></td>

<td>.NET: character class subtraction.</td>

<td>[\p{IsArabic}-[\D]]</td>

<td>An Arabic character that is not a non-digit, i.e., an Arabic digit</td>

</tr>

<tr class="wasabi">

<td><span class="mono">[…&&[…]]</span></td>

<td>Java, Ruby 2+: character class intersection. One character that is both in those on the left and in the && class.</td>

<td>[\S&&[\D]]</td>

<td>An non-whitespace character that is a non-digit.</td>

</tr>

<tr class="greentea">

<td><span class="mono">[…&&[…]]</span></td>

<td>Java, Ruby 2+: character class intersection.</td>

<td>[\S&&[\D]&&[^a-zA-Z]]</td>

<td>An non-whitespace character that a non-digit and not a letter.</td>

</tr>

<tr class="wasabi">

<td><span class="mono">[…&&[^…]]</span></td>

<td>Java, Ruby 2+: character class subtraction is obtained by intersecting a class with a negated class</td>

<td>[a-z&&[^aeiou]]</td>

<td>An English lowercase letter that is not a vowel.</td>

</tr>

<tr class="greentea">

<td><span class="mono">[…&&[^…]]</span></td>

<td>Java, Ruby 2+: character class subtraction</td>

<td>[\p{InArabic}&&[^\p{L}\p{N}]]</td>

<td>An Arabic character that is not a letter or a number</td>

</tr>

</tbody>

</table>

## Other Syntax

<table style="table-layout:fixed;" border="0" width="100%">

<tbody>

<tr>

<th scope="col">Syntax</th>

<th scope="col" width="50%">Desc</th>

<th scope="col">Ejemplo</th>

<th scope="col">Match</th>

</tr>

<tr class="brown">

<td><name="k"><span class="mono">\K</span></name="k"></td>

<td>Keep Out  
Perl, PCRE (C, PHP, R…), Python's alternate _regex_ engine, Ruby 2+: drop everything that was matched so far from the overall match to be returned</td>

<td>prefix\K\d+</td>

<td>12</td>

</tr>

<tr class="beige">

<td><name="blockescape"><span class="mono">\Q…\E</span></name="blockescape"></td>

<td>Perl, PCRE (C, PHP, R…), Java: treat anything between the delimiters as a literal string. Useful to escape metacharacters.</td>

<td>\Q(C++ ?)\E</td>

<td>(C++ ?)</td>

</tr>

</tbody>

</table>
