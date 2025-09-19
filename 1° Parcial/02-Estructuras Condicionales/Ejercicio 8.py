"""
-----------------------------------------------------
Ejercicio 8: Imprimir mensaje
-----------------------------------------------------
Enunciado:
Escriba un algoritmo que acepte dos números, calcule la suma e imprima el mensaje de acuerdo al resultado 
obtenido.                
suma <= 50 
suma  > 50 y <= 100 
suma  > 100 y <= 200 
suma  > 200 


RESOLUCION EN PSEUDOCODIGO

ACCION ordenar ES 
    AMBIENTE 
        num1,num2,suma: Real
    PROCESO
        Escribir("Este algoritmo calcula una suma de dos números e imprime un mensaje")
        Escribir("Ingrese los dos números")
        Leer(num1,num2)
        suma:=num1+num2
        Según suma hacer
            <= 50 : Escribir("La suma es menor o igual a 50")
            <= 100 : Escribir("La suma es mayor a 50 y menor o igual a 100")
            <= 200 : Escribir("La suma es mayor a 100 y menor o igual a 200")
            Otro : Escribir("La suma es mayor  a 200")
        Fin_Segun
FIN_ACCION

"""

def main():
    print("Este algoritmo calcula una suma de dos números e imprime un mensaje")
    num1,num2=map(float,input("Ingrese los dos números separados por un espacio: ").split())
    suma=num1+num2
    # python no tiene una estructura similar al según como si lo tienen otros lenguajes por lo que usamos un
    # condicional anidado
    if suma<=50:
        print("La suma es menor o igual a 50")
    elif suma <=100:
        print("La suma es mayor a 50 y menor o igual a 100")
    elif suma<=200:
        print("La suma es mayor a 100 y menor o igual a 200")
    else:
        print("La suma es mayor a 200")
    
if __name__ == "__main__":
    main()