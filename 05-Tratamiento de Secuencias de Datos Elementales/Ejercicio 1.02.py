"""
-----------------------------------------------------
Ejercicio 1.02: Conteo de Consonantes
-----------------------------------------------------
Enunciado:  
Dada una secuencia de letras del alfabeto que finaliza con la letra "Z", contar cuantas consonantes hay en la 
secuencia.  

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.02 ES 
       AMBIENTE 
        s: Secuencia de Caracter
        v: Caracter
        vocales:('A','E','I','O','U')
        cont: Entero
    PROCESO
        Escribir("Este algoritmo cuenta cuantas letras consonantes hay en una secuencia.")
        Arrancar(s)
        Avanzar(s,v)
        cont:=0
        Mientras NFDS(s) hacer
            SI v NoEN(vocales) entonces
                cont:=cont+1
            Fin_Si
            Avanzar(s,v)
        Fin_Mientras
        Cerrar(s)
        Escribir("Hay ",cont," letras consonantes en la secuencia")
FIN_ACCION

"""
#A fines practicos en python las secuencias las consideraremos Strings
#Y usaremos bucles para recorrer las secuencias
def main():
    vocales={"A","E","I","O","U"}
    salida='Z'
    print("Este algoritmo cuenta cuantas letras consonantes hay en una secuencia.")        
    sec=input("Ingrese una secuencia: ")  
    cont=0
    pos=0
    while sec[pos]!=salida: 
        if sec[pos] not in vocales:
            cont+=1
        pos+=1
    print("Hay ",cont," letras consonantes en la secuencia")
         
if __name__ == "__main__":
    main()
