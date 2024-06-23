# para saber de que tipo es cada objeto uso < type(objeto) >
sumaEnteros = 1 + 80
print(sumaEnteros, "\t", type(sumaEnteros))

sumaReales = 1.5 + 78
print(sumaReales, "\t", type(sumaReales))

##################################################################
####################    ARITMETICA   #############################
##################################################################
"""
OBTENER PARTE ENTERA DE UNA DIVISION:
    Se usa doble slash '//' para que python no tenga en cuenta
    los decimales
"""
division1 = 167 / 3
# es del tipo float
print(division1, type(division1))

division2 = 167 // 3
# es del tipo int
print(division2, type(division2))


##################################################################
########################     STRINGS      ########################
##################################################################
"""
    Los string son IMUTABLES.

    Cuando se esta trabajando con string y quiere operarse con multiplicacion
    Python lo que realiza es la repetisicion del string tantas veces
    como se haya indicado.

    Cuando al string lo precede una 'b' se esta tratando de una cadena
    almacenada como bit
"""
pruebaString = "Hola"
print(pruebaString * 5)

print(pruebaString[2])

# como es inmutable no se puede modificar
# error: pruebaString[0] = 'C'
prueba2String = "C" + pruebaString[1:]
print(prueba2String)

# para conocer como funcionan los metodos, puedo recurrir a <help(obj.metodo)>
prueba3String = "Hola"
help(prueba3String.find)

"""
MODIFICAR UN STRING:
    Una forma de modificar un string es convertilor a una lista, modificar
    el valor/elemento que se desea modificar, y volver a convertir
    la lista a string
"""
# al final del nombre existe una T que no deberia existir
mi_string = "AgustinT Admetlla"
lista = list(mi_string)
print(lista)

# se remueve el valor que no se de sea
lista.remove("T")
print(lista)


##################################################################
######################      CRASHEAR        ######################
##################################################################
pruebaString = "72"
esUnEntero = 8
print(int(pruebaString) + esUnEntero)


##################################################################
########################      LISTAS      ########################
##################################################################
"""
REFERENCIA LISTAS EN OTROS OBJETOS:
    Cuando se referencia a una lista desde otro objeto, se estan copiando
    los elementos de lista1 en lista2. Cuando se modifica lista1 lo valores
    de referencia que posee lista2 se actualizan, sin embargo cuando se
    modifica/cambia el elemento que almacena lista1, lista2 se quedara con el
    elemento viejo, generando que ambos objetos sean distintos.
"""
lista1 = "prueba"
lista2 = lista1
# se mantienen igual
print(lista1, lista2)

lista1 = 73
# ahora se presenta la diferencia de ambiguedad
print(lista1, lista2)

# en este intercambio se modifica uno de los valores
lista1 = ["hola", "prueba", 3]
lista2 = lista1
print(lista1, lista2)

lista1[0] = "Ahora anda"
print(lista1, lista2)

"""
COPIANDO LISTAS EN OTROS OBJETOS:
    De esta manera lista2 siempre matendra un unico valor, sin verse alterado
"""
import copy

lista1 = ["hola", "prueba", 3]
lista2 = copy.copy(lista1)

print(lista1, lista2)

lista1[0] = "Cambio de planes"
print(lista1, lista2)


##################################################################
###################     VARIABLES GLOBALES     ###################
##################################################################
"""
    Para poder modificar el valor de una variables global, existen varias
    alternativas:
    1. modificar el valor de una variable global a nvl modulo
    2. modificar el valor de una variable global a nivel funcion
    3. modificar el valor de una variable global a nivel funcion
        dentro de otra funcion, sin alterar el valor original.
"""
####### CASO 1
nivel_0 = 0  # fuera del modulo


def funcion_1():
    nivel_1 = 1  # dentro del modulo nvl1

    print("dentro del nivel 1: ", nivel_0, "\n")

    def funcion_2():
        # para modificar una variable fuera del modulo se usa 'global'
        global nivel_0

        nivel_2 = 2  # dentro del modulo nvl2

        print(nivel_0, "\t", nivel_1, "\t", nivel_2)

        nivel_0 = 10

    funcion_2()
    print(nivel_0, "\t", nivel_1)


funcion_1()
print(nivel_0)

####### CASO 2
nivel_0 = 0  # fuera del modulo


def funcion_1():
    nivel_1 = 1  # dentro del modulo nvl1

    def funcion_2():
        # para modificar una variable global, que esta dentro de una funcion
        # y se quiere modificar permanentemente su valor, se usa la 'nonlocal'
        nonlocal nivel_1
        nivel_1 = 99
        nivel_2 = 2  # dentro del modulo nvl2

        print(nivel_0, "\t", nivel_1, "\t", nivel_2)

    funcion_2()

    print(nivel_0, "\t", nivel_1)


funcion_1()
print(nivel_0)

####### CASO 3 modificacion de valores dentro de la funcion
####### sin modificar el valor original
nivel_0 = 0  # fuera del modulo


