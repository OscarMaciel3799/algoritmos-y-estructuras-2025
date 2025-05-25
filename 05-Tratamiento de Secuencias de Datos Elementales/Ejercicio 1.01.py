"""
-----------------------------------------------------
Ejercicio 1.01: Contar cantidad de A
-----------------------------------------------------
Enunciado:  
Dada una secuencia de letras del alfabeto que finaliza con una marca '*', contar cuantas letras "A" hay en la 
secuencia.

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.01 ES 
    AMBIENTE 
        s: Secuencia de Caracter
        v: Caracter
        cont: Entero
    PROCESO
        Escribir("Este algoritmo cuenta cuantas letras A hay en una secuencia.")
        Arrancar(s)
        Avanzar(s,v)
        cont:=0
        Mientras NFDS(s) hacer
            SI v:='A' entonces
                cont:=cont+1
            Fin_Si
            Avanzar(s)
        Fin_Mientras
        Cerrar(s)
        Escribir("Hay ",cont," letras A en la secuencia")
FIN_ACCION

"""

def main():
    #sec = ASDFSDFASDA*
    print("Este algoritmo cuenta cuantas letras A hay en una secuencia.")
    sec=input("Ingrese una secuencia: ")
    cont=0
    pos=0
    while sec[pos]!='*': 
        if sec[pos]=='A':
            cont+=1
        pos+=1
    print("Hay ",cont," letras A en la secuencia")

#A fines practicos en python las secuencias las consideraremos Strings
#Y usaremos bucles para recorrer las secuencias            
if __name__ == "__main__":
    main()
