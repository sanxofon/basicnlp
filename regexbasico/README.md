
# Curso básico de expresiones regulares en español

Muchas aplicaciones y lenguajes de programación tienen su propia implementación de expresiones regulares (*regex*), a menudo con diferencias leves y a veces significativas con respecto a otras implementaciones. Cuando dos aplicaciones usan una implementación diferente de expresiones regulares, decimos que usan diferentes "sabores" (*flavours*) de expresiones regulares. Trataré de explicar la sintaxis de los "sabores" más comunes, pero dejo aquí un [CheatSheet](cheatsheet.md) para referencia rápida y que incluye las diferencias básicas que se encontrarán en los distintos *sabores* de *regex* más comunes.

## Patrones de texto y coincidencias

Una **expresión regular* -o *regex* para abreviar- es un patrón que describe una cierta cantidad de textos que tienen ciertas características similares.

Una **coincidencia** es cuando la *expresión regular* se encontró en la cadena de búsqueda, la coincidencia es la porción de la *cadena* que coincide con el *patrón*, es decir el "pedazo de texto" que cumple las características definidas por la *expresión regular*.

Una **cadena** es un texto sobre el cual se buscarán *coincidencias* con la *expresión regular*.

### Caracteres literales

La *expresión regular* más básica consiste en un único *caracter literal*, como **a** y la búsqueda de sólo la primera *coincidencia* en una *cadena*. Si la *cadena* es **Lupita es una niña**, la primera *coincidencia* será la **a** que está después de la **t**. Los programas que realizar expresiones regulares nos permiten recibir el *caracter* encontrado como respuesta, **a**, y/o la posición de la coincidencia, que en este caso sería **5**.

Esta expresión regular también puede coincidir con la segunda **a**. Sólo lo hace cuando se le pide al motor de expresiones regulares que comience a buscar a través de la cadena **después** de la primera coincidencia. En un editor de texto, puede hacerlo utilizando su función "Buscar siguiente" o "Buscar hacia adelante". En un lenguaje de programación, generalmente hay una función separada a la que puede llamar para continuar buscando a través de la cadena después de la coincidencia anterior, que busca la última coincidencia o bien que permite buscar *todas* las coincidencias.

**Caracteres que tienen significados especiales en las expresiones regulares:**

1. la barra invertida **\\** 
1. la referencia **^** 
1. el signo de dólar **$** 
1. el punto **.** 
1. el símbolo de barra vertical **|** 
1. el signo de interrogación **?** 
1. el asterisco __*__ 
1. el signo más **+** 
1. el signo de guión o menos **-** 
1. los paréntesis de apertura **(** y de cierre **)** 
1. los corchetes de apertura **[** y de cierre **]** 
1. y las llaves de apertura **{** y de cierre **}** 

Estos caracteres especiales a menudo se llaman "metacaracteres". La mayoría de ellos muestran errores cuando no se usan adecuadamente.

Si deseas utilizar cualquiera de estos caracteres como un literal en una expresión regular, debes *escaparlos* con una barra invertida. Si quieres hacer coincidir '**1 + 1 = 2**', la expresión regular correcta es '**1 \\+ 1 = 2**'. De lo contrario, el signo más (+) tiene un significado especial.

Todos los demás caracteres son considerados literales y se representan a sí mismos en una *expresión regular*. De forma que si nuestro patrón es **abc123/"**, el motor buscará exactamente eso en el texto objetivo, como cualquier buscador por palabra simple.

### Clases de caracteres o juegos de caracteres

Una *clase de caracteres* coincide solo con uno de varios caracteres u opciones. Para hacer coincidir una **a** o una **e**, podemos usar el patrón **[ae]**.

> Podemos usar **p[aeiou]to** y para hacer coincidir con **p*a*to**, **p*e*to**, **p*i*to**, **p*o*to** y **p*u*to**. 

Una *clase de caracter* solo coincide con **un solo** caracter: **p[aeiou]to** no concuerda con **p*aa*to**, **p*au*to**, **p*eiu*to** o cualquier cosa similar.

**El orden de los caracteres dentro de una clase de caracter no importa.**

Puedes usar un guion **-** dentro de una *clase de caracteres* para especificar un rango de caracteres. 

> El patrón **[0-9]** coincide con un solo dígito entre 0 y 9. 

Puedes usar más de un rango.  El patrón **[0-9a-z]** coincide con un solo caracter ya sea número del **0** al **9** o una letra de la **a** a la **z** (sin acento, diéresis ni eñe).

> Para incluir todos los acentos del español y la eñe podemos usar: **[a-záéíóúüñ]**

