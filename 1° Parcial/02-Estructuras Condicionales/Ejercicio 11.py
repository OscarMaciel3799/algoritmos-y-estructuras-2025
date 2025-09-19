"""
-----------------------------------------------------
Ejercicio 11: Es divisor? 
-----------------------------------------------------
Enunciado:
Dados dos números enteros A y B generar un algoritmo que permita determinar si A es divisor de B o 
B es divisor de A.   


RESOLUCION EN PSEUDOCODIGO

ACCION divisor ES 
    AMBIENTE 
        a,b: Enteros
        
    PROCESO
        Escribir("Este algoritmo evalua si dos números son divisores entre sí")
        Escribir("Ingrese los números A y B")
        Leer(a,b)
        SI a MOD b = 0 entonces
            Escribir ("El número ",b," es divisor del número ",a)
        SINO
            SI b MOD a = 0 entonces
                Escribir ("El número ",a," es divisor del número ",b)
            SINO
                Escribir("Los números no son divisibles entre sí")
            Fin_Si
        Fin_Si
FIN_ACCION

"""

def main():
    print("Este programa evalua si dos números son divisores entre sí")
    a,b=map(int,input("Ingrese los números A y B separados por un espacio: ").split())
    if a%b==0:
        print("El número ",b," es divisor del número ",a)
    elif b%a==0:
        print("El número ",a," es divisor del número ",b)
    else:
        print("Los números no son divisibles entre sí")

if __name__ == "__main__":
    main()