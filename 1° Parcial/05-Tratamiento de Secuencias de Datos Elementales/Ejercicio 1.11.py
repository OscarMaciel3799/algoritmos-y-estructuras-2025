"""
-----------------------------------------------------
Ejercicio 1.11: 
-----------------------------------------------------
Enunciado:  
Dada una secuencia de caracteres, determinar la cantidad de palabras de 4 caracteres (letras) 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.11 ES 
    AMBIENTE 
        oracion: Secuencia de Caracteres
        v: Caracter
        cont,cantidad: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(oracion)
        Avanzar(oracion,v)
        cantidad:=0
        Mientras NFDS(oracion) hacer
            Mientras v=' '  hacer
                avanzar(oracion,v)
            Fin_Mientras
            cont:=0
            Mientras v<>' ' y NFDS(oracion)  hacer
                cont:=cont+1
                avanzar(oracion,v)
            Fin_Mientras
            SI cont=4 entonces
                cantidad:=cantidad+1
            FIN_SI
        Fin_Mientras
        Escribir("La cantidad de palabras de 4 caracteres son: ",cantidad)
FIN_ACCION

"""

#A fines practicos en python las secuencias de Enteros las consideraremos Listas
#A fines practicos en python las secuencias de Caracteres las consideraremos Strings
#Y usaremos bucles para recorrer las secuencias
def main():
    print("Este algoritmo ....")
    sec=str(input("Ingrese la secuencia: "))
    # Luna vino para jugar con su bola azul bajo el cielo.
    cantidad=0
    pos=0
    v=sec[pos]
    while pos<len(sec)-1:
        v=str(sec[pos])
        while  v==' ':
            pos+=1
            v=str(sec[pos])
        cont=0
        while v!=' ' and  pos<len(sec)-1:
            cont+=1
            pos+=1
            v=str(sec[pos])
        if cont==4:
            cantidad+=1
    print("La cantidad de palabras de 4 caracter son: ",cantidad)
            
if __name__ == "__main__":
    main()
