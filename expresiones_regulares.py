"""
    Una expresion regular es un conjunto de caracteres que forman un
    patron de busqueda.

    Para poder utilizar las expresiones regulares, se debe importar
    el modulo 're'; y utilizar los metodos:
        compile(): para agarrar la expresion regular
        match(): para comparar la expresion regular con el string donde
                 se quiere aplicar la expresion regular
"""
import re

patron = re.compile("p+")

lista = ["pera", "vfg"]

# el patron encuentra una coincidencia 'p' en el primer elemento
print(patron.match(lista[0]))

# no existe coincidencia
print(patron.match(lista[1]))

"""
EXISTEN 3 TIPOS DE EXPRESION REGULAR:
    POSIX: 
        es la que utiliza barras inclinadas

    PCRE: 
        usa clases [a-zA-Z0-9]

    BANDERAS: 
        utiliza banderas del <modulo re> de Python, es una forma
        particular solo de python

------------------------- 0 -------------------------

CARACTERES:
    Los caracteres son simbolos que funcionan como comodin. Cuando estan
    acompañadas de simbolos como '+' se le da a los caracteres un 
    significado, en este caso que se indica que el caracter se puede repetir
    mas de una vez

CLASES:
    Es cuando en un patron se encuentran corchetes. Se lo conoce como 
    Clase Caracter. Ejemplo:
        [aeiu]uto   -> especifica que dicho conjunto de letras, se puede
                       encontrar delante de 'uto'
        a[up]to     -> coincide con 'aUto' o 'aPto'

RANGOS:
    Para determinar rangos, se utiliza dentro de los corchetes, un guion

    [0-9]   -> digitos del 0 al 9
    [a-z]   -> caracteres minuscula de 'a' a la 'z'
    [A-Z]   -> caracteres mayuscula de A a la Z
    [a-z-A-Z]   -> caracteres de A a Z en MAY o MIN

META-CARACTERES:
    - El meta caracter \ puede ir seguida de varios caracteres para indicar
    secuencias especiales. Incluyen alternativas, repeticiones del
    patron los cuales son interpretados. A demas de tambien servir para
    que en la busqueda de caracteres concretos como el de clase '[' sean
    textual

    Expresión       Definición
    \A  ----------->Coincide sólo al comienzo de la cadena
    \b  ----------->Marca la posicion de una palabra limitada por espacios
                    en blanco, puntuacion o el inicio/final de una cadena
    \d  ----------->Coincide con cualquier digito decimal; es quivalente 
                    a escribir [0-9]
    \D  ----------->Coincide con cualquier digito que no sea un decimal,
                    esto equivale a la clase [^ 0-9]
    \s  ----------->Coincide con cualquier caracter de espacio en blanco, 
                    esto es equivalente a [\ t \ n \ r \ f \ v]
    \S  ----------->Coincide con cualquier caracter que no sea una
                    espacio en blanco, equivalente a
                    [^ \ t \ n \ r \ f \ v]
    \w  ----------->Coincide con cualquier caracter alfanumerico, 
                    equivalente a [a-zA-Z0-9_]
    \W  ----------->Coincide con cualquier caracter que no sea alfanumerico
                    equivalente a [^ a-zA-Z0-9_]


    - El meta caracter ^ denominado circunflejo tiene 2 usos:
    FUERA DE UNA CLASE CARACTER: 
        Indica que para que la comparacion sea verdadera la declaracion, 
        condicion o busqueda debe empezar con dicha condicion
    DENTRO DE UNA CLASE CARACTER:
        <<<<No se entiende la teoria, pesimo>>>>


    - El meta caracter $ indica que una declaracion sera verdadera
    siempre que la cadena a comparar finalice con el patron indicado.


    - El metacaracter |, barra vertical, sirve para separar patrones
    alternativos. Ejemplo:
            patron = re.compile('pera''|manzana')

------------------------- 0 -------------------------

REPETICION:
    La repeticion se especifica mediante cuantificadores:
    Ejemplo:
        z{2,4}      -> indica que z puede repetirse desde 2 veces a 4.
                    'zz' 'zzz' o 'zzzz'
        [aeiou]{3,} -> indica que coincide con 3 o mas vocales sucesivas

        \d{8}       -> indica que coincide con 8 digitos exactos

    CUANTIFICADORES DE CARACTER SIMPLE:
        *           ->  equivale a {0,}
        +           ->  equivale a {1,}
        ?           ->  equivale a {0,1}

    EJEMPLOS:
        colou?r                  identifica 'colour' o 'color'
        \b[1-9][0-9]{3}\b        Identifica un número entre 1000 y 9999
        \b[1-9][0-9]{2,4}\b      Identifica un número entre 100 y 99999
        <[A-Za-z][A-Za-z0-9]*>   Identifica una etiqueta html sin atributos
        <[A-Za-z0-9]+>           Puede identificar etiquetas <1>

------------------------- 0 -------------------------

SUB-PATRONES:
    Si dentro de un sub patron () se incluye el signo de interrogacion (?)
    el caracter siguiente al signo determina un significado y sintaxis.

    (?aiLmsux)
    (Una o más letras del conjunto 'a', 'i', 'L', 'm', 's', 'u', 'x'.) 
    El grupo coincide con la cadena vacía; las letras establecen los 
    indicadores correspondientes:
        - re.A (coincidencia sólo ASCII)
        - re.I (ignorar mayúsculas y minúsculas)
        - re.L (depende del entorno local)
        - re.M (multilínea), re.S (el punto coincide con todos) 
        - re.U (coincidencia de Unicode) 
        - re.X (verbose), para toda la expresión regular

    USO DE FLAG:
        En el caso de utilizar un flag (?:...) dentro de una expresion,
        este se aplica solamente a la expresion contenida dentro de los
        parentesis, y no a las expresiones externas.
        Ejemplo:
            patron = re.compile(r'(?i:pera) y manzana')

PAGINA PARA CORROBORAR PATRONES:
    https://regex101.com/

>>>>>>>>>>>>>>>>>>>> RESTO DE TEORIA EN CUADERNILLO <<<<<<<<<<<<<<<<<<<<<

"""