Escribir una *referencia* después del *corchete de apertura* **[^** niega la clase de caracter. El resultado es que la clase de caracteres coincide con cualquier cosa que **no** esté en la clase de caracteres.

> Por ejemplo, el patrón **c[^au]lo** coincide con cualquier palabra como **celo**, **colo**, **cblo**, **c8lo**, etc. pero **no** coincide con **calo** ni con **culo**.

### Clases de caracteres abreviados

+ **\\d** coincide con un solo carácter que es un dígito
+ **\\w** coincide con un "carácter de palabra" (caracteres alfanuméricos sin acentos más guion bajo)
+ **\\s** coincide con un carácter de espacio en blanco (incluye tabulador y saltos de línea).

Las opciones negativas de las anteriores son:

+ **\D**	coincide con un solo carácter que **no** es un dígito
+ **\W**	coincide con un carácter  que **no** sea "carácter de palabra"
+ **\S**	coincide con un carácter que **no** sea de espacio en blanco

Los caracteres reales que coinciden con los atajos depende del software que está utilizando, sobre todo con letras y signos que no sean del inglés, como los acentos del español y la eñe. Por ejemplo, el caracter **\\w** no va a coincidir con **á**, **é**, **í**, **ó**, **ú**, **ü** ni **ñ** en versiones que no incorporen Unicode correctamente.

Ver CheatSheet para saber más entre las diferencias, por ejemplo, entre Python 2 y Python 3.

### Caracteres no imprimibles

Puede usar secuencias de caracteres especiales para poner caracteres no imprimibles en su expresión regular.

1. **\\t** para hacer coincidir un carácter de tabulación
1. **\\r** para retorno de carro
1. **\\n** para salto de línea

Los elementos no imprimibles más exóticos son **\\a** (campana), **\\e** (escape), **\\f** (alimentación de formulario) y **\\v** (pestaña vertical). Recuerde que los archivos de texto de *Windows* usan **\\r\\n** para terminar líneas, mientras que los archivos de texto de *UNIX* y *MAC* usan solamente **\\n** .

Si su aplicación es compatible con *Unicode* , puedes usar **\\uFFFF** o **\\x{FFFF}** para insertar un carácter *Unicode* *directamente*. Por ejemplo, **\\u1F40C** o **\\x{1F40C}** coincide con el signo de un caracolito **🐌** y **\\u1F4A9** o **\\x{1F4A9}** coincide con la famosa "*pile of poo*" 💩.

Si una aplicación no es compatible con *Unicode*, se puede usar **\\xFF** para que coincida con un carácter específico por su índice hexadecimal en el juego de caracteres. **\\xA9** coincide con el símbolo de **Ⓒ** en el juego de caracteres *Latin-1*.

Todos los *caracteres no imprimibles* se pueden usar directamente en la *expresión regular* o como parte de una *clase de caracteres*.

### El punto (.) coincide (casi) con cualquier caracter

El punto **.** coincide con un solo carácter, excepto los caracteres de *salto de línea*. La mayoría de las aplicaciones tienen un modo "punto coincide con todos" o "línea única" que hace que el punto coincida con *cualquier carácter*, incluidos los *saltos de línea*.

> El patrón **gr.s** y coincide con **gris**, **gr4s** , **gr%s**, etc.

**Utilice el punto con moderación. A menudo, una clase de caracter o clase de carácter negada es más rápida y más precisa.**

### Anclajes

Los anclajes no coinciden con ningún caracter sino con una posición.

El caracter **^** en un *patrón regex* coincide con el comienzo de la cadena y el signo **$** coincide con el final de la *cadena*.

La mayoría de los motores *regex* tienen un modo "multilínea" que hace a **^** coincidir *después* de cualquier *salto de línea*, y a **$** *antes* de cualquier *salto de línea*.

> Por ejemplo, en la cadena **bob blub** el patrón **^b** solo coincide con la primera **b** de _**b**ob_ y el patrón **b$** solo coincide con la última **b** de _blu**b**_.

El caracter de anclaje **\\b** coincide en un límite de palabra.

Un límite de palabras es una posición entre un carácter que puede coincidir con **\\w** y un carácter que no puede ser igualado por **\\w** . El caracter **\\b** también coincide al principio y/o al final de la cadena si el primer y/o último caracteres de la cadena son *caracteres de palabra*.

El caracter **\\B** es la negación del anterior y  coincide en todas las posiciones donde **\\b** no puede coincidir.

### Alternancia

La alternancia es la expresión regular para las opciones de más de un caracter.

> El patrón **gato|perro** coincide con **gato** en *Sobre gatos y perros*. Si la expresión regular se aplica nuevamente, coincide con el **perro**.

Puede agregar tantas alternativas como desee: **gato|perro|ratón|pez**.

Debe agrupar las alternativas entre paréntesis **(opcion1|opcion2|etc.)** para usarlas normalmente en una expresión regular más compleja:

> Ejemplo, **Comida para (gato|perro)** coincidirá con **Comida para gato** y con **Comida para perro**. 

Esto se debe a que la *alternancia* tiene la precedencia más baja de todos los operadores de expresiones regulares, es decir que en el patrón (sin paréntesis) **Comida para gato|perro** las opciones definidas son **Comida para gato** por un lado y **perro** por el otro.

### Repetición

El signo de interrogación **?** hace que el *token* anterior en la expresión regular sea opcional.

> Por ejemplo, el patrón **patos?** coincide con **pato** o **patos**. Y el patrón **ob?scuridad** coincide con **obscuridad** tanto como con **oscuridad**.

El asterisco __*__ le dice al motor que intente hacer coincidir el *token* anterior *con cero o más veces*. La suma **+** le dice al motor que intente hacer coincidir el token anterior *una vez o más*. 

> Por ejemplo, el patrón __eh*__ coincidirá con **e**, **eh**, **ehh**, **ehhh**, etc. y el patrón **go+l** encontrará coincidencias en **gol**, **gool**, **goool**, etc. pero no en **gl**. 

Para especificar una cantidad específica de repeticiones se usan las llaves **{ }**.

> Usa el patrón **[0-9]{3}** para hacer coincidir con cualquier número entre **000**, o bien se puede usar [0-9]{2,4} para coincidir con cualquier número entre **00** y **9999**.

### Repetición codiciosa y perezosa

Los *operadores de repetición* o *cuantificadores* son **codiciosos**. Esto quiere decir que amplían la coincidencia tanto como pueden, y solo devuelven el *match* si deben satisfacer el resto de la expresión regular o si no queda nada por agregar a la coincidencia.

> Por ejemplo, el patrón **a+** coincidirá con **aaaa** en la cadena **aaaab**.

Coloque un signo de interrogación **?** *después del cuantificador* para que sea **perezoso**.

> Por ejemplo, el patrón **a+?** coincide con **a** en la cadena **aaaab**.

### Agrupando y capturando

Coloque paréntesis alrededor de múltiples tokens para agruparlos. A continuación, puede aplicar un cuantificador al grupo. Ej. Establecer ( Valor ) ? coincide con Set o SetValue .

Los paréntesis crean un grupo de captura. El ejemplo de arriba tiene un grupo. Después del partido, el grupo número uno no contiene nada si Set fue emparejado. Contiene valor si SetValue fue emparejado. Cómo acceder a los contenidos del grupo depende del software o del lenguaje de programación que esté utilizando. El grupo cero siempre contiene toda la coincidencia de expresiones regulares.

Use la sintaxis especial Set (?: Value ) ? para agrupar tokens sin crear un grupo de captura. Esto es más eficiente si no planea usar los contenidos del grupo. No confunda el signo de interrogación en la sintaxis del grupo que no captura con el cuantificador.

### Backreferences

Dentro de la expresión regular, puede usar la referencia inversa \ 1 para que coincida con el mismo texto que coincidió con el grupo de captura. ( [ abc ] ) = \ 1 coincide con a = a , b = b y c = c . No coincide con nada más. Si su expresión regular tiene múltiples grupos de captura, se numeran contando sus paréntesis de apertura de izquierda a derecha.

### Grupos nombrados y Backreferences

Si tu expresión regular tiene muchos grupos, hacer un seguimiento de sus números puede ser engorroso. Haga que sus expresiones regulares sean más fáciles de leer nombrando sus grupos. (? <mygroup> [ abc ] ) = \ k <mygroup> es idéntico a ( [ abc ] ) = \ 1 , excepto que puede hacer referencia al grupo por su nombre.

### Propiedades Unicode

\ p {L} coincide con un solo caracter que se encuentra en la categoría Unicode dada. L significa letra. \ P {L} coincide con un solo carácter que no está en la categoría Unicode dada. Puede encontrar una lista completa de categorías Unicode en el tutorial.

### Mirar alrededor (Lookaround)

Lookaround es un tipo especial de grupo. Los tokens dentro del grupo se emparejan normalmente, pero luego el motor de expresiones regulares hace que el grupo abandone su coincidencia y solo conserva el resultado. Lookaround coincide con una posición, al igual que los anclajes. No expande la coincidencia de expresiones regulares.

q (? = u ) concuerda con la q en cuestión , pero no en Iraq . Este es un avance positivo. Tú no eres parte de la coincidencia global de expresiones regulares. El lookahead coincide en cada posición de la cadena antes de a.

q (?! u ) coincide con q en Iraq, pero no en cuestión . Esto es un lookahead negativo. Se intentan las fichas dentro de la búsqueda anticipada, se descarta su coincidencia y el resultado se invierte.

Para mirar hacia atrás, use lookbehind. (? <= a ) b coincide con b en abc . Este es un aspecto positivo detrás. (? <! a ) b no coincide con abc .

Puede usar una expresión regular hecha y derecha dentro de lookahead. La mayoría de las aplicaciones solo permiten expresiones de longitud fija en lookbehind.
