"""
-----------------------------------------------------
Ejercicio 29: Secuencia de pares hasta 2
-----------------------------------------------------
Enunciado:  
Escribir un algoritmo que permita imprimir la siguiente sucesión. Considere que N es un número par, que se 
ingresa.               
2   4   6   ................  N 
2   4   6   ..........  N-2 
2   4   6   ...  N-4 
............ 
2   4   6    
2   4    
2 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_29 ES 
    AMBIENTE 
        N,i: Entero
        secuencia: Alfanumerico
    PROCESO
        Escribir("Ingrese un número par: ")
        Leer(N)
        Si N MOD 2 <> 0 Entonces
            Escribir("El número no es par.")
        Sino
            Para i:=N Hasta 2; -2 Hacer
            secuencia:="2"
                Para j:=4 Hasta i;2 Hacer
                    secuencia:=secuencia+" "+j
                FinPara
                Escribir(secuencia)
            FinPara
        FinSi
FIN_ACCION

"""

def main():
    N = int(input("Ingrese un número par: "))
    if N % 2 != 0:
        print("El número no es par.")
    else:
        for i in range(N, 1 - 1, -2):
            secuencia=str(2)
            for j in range(4, i + 1, 2):
                secuencia+=" "+str(j)
            print(secuencia)
            
if __name__ == "__main__":
    main()
