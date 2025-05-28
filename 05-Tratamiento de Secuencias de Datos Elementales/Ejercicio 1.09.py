"""
-----------------------------------------------------
Ejercicio 1.09: 
-----------------------------------------------------
Enunciado:  
Se dispone de una secuencia de caracteres.  Se desea determinar la cantidad de palabras que comienzan con 
la letra “I”. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.09 ES 
    AMBIENTE 
        palabras: Secuencia de Caracteres
        v: Caracter
        cont: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(palabras)
        Avanzar(palabras,v)
        cont:=0
        Mientras NFDS(palabras) hacer
            Mientras v=' '  hacer
                avanzar(palabras,v)
            Fin_Mientras
            SI v='I' entonces
                cont:=cont+1
            Fin_SI
            Mientras v<>' ' y NFDS(palabra)  hacer
                avanzar(palabras,v)
            Fin_Mientras
        Fin_Mientras
        Escribir("La cantidad de palabras que empiezan con I son: ",cont)
FIN_ACCION

"""
#A fines practicos en python las secuencias de Enteros las consideraremos Listas
#A fines practicos en python las secuencias de Caracteres las consideraremos Strings
#Y usaremos bucles para recorrer las secuencias
def main():
    print("Este algoritmo ....")
    sec=str(input("Ingrese la secuencia: "))
    # Ignacio imaginó increíbles islas iluminadas por intensos rayos de luna.
    cont=0
    pos=0
    v=sec[pos]
    while pos<len(sec)-1:
        v=str(sec[pos])
        while  v==' ':
            pos+=1
            v=str(sec[pos])
        if v.lower()=='i':
                cont+=1
        while v!=' ' and  pos<len(sec)-1:
            pos+=1
            v=str(sec[pos])
    
    print("La cantidad de palabras que empiezan con I son: ",cont)
            
if __name__ == "__main__":
    main()
