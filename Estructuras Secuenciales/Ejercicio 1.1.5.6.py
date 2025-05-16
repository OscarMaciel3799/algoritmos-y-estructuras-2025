"""
-------------------------------------------------------------
Ejercicio 1.1.5.6: Calcular el producto de números complejos
-------------------------------------------------------------
Enunciado:
Realizar un programa que lea dos número complejos,  (a, b) y (c,d), calcule su producto :

(a, b) * (c,d) = (ac - db,ad +bc)



RESOLUCION EN PSEUDOCODIGO

ACCION calcular_producto ES 
    AMBIENTE 
        numero_1x,numero_1y,numero_2x,numero_2y,numero_3x,numero_3y: Real
    PROCESO
        Escribir("Este algoritmo calcula el producto de dos números complejos")
        Escribir("Ingrese los valores del primer número complejo")
        Leer(numero_1x,numero_1y)
        Escribir("Ingrese los valores del segundo número complejo")
        Leer(numero_2x,numero_2y)
        numero_3x:=numero_1x*numero_2x - numero_1y*numero_2y
        numero_3y:=numero_1x*numero_2y + numero_1y*numero_2x
        Escribir("Los valores del número resultante son : (",numero_3x," , ",numero_3y,")")
FIN_ACCION

"""

def main():
    print("Este programa calcula el producto de dos números complejos")
    numero1_x,numero1_y=map(float,input("Ingrese los valores del primer número complejos separados por un espacio: ").split())
    numero2_x,numero2_y=map(float,input("Ingrese los valores del segundo número complejos separados por un espacio: ").split())
    numero3_x=numero1_x*numero2_x-numero1_y*numero2_y
    numero3_y=numero1_x*numero2_y+numero1_y*numero2_x
    print("Los valores del número resultante son: (",numero3_x," , ",numero3_y,")")

if __name__ == "__main__":
    main()