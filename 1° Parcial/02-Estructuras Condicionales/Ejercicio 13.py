"""
-----------------------------------------------------
Ejercicio 13: Conversion de monedas
-----------------------------------------------------
Enunciado:
Escriba un algoritmo que acepte un número entero mayor a 100 y menor a 1000 que representa una suma de 
dinero e indique cuántos billetes de cada denominación necesita, suponiendo que solo existen billetes de 100, 10 y 1 
peso.   


RESOLUCION EN PSEUDOCODIGO

ACCION billetes ES 
    AMBIENTE 
        num: Entero
        
    PROCESO
        Escribir("Este algoritmo calcula la cantidad de billetes de 100, 10 y 1 se necesita para llegar al número ingresado")
        Escribir("Ingrese un número entre 100 y 1000")
        Leer(num)
        Escribir("Se necesitan ",(num DIV 100)," billetes de 100")
        Escribir("Se necesitan ",((num DIV 10) MOD 10)," billetes de 10")
        Escribir("Se necesitan ",(num MOD 10)," billetes de 1")
FIN_ACCION

"""

def main():
    print("Este algoritmo calcula la cantidad de billetes de 100, 10 y 1 se necesita para llegar al número ingresado")
    num=int(input("Ingrese un número entre 100 y 1000: "))
    print("Se necesitan ",(int(num/100))," billetes de 100")
    print("Se necesitan ",(int((num/10)%10))," billetes de 10")
    print("Se necesitan ",(num%10)," billetes de 1")
    

if __name__ == "__main__":
    main()