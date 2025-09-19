"""
-----------------------------------------------------
Ejercicio 32.08: Intercambiar variables
-----------------------------------------------------
Enunciado:  
Crear un procedimiento que intercambie los valores de dos variables numéricas.

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_8 ES 
    AMBIENTE 
        v1,v2: Entero
        Procedimiento intercambiar(var1,var2: Entero)
                v2:=var1
                v1:=var2
                Escribir("El valor de la primer variable ahora es: ",v1)
                Escribir("El valor de la segunda variable ahora es: ",v2)
        Fin_Procedimiento
    PROCESO
        Escribir("Este algoritmo intercambia los valores de dos variables numéricas.")
        Escribir("Ingrese los valores de las 2 variables")
        Leer(v1,v2)
        intercambiar(v1,v2)
        
FIN_ACCION

"""

def intercambiar(var1,var2):
    print(var1,var2)
    v2=var1
    v1=var2
    print("El valor de la primer variable ahora es: ",v1)
    print("El valor de la segunda variable ahora es: ",v2)
            
if __name__ == "__main__":
    print("Este algoritmo intercambia los valores de dos variables numéricas.")
    v1,v2=map(int,input("Ingrese los valores de las 2 variables: ").split())
    intercambiar(v1,v2)
