"""
-----------------------------------------------------
Ejercicio 1.13: 
-----------------------------------------------------
Enunciado:  
A partir del ejercicio anterior, determinar el porcentaje que representan las palabras que comienzan con “ALG” 
sobre todas las palabras de la secuencia 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.13 ES 
    AMBIENTE 
        oracion,sal: Secuencia de Caracteres
        v: Caracter
        existe_A,existe_L: Booleano
        palabras_alg,palabras_total: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(oracion)
        Avanzar(oracion,v)
        palabras_total:=0
        palabras_alg:=0
        Mientras NFDS(oracion) hacer
            Mientras v=' '  hacer
                avanzar(oracion,v)
            Fin_Mientras
            palabras_total:=palabras_total + 1
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
                palabras_alg:=palabras_alg + 1                
            FIN_SI   
            Mientras v<>' ' y NFDS(oracion)  hacer
                avanzar(oracion,v)
            Fin_Mientras 
        Fin_Mientras
        Escribir("El porcentaje de palabras que empiezan por alg es: ",(palabras_alg*100/palabras_total)," %")
FIN_ACCION

"""
#A fines practicos en python las secuencias de Caracteres las consideraremos Strings
#Y usaremos bucles para recorrer las secuencias
def main():
    print("Este algoritmo ....")
    oracion="Algunas personas usan algoritmos para resolver ciertos problemas de forma más eficiente"
    pos=0
    palabras_total=0
    palabras_alg=0
    while pos < len(oracion)-1:
        v=oracion[pos]
        while v==' ':
            pos+=1
            v=oracion[pos]
            
        palabras_total+=1
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
        if existe_A and existe_L and v.upper()=='G':
                palabras_alg += 1                
        while v!=' ' and pos < len(oracion)-1:
            pos+=1
            v=oracion[pos]
        
    print("El porcentaje de palabras que empiezan por alg es: ",(palabras_alg*100/palabras_total)," %")
            
if __name__ == "__main__":
    main()
