"""
LLAMAS DE RETORNO:
    Se puede realizar la llamada a una funcion de forma dinamica, esto
    quiere decir, desconociendo su nombre.

    Para poder llamar a una funcion de forma dinamica, se utilizan 2 
    funciones nativas: locals() y globals(). Ambas funciones retornan
    un diccionario.
        locals() se compone de todos los elementos de ambito local
        globals() se compone de los elementos a nivel global


CORROBORAR QUE LA FUNCION EXISTA:
    Como pueden estar mal escritas las llamdas a funcion o no existir, se
    deben corroborar. Ejemplo:

        if nomb_func in locals():
            if callable(locals()[nomb_func]):
                # sentencias

    in       -> Permite conocer si un elemento se encuentra dentro de 
                una coleccion

    callable -> El método callable() toma solo un argumento, 
                un objeto y devuelve uno de los dos valores:

                1. true, si el objeto parece ser invocable.
                2. cuando el objeto no es invocable.

"""


def imprimir_cadena(nombre, apellido):
    return "Bienvenido " + nombre + " " + apellido


def llamar_funcion(nomb_func, *args):
    # llamada de retorno a nivel global

    if nomb_func in globals():
        if callable(globals()[nomb_func]):
            return globals()[nomb_func](args[0], args[1])
    else:
        return "Funcion no encontrada"


print(llamar_funcion("imprimir_cadena", "Agustin", "Admetlla"))

# llamada retorno a nivel local
nomb_func = "imprimir_cadena"

if nomb_func in locals():
    if callable(locals()[nomb_func]):
        print(locals()[nomb_func]("Rocio", "Admetlla"))
