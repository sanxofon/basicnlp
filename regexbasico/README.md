# Curso básico de expresiones regulares en español

Muchas aplicaciones y lenguajes de programación tienen su propia implementación de expresiones regulares, a menudo con diferencias leves y a veces significativas con respecto a otras implementaciones. Cuando dos aplicaciones usan una implementación diferente de expresiones regulares, decimos que usan diferentes "sabores" (*flavours*) de expresiones regulares. Trataré de explicar la sintaxis de los "sabores" más comunes.

## Patrones de texto y coincidencias

Una **expresión regular**, o *regex* para abreviar, es un patrón que describe una cierta cantidad de texto.

Una **coincidencia** es cuando la expresión regular se concontró en la cadena de búsqueda, la coincidencia es la porción de la cadena que coincide con el patrón.

Una **cadena** es un texto al cual se le aplicará la expresión regular.

Caracteres literales

La expresión regular más básica consiste en un único carácter literal, como **a** y la búsqueda de sólo la primera cincidencia en una cadena. Si la cadena es **Lupita es una niña**, la coincidencia será la **a** que está después de la **t**. Los programas que realizar expresiones regulares nos permiten recibir el caracter encontrado como respuesta, **a**, y/o la posición de la coincidencia, que en este caso sería **5**.

Esta expresión regular también puede coincidir con la segunda. Solo lo hace cuando le dice al motor de expresiones regulares que comience a buscar a través de la cadena después de la primera coincidencia. En un editor de texto, puede hacerlo utilizando su función "Buscar siguiente" o "Buscar hacia adelante". En un lenguaje de programación, generalmente hay una función separada a la que puede llamar para continuar buscando a través de la cadena después de la coincidencia anterior, que busca la última coincidencia o que permite buscar todas las coincidencias.

**Doce caracteres tienen significados especiales en las expresiones regulares:**