def funcion_1():
    nivel_1 = 1  # dentro del modulo nvl1

    def funcion_2():
        # para modificar una variable global dentro de una funcion que
        # la usa y no se quiere alterar el valor original
        # se utiliza 'global'
        global nivel_1
        nivel_1 = 99
        nivel_2 = 2  # dentro del modulo nvl2

        print(nivel_0, "\t", nivel_1, "\t", nivel_2)

    funcion_2()

    print(nivel_0, "\t", nivel_1)


funcion_1()
print(nivel_0)

##################################################################
######################     RECURSIVIDAD     ######################
##################################################################


def miSuma(lista):
    print(lista)

    if lista:
        return lista[0] + miSuma(lista[1:])
    else:
        return 0


print(miSuma([1, 2, 3, 4, 5]))
"""
:: RETORNO: print(miSuma([1, 2, 3, 4, 5]))
    - ingreso (1) a funcion miSuma
        lista = [1, 2, 3, 4, 5]    
    - print: 
        1, 2, 3, 4, 5
    - ingreso condicion if :: lista == ¿lista contiene algo? TRUE/FALSE
    - return TRUE:
        lista[0] = 1
        acumula 1 + miSuma(lista[1:]) == 1 + miSuma([2, 3, 4, 5])
        - llama funcion miSuma
    
    - ingreso (2) a funcion miSuma
        lista = [2, 3, 4, 5]
    - print: 
        2, 3, 4, 5
    - ingreso condicion if :: lista == ¿lista contiene algo? TRUE/FALSE
    - return TRUE:
        lista[0] = 2
        acumula 1 + 2 + miSuma(lista[1:]) == 1 + n... + miSuma([3, 4, 5])
        - llama funcion miSuma

    - ingreso (3) a funcion miSuma
        lista = [3, 4, 5]
    - print: 
        3, 4, 5
    - ingreso condicion if :: lista == ¿lista contiene algo? TRUE/FALSE
    - return TRUE:
        lista[0] = 3
        acumula 1 + 2 + 3 + miSuma(lista[1:]) == 1 + n... + miSuma([4, 5])
        - llama funcion miSuma
    
    - ingreso (4) a funcion miSuma
        lista = [4, 5]
    - print: 
        4, 5
    - ingreso condicion if :: lista == ¿lista contiene algo? TRUE/FALSE
    - return TRUE:
        lista[0] = 4
        acumula 1 + 2 + 3 + 4 
            + miSuma(lista[1:]) == 1 + n... + miSuma([5])
        - llama funcion miSuma

    - ingreso (5) a funcion miSuma
        lista = [5]
    - print: 
        5
    - ingreso condicion if :: lista == ¿lista contiene algo? TRUE/FALSE
    - return TRUE:
        lista[0] = 5
        acumula 1 + 2 + 3 + 4 + 5
            + miSuma(lista[1:]) == 1 + n... + miSuma([])
        - llama funcion miSuma

    - ingreso (6) a funcion miSuma
        lista = []
    - print: 
        
    - ingreso condicion if :: lista == ¿lista contiene algo? TRUE/FALSE
    - return FALSE:
            acumula 1 + 2 + 3 + 4 + 5 + 0

    - vuelve al primer llamado de miSuma donde va a mostrar el total
        acumulado: 15, y lo imprime porque se retorna el valor y 
        fue llamado desde un print
"""


##################################################################
################     INFORMACION DE OBJETOS     ################
##################################################################
def miSuma(lista):
    print(lista)

    if lista:
        return lista[0] + miSuma(lista[1:])
    else:
        return 0


print("NOMBRE DE LA FUNCION: ", "#" * 15)
nombFunc = str(miSuma.__name__)
print(nombFunc)
print("\n", "#" * 15)

print("\nObtengo La CLASE PADRE de: ", nombFunc, "#" * 15)
print(miSuma.__class__.__base__)
print("\n", "#" * 15)

print("\VERIFICO SI ES OBJETO DE UNA CLASE: ", "#" * 15)
print(miSuma.__class__)
print("\n", "#" * 15)

print("\nObtengo los METODOS ASOCIADOS la clase: ", nombFunc, "#" * 15)
print(dir(miSuma))
print("\n", "#" * 15)

print("\nObtengo datos de la funcion: ", "#" * 15)
print(miSuma.__code__)
print("\n", "#" * 15)

print("\nObtengo nombre de variables usadas: ", "#" * 15)
print(miSuma.__code__.co_varnames)
print("\n", "#" * 15)

print("\nObtengo cantidad de argumentos: ", "#" * 15)
print(miSuma.__code__.co_argcount)


##################################################################
#####################     FUNCION LAMBDA     #####################
##################################################################

"""
SINTAXIS:
    lambda argumento1,argumento1,...,argumentoN: expresion
"""
# se pueden definiar variables que cumplan la tarea de funciones
def Sumar(a, b):
    return a + b


sumarNumeros = lambda num1, num2: num1 + num2

print(sumarNumeros(1, 2))
