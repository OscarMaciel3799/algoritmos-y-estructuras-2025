"""
-----------------------------------------------------
Ejercicio 32.09: Mostrar números gigantes por pantalla
-----------------------------------------------------
Enunciado:  
Desarrollar los procedimientos mostrar_0, mostrar_1,..., mostrar_9 que visualicen por pantalla, 
respectivamente, los números 0,1,...,9 en tamaño grande, tal y como se muestra a continuación: 

* * * *    *    * * * *   * * * *   *     *   * * * *   * * * *   * * * *   * * * *   * * * *
*     *    *          *         *   *     *   *         *               *   *     *   *     *
*     *    *    * * * *   * * * *   * * * *   * * * *   * * * *         *   * * * *   * * * *
*     *    *    *               *         *         *   *     *         *   *     *         *
* * * *    *    * * * *   * * * *         *   * * * *   * * * *         *   * * * *   * * * *

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_9 ES 
    AMBIENTE 
        Procedimiento mostrar_0() es
            Escribir("* * * *")
            Escribir("*     *")
            Escribir("*     *")
            Escribir("*     *")
            Escribir("* * * *")
        Fin_Procedimiento
        Procedimiento mostrar_1() es
            Escribir("*")
            Escribir("*")
            Escribir("*")
            Escribir("*")
            Escribir("*")
        Fin_Procedimiento
        Procedimiento mostrar_2() es
            Escribir("* * * *")
            Escribir("      *")
            Escribir("* * * *")
            Escribir("*      ")
            Escribir("* * * *")
        Fin_Procedimiento
        Procedimiento mostrar_3() es
            Escribir("* * * *") 
            Escribir("      *")
            Escribir("* * * *")
            Escribir("      *")
            Escribir("* * * *")
        Fin_Procedimiento
        Procedimiento mostrar_4() es
            Escribir("*     *")
            Escribir("*     *")
            Escribir("* * * *")
            Escribir("      *")
            Escribir("      *")
        Fin_Procedimiento
        Procedimiento mostrar_5() es
            Escribir("* * * *")
            Escribir("*      ")
            Escribir("* * * *")
            Escribir("      *")
            Escribir("* * * *")
        Fin_Procedimiento
        Procedimiento mostrar_6() es
            Escribir("* * * *")
            Escribir("*      ")
            Escribir("* * * *")
            Escribir("*     *")
            Escribir("* * * *")
        Fin_Procedimiento
        Procedimiento mostrar_7() es
            Escribir("* * * *")
            Escribir("      *")
            Escribir("      *")
            Escribir("      *")
            Escribir("      *")
        Fin_Procedimiento
        Procedimiento mostrar_8() es
            Escribir("* * * *")
            Escribir("*     *")
            Escribir("* * * *")
            Escribir("*     *")
            Escribir("* * * *")
        Fin_Procedimiento
        Procedimiento mostrar_9() es
            Escribir("* * * *")
            Escribir("*     *")
            Escribir("* * * *")
            Escribir("      *")
            Escribir("* * * *")
        Fin_Procedimiento
    PROCESO
        Escribir("Este algoritmo muesta números gigantes por pantalla")
        Escribir(mostrar_0(),mostrar_1(),mostrar_2(),mostrar_3(),mostrar_4(),mostrar_5(),mostrar_6(),mostrar_7(),mostrar_8(),mostrar_9())
        
FIN_ACCION

"""

def mostrar_0():
    numero_0 = [
        "* * * *",
        "*     *",
        "*     *",
        "*     *",
        "* * * *"
    ]
    return "\n".join(numero_0)

def mostrar_1():
    numero_1 = [
        "*",
        "*",
        "*",
        "*",
        "*"
    ]
    return "\n".join(numero_1)

def mostrar_2():
    numero_2 = [
        "* * * *",
        "      *",
        "* * * *",
        "*      ",
        "* * * *"
    ]
    return "\n".join(numero_2)
    
def mostrar_3():
    numero_3 = [
        "* * * *",
        "      *",
        "* * * *",
        "      *",
        "* * * *"
    ]
    return "\n".join(numero_3)

def mostrar_4():
    numero_4 = [
        "*     *",
        "*     *",
        "* * * *",
        "      *",
        "      *"
    ]
    return "\n".join(numero_4)

def mostrar_5():
    numero_5 = [
        "* * * *",
        "*      ",
        "* * * *",
        "      *",
        "* * * *"
    ]
    return "\n".join(numero_5)

def mostrar_6():
    numero_6 = [
        "* * * *",
        "*      ",
        "* * * *",
        "*     *",
        "* * * *"
    ]
    return "\n".join(numero_6)

def mostrar_7():
    numero_7 = [
        "* * * *",
        "      *",
        "      *",
        "      *",
        "      *"
    ]
    return "\n".join(numero_7)
            
def mostrar_8():
    numero_8 = [
        "* * * *",
        "*     *",
        "* * * *",
        "*     *",
        "* * * *"
    ]
    return "\n".join(numero_8)
    
        
def mostrar_9():
    numero_9 = [
        "* * * *",
        "*     *",
        "* * * *",
        "      *",
        "* * * *"
    ]
    return "\n".join(numero_9)
            
if __name__ == "__main__":
    print("Este algoritmo ....")
    print(mostrar_0())
    print("       ")
    print(mostrar_1())
    print("       ")
    print(mostrar_2())
    print("       ")
    print(mostrar_3())
    print("       ")
    print(mostrar_4())
    print("       ")
    print(mostrar_5())
    print("       ")
    print(mostrar_6())
    print("       ")
    print(mostrar_7())
    print("       ")
    print(mostrar_8())
    print("       ")
    print(mostrar_9())
        