1. la barra invertida **\\** 
1. la línea **^** 
1. el signo de dólar **$** 
1. el punto o el punto **.** 
1. el símbolo de barra o tubo vertical **|** 
1. el signo de interrogación **?** 
1. el asterisco o estrella ***** 
1. el signo más **+** 
1. el paréntesis de apertura **(** 
1. el paréntesis de cierre **)** 
1. el corchete de apertura **[** 
1. y la llave de apertura **{** 

Estos caracteres especiales a menudo se llaman "metacaracteres". La mayoría de ellos son errores cuando se usan solos.

Si desea utilizar cualquiera de estos caracteres como un literal en una expresión regular, debe escapar de ellos con una barra invertida. Si quiere hacer coincidir 1 + 1 = 2 , la expresión regular correcta es 1 \ + 1 = 2 . De lo contrario, el signo más tiene un significado especial.

Aprenda más sobre los caracteres literales
Clases de caracteres o juegos de caracteres

Una "clase de caracteres" coincide solo con uno de varios caracteres. Para hacer coincidir una a o una e, usa [ ae ] . Puede usar esto en gr [ ae ] y para hacer coincidir gris o gris . Una clase de caracter solo coincide con un solo carácter. gr [ ae ] y no concuerda con graay , graey o cualquier cosa similar . El orden de los caracteres dentro de una clase de caracter no importa.

Puede usar un guion dentro de una clase de caracteres para especificar un rango de caracteres. [ 0 - 9 ] coincide con un solo dígito entre 0 y 9. Puede usar más de un rango. [ 0 - 9 a - f A - F ] coincide con un solo dígito hexadecimal, mayúsculas y minúsculas insensiblemente. Puede combinar rangos y caracteres individuales. [ 0 - 9 a - f x A - F X ] coincide con un dígito hexadecimal o la letra X.

Escribir una referencia después del corchete de apertura niega la clase de caracter. El resultado es que la clase de caracteres coincide con cualquier carácter que no esté en la clase de caracteres. q [ ^ x ] coincide con qu en cuestión . No coincide con Iraq ya que no hay un caracter después de la q para que coincida la clase de caracter negada.

Aprenda más sobre las clases de caracteres
Clases de caracteres abreviados

\ d coincide con un solo carácter que es un dígito, \ w coincide con un "carácter de palabra" (caracteres alfanuméricos más guion bajo) y \ s coincide con un carácter de espacio en blanco (incluye pestañas y saltos de línea). Los caracteres reales que coinciden con los atajos depende del software que está utilizando. En las aplicaciones modernas, incluyen letras y números que no son en inglés.

Aprenda más sobre las clases de caracteres abreviados
Caracteres no imprimibles

Puede usar secuencias de caracteres especiales para poner caracteres no imprimibles en su expresión regular. Utilice \ t para hacer coincidir un carácter de tabulación (ASCII 0x09), \ r para retorno de carro (0x0D) y \ n para avance de línea (0x0A). Los elementos no imprimibles más exóticos son \ a (campana, 0x07), \ e (escape, 0x1B), \ f (alimentación de formulario, 0x0C) y \ v (pestaña vertical, 0x0B). Recuerde que los archivos de texto de Windows usan \ r \ n para terminar líneas, mientras que los archivos de texto de UNIX usan \ n .

Si su aplicación es compatible con Unicode , use \ uFFFF o \ x {FFFF} para insertar un carácter Unicode. \ u20AC o \ x {20AC} coincide con el signo de moneda del euro.

Si su aplicación no es compatible con Unicode, use \ xFF para que coincida con un carácter específico por su índice hexadecimal en el juego de caracteres. \ xA9 coincide con el símbolo de copyright en el juego de caracteres Latin-1.

Todos los caracteres no imprimibles se pueden usar directamente en la expresión regular o como parte de una clase de caracteres.

Obtenga más información sobre los caracteres no imprimibles
El punto coincide (casi) con cualquier caracter

El punto coincide con un solo carácter, excepto los caracteres de salto de línea. La mayoría de las aplicaciones tienen un modo "punto coincide con todos" o "línea única" que hace que el punto coincida con cualquier carácter, incluidos los saltos de línea.

gr . y coincide con gris , gris , gr% y , etc. Utilice el punto con moderación. A menudo, una clase de caracter o clase de carácter negada es más rápida y más precisa.

Aprenda más sobre el punto
Anclajes

Los anclajes no coinciden con ningún caracter. Ellos coinciden con una posición. ^ coincide al comienzo de la cadena y $ coincidencias al final de la cadena. La mayoría de los motores regex tienen un modo "multilínea" que hace ^ coincidir después de cualquier salto de línea, y $ antes de cualquier salto de línea. Eg ^ b solo coincide con el primer b en bob .

\ b coincide en un límite de palabra. Un límite de palabras es una posición entre un carácter que puede coincidir con \ w y un carácter que no puede ser igualado por \ w . \ b también coincide al principio y / o al final de la cadena si el primer y / o último caracteres de la cadena son caracteres de palabra. \ B coincide en todas las posiciones donde \ b no puede coincidir.

Conozca más sobre anclajes
Alternancia

La alternancia es la expresión regular equivalente a "o". gato | el perro coincide con el gato en Sobre gatos y perros . Si la expresión regular se aplica nuevamente, coincide con el perro . Puede agregar tantas alternativas como desee: cat | perro | ratón | pez

La alternancia tiene la precedencia más baja de todos los operadores de expresiones regulares. gato | la comida para perros coincide con la comida para gatos o perros . Para crear una expresión regular que coincida con la comida para gatos o la comida para perros , debe agrupar las alternativas: ( cat | dog ) comida .

Aprenda más sobre la alternancia
Repetición

El signo de interrogación hace que el token anterior en la expresión regular sea opcional. colo tu ? r coincide con el color o el color .

El asterisco o estrella le dice al motor que intente hacer coincidir el token anterior con cero o más veces. La ventaja le dice al motor que intente hacer coincidir el token anterior una vez o más. < [ A - Z a - z ] [ A - Z a - z 0 - 9 ] * > coincide con una etiqueta HTML sin ningún atributo. < [ A - Z a - z 0 - 9 ] + > es más fácil de escribir, pero coincide con etiquetas no válidas como <1> .

Use llaves para especificar una cantidad específica de repetición. Use \ b [ 1 - 9 ] [ 0 - 9 ] {3} \ b para hacer coincidir un número entre 1000 y 9999. \ b [ 1 - 9 ] [ 0 - 9 ] {2,4} \ b coincide con un número entre 100 y 99999.

Conozca más sobre los cuantificadores
Repetición codiciosa y perezosa

Los operadores de repetición o cuantificadores son codiciosos. Amplían el partido tanto como pueden, y solo devuelven si deben satisfacer el resto de la expresión regular. La expresión regular < . + > coincide <EM> primero </ EM> en Esta es una <EM> primera </ EM> prueba .

Coloque un signo de interrogación después del cuantificador para que sea flojo. < . + ? > coincide con <EM> en la cadena anterior.

Una mejor solución es seguir mi consejo de usar el punto con moderación. Use < [ ^ <> ] + > para hacer coincidir rápidamente una etiqueta HTML sin tener en cuenta los atributos. La clase de caracteres negada es más específica que el punto, lo que ayuda al motor de expresiones regulares a encontrar coincidencias rápidamente.

Aprenda más sobre los cuantificadores codiciosos y perezosos
Agrupando y capturando

Coloque paréntesis alrededor de múltiples tokens para agruparlos. A continuación, puede aplicar un cuantificador al grupo. Ej. Establecer ( Valor ) ? coincide con Set o SetValue .

Los paréntesis crean un grupo de captura. El ejemplo de arriba tiene un grupo. Después del partido, el grupo número uno no contiene nada si Set fue emparejado. Contiene valor si SetValue fue emparejado. Cómo acceder a los contenidos del grupo depende del software o del lenguaje de programación que esté utilizando. El grupo cero siempre contiene toda la coincidencia de expresiones regulares.

Use la sintaxis especial Set (?: Value ) ? para agrupar tokens sin crear un grupo de captura. Esto es más eficiente si no planea usar los contenidos del grupo. No confunda el signo de interrogación en la sintaxis del grupo que no captura con el cuantificador.

Obtenga más información sobre cómo agrupar y capturar
Backreferences

Dentro de la expresión regular, puede usar la referencia inversa \ 1 para que coincida con el mismo texto que coincidió con el grupo de captura. ( [ abc ] ) = \ 1 coincide con a = a , b = b y c = c . No coincide con nada más. Si su expresión regular tiene múltiples grupos de captura, se numeran contando sus paréntesis de apertura de izquierda a derecha.

Obtenga más información acerca de las referencias posteriores
Grupos nombrados y Backreferences

Si tu expresión regular tiene muchos grupos, hacer un seguimiento de sus números puede ser engorroso. Haga que sus expresiones regulares sean más fáciles de leer nombrando sus grupos. (? <mygroup> [ abc ] ) = \ k <mygroup> es idéntico a ( [ abc ] ) = \ 1 , excepto que puede hacer referencia al grupo por su nombre.

Aprenda más sobre grupos nombrados
Propiedades Unicode

\ p {L} coincide con un solo caracter que se encuentra en la categoría Unicode dada. L significa letra. \ P {L} coincide con un solo carácter que no está en la categoría Unicode dada. Puede encontrar una lista completa de categorías Unicode en el tutorial.

Obtenga más información sobre las expresiones regulares de Unicode
Mira alrededor

Lookaround es un tipo especial de grupo. Los tokens dentro del grupo se emparejan normalmente, pero luego el motor de expresiones regulares hace que el grupo abandone su coincidencia y solo conserva el resultado. Lookaround coincide con una posición, al igual que los anclajes. No expande la coincidencia de expresiones regulares.

q (? = u ) concuerda con la q en cuestión , pero no en Iraq . Este es un avance positivo. Tú no eres parte de la coincidencia global de expresiones regulares. El lookahead coincide en cada posición de la cadena antes de a.

q (?! u ) coincide con q en Iraq, pero no en cuestión . Esto es un lookahead negativo. Se intentan las fichas dentro de la búsqueda anticipada, se descarta su coincidencia y el resultado se invierte.

Para mirar hacia atrás, use lookbehind. (? <= a ) b coincide con b en abc . Este es un aspecto positivo detrás. (? <! a ) b no coincide con abc .

Puede usar una expresión regular hecha y derecha dentro de lookahead. La mayoría de las aplicaciones solo permiten expresiones de longitud fija en lookbehind.

Conozca más sobre lookaround
Sintaxis de espaciado libre

Muchas aplicaciones tienen una opción que puede denominarse "espacio libre" o "ignorar espacios en blanco" o "comentarios" que hace que el motor de expresiones regulares ignore los espacios no escaneados y los saltos de línea, lo que hace que el carácter # inicie un comentario que se ejecuta hasta el final de la línea. Esto le permite usar espacios en blanco para formatear su expresión regular de manera que sea más fácil de leer para los humanos y, por lo tanto, sea más fácil de mantener. 