"""
-----------------------------------------------------
Ejercicio 1.04: Cantidad de socios
-----------------------------------------------------
Enunciado:  
Se dispone de una secuencia de números de socios, y se desea saber la cantidad de socios que están 
registrados. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.04 ES 
    AMBIENTE 
        s: Secuencia de enteros
        v,cont: Entero
        
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(s)
        Avanzar(s,v)
        cont:=0
        Mientras NFDS(s) hacer
            cont:=cont+1
            Avanzar(s,v)
        Fin_Mientras
        Escribir("Hay ",cont," socios registrados")
FIN_ACCION

"""

def main():
    print("Este algoritmo cuenta la cantidad de socios registrados en un secuencia")
    sec=input("Ingrese una secuencia de entrada separadas por comas: ").split(',')
    pos=0
    cont=0
    while pos<len(sec): 
        cont+=1
        pos+=1
    print("Hay ",cont," socios registrados")
            
if __name__ == "__main__":
    main()
