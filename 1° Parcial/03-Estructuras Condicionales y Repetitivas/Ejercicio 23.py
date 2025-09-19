"""
-----------------------------------------------------
Ejercicio 23: Calcular los primeros 50 de Fibonacci
-----------------------------------------------------
Enunciado:  
Elabore un algoritmo para calcular los primeros 50 números de FIBONACCI, sabiendo que dichos números 
cumplen con lo siguiente: 
A0=0, A1=1, A2=A0+A1, ..... An=A(n-1)+A(n-2). 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_23 ES 
    AMBIENTE 
        a,b,c,i: Entero
    PROCESO
        Escribir("Este algoritmo calcula los primeros 50 números de FIBONACCI")
        a:=0
        b:=1
        Escribir("Fibonacci[0] = ", a)
        Escribir("Fibonacci[1] = ", b)
        Para i:=2 Hasta 49 Hacer
            c:= a + b
            Escribir("Fibonacci[", i, "] = ", c)
            a:=b
            b:=c
        FinPara
FIN_ACCION

"""

def main():
    a = 0
    b = 1
    print(f"Fibonacci[0] = {a}")
    print(f"Fibonacci[1] = {b}")
    for i in range(2, 50):
        c = a + b
        print(f"Fibonacci[{i}] = {c}")
        a = b
        b = c
            
if __name__ == "__main__":
    main()
