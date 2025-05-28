"""
-----------------------------------------------------
Ejercicio 1.10: 
-----------------------------------------------------
Enunciado:  
Se dispone de una secuencia de caracteres.  Se desea permita contar la cantidad de palabras que comienzan 
con una letra dada. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.10 ES 
    AMBIENTE 
        palabras: Secuencia de Caracteres
        letra: Caracter
        v: Caracter
        cont: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Escribir("Ingrese un caracter")
        Leer(letra)
        Arrancar(palabras)
        Avanzar(palabras,v)
        cont:=0
        Mientras NFDS(palabras) hacer
            Mientras v=' '  hacer
                avanzar(palabras,v)
            Fin_Mientras
            SI v=letra entonces
                cont:=cont+1
            Fin_SI
            Mientras v<>' ' y NFDS(palabra)  hacer
                avanzar(palabras,v)
            Fin_Mientras
        Fin_Mientras
        Escribir("La cantidad de palabras que empiezan con la letra ",letra," son: ",cont)
FIN_ACCION

"""

#A fines practicos en python las secuencias de Enteros las consideraremos Listas
#A fines practicos en python las secuencias de Caracteres las consideraremos Strings
#Y usaremos bucles para recorrer las secuencias
def main():
    print("Este algoritmo ....")
    sec=str(input("Ingrese la secuencia: "))
    # Ignacio imaginó increíbles islas iluminadas por intensos rayos de luna.
    letra=str(input("Ingrese un caracter: "))
    # p
    if len(letra)<1:
        print("El valor ingresado no es UN CARACTER")
    else:
        cont=0
        pos=0
        v=sec[pos]
        while pos<len(sec)-1:
            v=str(sec[pos])
            while  v==' ':
                pos+=1
                v=str(sec[pos])
            if v.lower()==letra.lower():
                    cont+=1
            while v!=' ' and  pos<len(sec)-1:
                pos+=1
                v=str(sec[pos])
        
        print("La cantidad de palabras que empiezan con la letra ",letra," son: ",cont)
            
if __name__ == "__main__":
    main()
