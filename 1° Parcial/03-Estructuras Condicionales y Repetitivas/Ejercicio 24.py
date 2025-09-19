"""
-----------------------------------------------------
Ejercicio 24: abc=a**3+b**3+c**3
-----------------------------------------------------
Enunciado:  
Construya un algoritmo capaz de encontrar todas las cifras de tres dígitos que cumplan con la condición de que la 
suma de los cubos de sus dígitos sea igual al número que la cifra representa. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_24 ES 
    AMBIENTE 
        numero,a,b,c: Entero
    PROCESO
        Escribir("Este algoritmo encuentra todas las cifras de tres dígitos que cumplan con la condición de que la 
suma de los cubos de sus dígitos sea igual al número que la cifra representa.")
        Para numero:=100 Hasta 999 Hacer
            a:=numero DIV 100
            b:=(numero MOD 100) DIV 10
            c:=numero MOD 10
            Si (a**3 + b**3 + c**3) = numero Entonces
                Escribir(numero)
            FinSi
        FinPara
FIN_ACCION

"""

def main():
    for numero in range(100, 1000):
        a = numero // 100
        b = (numero % 100) // 10
        c = numero % 10
        if (a**3 + b**3 + c**3) == numero:
            print(numero)
            
if __name__ == "__main__":
    main()
