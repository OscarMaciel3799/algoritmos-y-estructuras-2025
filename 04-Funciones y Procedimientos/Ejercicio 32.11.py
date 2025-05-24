"""
-----------------------------------------------------
Ejercicio 32.11: Calculadora
-----------------------------------------------------
Enunciado:  
Diseñe un algoritmo que muestre un menú con las opciones sumar, restar, multiplicar y dividir, el algoritmo 
solicitará una opción y realizará la tarea elegida, se debe usar un procedimiento para mostrar el menú, pedir los datos 
en el algoritmo principal y después usar funciones para realizar los cálculos. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_32.11 ES 
    AMBIENTE 
        num1,num2: Real
        opciones:(1,2,3,4)
        Procedimiento Menu() Es
            Escribir("Elija la operación que desea realizar:")
            Escribir("1 - Suma")
            Escribir("2 - Resta")
            Escribir("3 - Multiplicación")
            Escribir("4 - Division")
        Fin_Procedimiento
        Funcion suma(n1,n2: Real):Real Es
            suma:=n1+n2
        Fin_Funcion
        Funcion restar(n1,n2: Real):Real Es
            restar:=n1-n2
        Fin_Funcion
        Funcion multiplicacion(n1,n2: Real):Real Es
            multiplicacion:=n1*n2
        Fin_Funcion
        Funcion division(n1,n2: Real):Real Es
            division:=n1/n2
        Fin_Funcion
    PROCESO
        Escribir("Este algoritmo permite hacer los siguientes cálculos sumar, restar, multiplicar y dividir")
        Menu()
        Leer(opcion)
        Escribir("Ingrese los dos números que desea operar")
        Leer(num1,num2)
        Segun opcion hacer
            1: suma(num1,num2)
            2: resta(num1,num2)
            3: multiplicacion(num1,num2)
            4: division(num1,num2)
        Fin Segun
FIN_ACCION

"""
def Menu():
    menu_opciones = [
    "Elija la operación que desea realizar:",
    "1 - Suma",
    "2 - Resta",
    "3 - Multiplicación",
    "4 - Division",
    ""
    ]
    return "\n".join(menu_opciones)

def suma(n1,n2):
        return n1+n2
        
def resta(n1,n2):
    return n1-n2
        
def multiplicacion(n1,n2):
    return n1*n2
            
def division(n1,n2):
    return n1/n2


def opciones(n):
        match n:
            case 1:
                return suma(num1,num2)
            case 2:
                return resta(num1,num2)
            case 3:
                return multiplicacion(num1,num2)
            case 4:
                return division(num1,num2)
                   
if __name__ == "__main__":
    print("Este algoritmo permite hacer los siguientes cálculos sumar, restar, multiplicar y dividir")
    opcion=int(input(Menu()))
    num1,num2=map(float,input("Ingrese los dos números que desea operar separados por un espacio: ").split())
    print("El resultado de la operacion es: ",opciones(opcion))
    
            