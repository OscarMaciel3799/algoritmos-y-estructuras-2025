"""
-----------------------------------------------------
Ejercicio 1.1.5.1: Calcular el precio futuro con inflación
-----------------------------------------------------
Enunciado:
Escribir un programa que permita calcular el precio de un artículo para un año dado,
considerando que la inflación es del 4 por 100 anual.

La fórmula del precio es: 
P = C * (1 + R) ^ (N - A)
C - Precio actual.
N - Año futuro.
R - Tasa de Inflación.
A - Año actual.


RESOLUCION EN PSEUDOCODIGO

ACCION precio_futuro ES 
    AMBIENTE 
        precio_actual, precio_final : Real
        inflacion = 0,04
        año_actual, año_final : Entero
    PROCESO
        Escribir("Este algoritmo calcula el precio futuro de un producto")
        Escribir("Ingrese el precio del producto")
        Leer(precio_actual)
        Escribir("Ingrese el año actual, y el año futuro")
        Leer(año_actual,año_futuro)
        precio_final:=precio_actual*(1+inflacion)**(año_final - año_actual)
        Escribir("El precio final del producto sera: ",precio_final)
FIN_ACCION

"""

def main():
    print("Este programa calcula el precio futuro de un producto")
    precio_actual=float(input("Ingrese el precio del producto: "))
    año_actual=int(input("Ingrese el año actual: "))
    año_futuro=int(input("Ingrese el año futuro: "))
    inflacion=0.04
    precio_futuro=precio_actual*(1+inflacion)**(año_futuro-año_actual)
    print("El precio futuro del producto será: ",precio_futuro)
    
if __name__ == "__main__":
    main()
    