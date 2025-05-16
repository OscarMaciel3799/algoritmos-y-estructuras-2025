"""
-----------------------------------------------------
Ejercicio 1.1.5.4: Calcular superficie de un trapecio
-----------------------------------------------------
Enunciado:
Se desea calcular la superficie de un trapecio, para la cual se ingresa la longitud de ambas
bases y la altura. 

En base a la fórmula:
S = (Bmay +Bmen)× h / 2
Finalizando el proceso, emitir dicha superficie y los valores ingresados.


RESOLUCION EN PSEUDOCODIGO

ACCION calcular_superficie ES 
    AMBIENTE 
        base_menor,base_mayor,altura,superficie: Real
    PROCESO
        Escribir("Este algoritmo calcula la superficie de un trapecio")
        Escribir("Ingrese la base menor y la base mayor del trapecio")
        Leer(base_menor,base_mayor)
        Escribir("Ingrese la altura del trapecio")
        Leer(Altura)
        superficie:=(base_menor+base_mayor)*altura/2
        Escribir("La superficie del trapecio es: ",superficie)
FIN_ACCION

"""

def main():
    print("Este programa calcula la superficie de un trapecio")
    base_menor,base_mayor=map(float,input("Ingrese la base menor y la base mayor del trapecio separados por un espacio: ").split())
    altura=float(input("Ingrese la altura del trapecio: "))
    superficie=(base_menor+base_mayor)*altura/2
    print("La superficie del trapecio es: ",superficie)

if __name__ == "__main__":
    main()