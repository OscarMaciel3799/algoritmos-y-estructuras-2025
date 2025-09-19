"""
-----------------------------------------------------
Ejercicio 1.1.5.2: Calcular el discriminante
-----------------------------------------------------
Enunciado:
Las raíces de una ecuación de segundo grado ax**2 + bx + c =0 son reales si y sólo si el discriminante dado por  
(b2 − 4ac) no es negativo. 
Se desea leer el valor de los coeficientes a,b ,c e imprimir el resultado del discriminante.
Realizar prueba de escritorio.



RESOLUCION EN PSEUDOCODIGO

ACCION discriminante ES 
    AMBIENTE 
        a,b,c,discriminante: Real
    PROCESO
        Escribir("Este algoritmo calcula el discriminante de una ecuación de segundo grado")
        Escribir("Ingrese los coeficientes a, b y c")
        Leer(a,b,c)
        discriminante:= (b**2)-(4*a*c)
        Escribir("El valor del discriminante es: ",discriminante)
FIN_ACCION

"""

def main():
    print("Este programa calcula el discriminante de una ecuación de segundo grado")
    a, b, c = map(float, input("Ingrese los coeficientes a, b y c separados por espacios: ").split())
    discriminante=(b**2)-4*a*c
    print("El valor del discriminante es: ",discriminante)

if __name__ == "__main__":
    main()