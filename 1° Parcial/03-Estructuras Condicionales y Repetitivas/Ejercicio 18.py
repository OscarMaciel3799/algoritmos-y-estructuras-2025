"""
-----------------------------------------------------
Ejercicio 18: Calcular division usando suma y resta
-----------------------------------------------------
Enunciado:  
Elabore un algoritmo que calcule el cociente de dos enteros F y G y el resto de la operación, empleando sólo las 
operaciones suma y diferencia. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_18 ES 
    AMBIENTE 
        f,g,cociente,resto: Entero
    PROCESO
        Escribir("Este algoritmo calcula el cociente de dos enteros F y G y el resto de la operación")
        Escribir("Ingrese los números F y G")
        Leer(f,g)
        cociente:=0
        Mientras f>=g hacer
            cociente:=cociente+1
            f:=f-g
        Fin_Mientras
        resto:=f
        Escribir("El cociente entre los números ",(g*cociente+resto)," y ",g," es: ",cociente," y el resto es: ",resto)
FIN_ACCION

"""

def main():
    print("Este programa calcula el cociente de dos enteros F y G y el resto de la operación")
    f,g=map(int,input("Ingrese los números F y G: ").split())
    cociente=0
    while f-g>=0:
        cociente+=1
        f-=g
    resto=f
    print("El cociente entre los números ",(g*cociente+resto)," y ",g," es: ",cociente," y el resto es: ",resto)
            
if __name__ == "__main__":
    main()
