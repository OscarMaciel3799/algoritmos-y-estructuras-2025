"""
-----------------------------------------------------
Ejercicio 1.1.5.7: Calcular la media geométrica
-----------------------------------------------------
Enunciado:
Escriba un algoritmo que halle la media geométrica de tres valores X,Y ,Z . Este debe emitir
los tres valores por separado y luego el valor medio. La media geométrica es igual a
(X * Y * Z)/3



RESOLUCION EN PSEUDOCODIGO

ACCION calcular_media ES 
    AMBIENTE 
        x,y,z,media: Real
    PROCESO
        Escribir("Este algoritmo calcula la media geométrica entre 3 valores")
        Escribir("Ingrese los 3 valores")
        Leer(x,y,z)
        media:=(x * y * z) /3
        Escribir("La media geométrica es: ".media)
FIN_ACCION

"""
def main():
    print("Este programa calcula la media geométrica entre tres valores")
    x,y,z=map(float,input("Ingrese los tres valores separados por un espacio: ").split())
    media=(x*y*z)/3
    print("El valor de la media geométrica es: ",media)

if __name__ == "__main__":
    main()