"""
-----------------------------------------------------
Ejercicio 32.03: Menor valor
-----------------------------------------------------
Enunciado:  
Diseñe una función que permita ingresar 3 números y devuelva el mínimo valor. El programa principal debe 
permitir que este proceso se repita la cantidad de veces que el usuario desee. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_3 ES 
    AMBIENTE 
        num1,num2,num3: Entero
        seguir:(S,N)
        Funcion menor (n1,n2,n3: Entero): Entero Es
            SI n1<n2 y n1<n3 entonces
                menor:= n1
            SINO
                SI n2<n1 y n2<n3 entonces
                    menor:=n2
                SINO
                    menor:=n3
                Fin_Si
            Fin_SI
        Fin_Funcion
    PROCESO
        Escribir("Este algoritmo devuelve el menor de 3 números")
        Escribir("Desea ingresar la primer terna de números? S para Si, N para NO")
        Leer(seguir)
        Mientras seguir='S' hacer
            Escribir("Ingrese los tres números:")
            Leer(ni,n2,n3)
            Escribir("El menor de los tres números es :",menor(n1,n2,n3))
            Escribir("Desea ingresar otra terna? S para SI, N para NO")
            Leer(seguir)
        Fin_Mientras
FIN_ACCION

"""

def menor(n1,n2,n3):
    if n1<n2 and n1<n3:
        return n1
    elif n2<n1 and n2<n3:
        return n2
    else:
        return n3
            
if __name__ == "__main__":
    print("Este algoritmo devuelve el menor de 3 números")
    seguir=str(input("Desea ingresar la primer terna de números? S para Si, N para NO: "))

    while seguir=="S":
        num1,num2,num3=map(int,input("Ingrese los tres números separados por espacios: ").split())
        print("El menor de los tres números es :",menor(num1,num2,num3))
        seguir=str(input("Desea ingresar otra terna? S para SI, N para NO: "))