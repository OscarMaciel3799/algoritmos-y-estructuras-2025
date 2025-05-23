"""
-----------------------------------------------------
Ejercicio 32.10: Mostrar números gigantes por pantalla
-----------------------------------------------------
Enunciado:  
Escribir un único procedimiento "mostrar_nro" que reciba como parámetro un dígito y lo muestre por pantalla 
de la misma forma que se indica en el ejercicio 9. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_0 ES 
    AMBIENTE 
        num: Entero
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
        Escribir("Este algoritmo muestra un número elegido en tamaño gigante")
        Escribir("Ingrese un número")
        Leer(num)
        Segun num hacer
            0:mostrar_0()
            1:mostrar_1()
            2:mostrar_2()
            3:mostrar_3()
            4:mostrar_4()
            5:mostrar_5()
            6:mostrar_6()
            7:mostrar_7()
            8:mostrar_8()
            9:mostrar_9()
        Fin_Segun
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
def numero_gigante(n):
    match n:
        case 0:
            return mostrar_0()
        case 1:
            return mostrar_1()
        case 2:
            return mostrar_2()
        case 3:
            return mostrar_3()
        case 4:
            return mostrar_4()
        case 5:
            return mostrar_5()
        case 6:
            return mostrar_6()
        case 7:
            return mostrar_7()
        case 8:
            return mostrar_8()
        case 9:
            return mostrar_9()             
if __name__ == "__main__":
    print("Este algoritmo muestra un número elegido en tamaño gigante")
    num=int(input("Ingrese un número: "))
    
    print(numero_gigante(num))
    
