"""
-----------------------------------------------------
Ejercicio 32.01: Devolver el cuadrado de un número
-----------------------------------------------------
Enunciado:  
Realice una función que dado un número devuelva su cuadrado. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1 ES 
    AMBIENTE 
        num: Entero
        Funcion cuadrado es (n: Entero):Entero Es
            cuadrado:=n**2
        Fin_Funcion
    PROCESO
        Escribir("Este algoritmo devuelve el cuadrado de un número")
        Escribir("Ingrese un número entero: ")
        Leer(num)
        Escribir("El cuadrado del número ",num," es: ",cuadrado(num))
FIN_ACCION

"""

def cuadrado(n):
    n=n**2
    return n
            
if __name__ == "__main__":
    print("Este algoritmo devuelve el cuadrado de un número")
    num=int(input("ingrese un número entero: "))
    print("El cuadrado del número ",num," es: ",cuadrado(num))
