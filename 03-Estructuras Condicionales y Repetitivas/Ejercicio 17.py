"""
-----------------------------------------------------
Ejercicio 17: Calcular producto usando la suma
-----------------------------------------------------
Enunciado:  
Elabore un algoritmo que calcule el producto de dos enteros A y B empleando sólo la operación suma. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_17 ES 
    AMBIENTE 
        a,b,c,total: Entero
    PROCESO
        Escribir("Este algoritmo calcula el producto  de dos enteros A y B")
        Escribir("Ingrese los números A y B")
        Leer(a,b)
        total:=0
        Para c:=1 hasta b hacer
            total:=total+a
        Fin_Para
        Escribir("El total del producto es: ",total)
FIN_ACCION

"""

def main():
    print("Este algoritmo calcula el producto  de dos enteros A y B")
    a,b=map(int,input("Ingrese los números A y B: ").split())
    total=0
    for c in range(1,b+1):
        total+=a
    print("El total del producto es: ",total)
            
if __name__ == "__main__":
    main()
