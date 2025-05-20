"""
-----------------------------------------------------
Ejercicio 28: Secuencia de pares hasta N
-----------------------------------------------------
Enunciado:  
Escribir un algoritmo que permita imprimir la siguiente sucesión. Considere que N es un número par, que se 
ingresa.        
 
2   4   6    8  ...  N 
4   6   8  10  ...  N 
6   8  10  12 ...  N 
.... 
.... 
N

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_28 ES 
    AMBIENTE 
        N,i: Entero
        secuencia: Alfanumerico
    PROCESO
        Escribir("Este algoritmo devuelve una sucesion de N")
        Escribir("Ingrese un número par: ")
        Leer(N)
        Si N MOD 2 <> 0 Entonces
            Escribir("El número no es par.")
        Sino
            Para i:=2 Hasta N; 2 Hacer
                secuencia:=i
                Para j:=i Hasta N Con Paso 2 Hacer
                    secuencia:=secuencia+" "+j
                FinPara
                Escribir(secuencia)
            FinPara
        FinSi
        
FIN_ACCION

"""

def main():
    print("Este algoritmo devuelve una sucesion de N")
    N = int(input("Ingrese un número par: "))
    if N % 2 != 0:
        print("El número no es par.")
    else:
        for i in range(2, N + 1, 2):
            secuencia=str(i)
            for j in range(i+2, N + 1, 2):
                secuencia+=" "+str(j)
            print(secuencia)
            
if __name__ == "__main__":
    main()
