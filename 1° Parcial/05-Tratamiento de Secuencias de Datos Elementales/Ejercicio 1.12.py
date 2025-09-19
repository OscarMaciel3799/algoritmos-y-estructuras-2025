"""
-----------------------------------------------------
Ejercicio 1.12: 
-----------------------------------------------------
Enunciado:  
Se dispone de una secuencia de caracteres.  Se desea listar las palabras que comiencen con "ALG". 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.12 ES 
    AMBIENTE 
        oracion,sal: Secuencia de Caracteres
        v: Caracter
        existe_A,existe_L: Booleano
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(oracion)
        Avanzar(oracion,v)
        Mientras NFDS(oracion) hacer
            Mientras v=' '  hacer
                avanzar(oracion,v)
            Fin_Mientras
            avanzar(oracion,v)
            existe_A:=FALSO
            existe_L:=FALSO
            SI v='A' entonces
                existe_A:=VERDADERO
            FIN_SI
            avanzar(oracion,v)
            SI v='L' entonces
                existe_L:=VERDADERO
            FIN_SI
            avanzar(oracion,v)
            SI existe_A y existe_L y v='G' entonces
                Escribir(sal,'a')
                Escribir(sal,'l')
                Escribir(sal,v)
                
                Mientras v<>' ' y NFDS(oracion)  hacer
                    Escribir(sal,v)
                    avanzar(oracion,v)
                Fin_Mientras
            SINO
                Mientras v<>' ' y NFDS(oracion)  hacer
                    avanzar(oracion,v)
                Fin_Mientras
            FIN_SI    
        Fin_Mientras
        Cerrar(sal)
FIN_ACCION

"""

#A fines practicos en python las secuencias de Caracteres las consideraremos Strings
#Y usaremos bucles para recorrer las secuencias
def main():
    print("Este algoritmo ....")
    oracion="Algunas personas usan algoritmos para resolver ciertos problemas de forma más eficiente"
    sal=None
    pos=0
    v=oracion[pos]
    while pos<len(oracion)-1:
        v=str(oracion[pos])
        while  v==' ':
            pos+=1
            v=str(oracion[pos])
        
        existe_A=False
        existe_L=False
        if v.upper()=="A":
            existe_A=True
        pos+=1
        v=str(oracion[pos])
        if v.upper()=='L':
            existe_L=True
        pos+=1
        v=str(oracion[pos])
        if v.upper()=='G' and existe_A and existe_L:
            if sal==None:
                sal="a"
            else:
                sal+="a"
            sal+="l"
            while v!=' ' and pos<len(oracion):
                sal+=v
                pos+=1        
                v=str(oracion[pos])
        else:
            while v!=' ' and pos<len(oracion)-1:
                pos+=1
                v=str(oracion[pos])
        
    print("La Secuencia resultante es: ",sal)
            
if __name__ == "__main__":
    main()