"""
-----------------------------------------------------
Ejercicio 1.14: 
-----------------------------------------------------
Enunciado:  
Se dispone de una secuencia de caracteres y se desea saber la cantidad de caracteres (incluidos los espacios) 
que existen entre una coma y la siguiente.  Se debe considerar que puede haber más de un par de comas, y que las 
subsecuencias inicial y final deben descartarse por no cumplir la condición enunciada.  Supóngase que las comas son 
siempre contiguas al último caracter de la palabra. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.14 ES 
    AMBIENTE 
        sec: Secuencia de Caracteres
        s: Caracter
        coma_inicial: Entero
        total_caracter: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(sec);Avanzar(sec,s)
        
        primer_tramo:=VERDADERO
        Mientras NFDS(sec) hacer
            SI primer_tramo entonces
                primer_tramo:=FALSO
            SINO
                Escribir("Hay ",caracter_tramo," caracteres entre las comas")
            caracter_tramo:=0
            Mientras s<>',' hacer
                caracter_tramo:= caracter_tramo + 1
                Avanzar(sec,s)
            Fin_Mientras
            Avanzar(sec,s)
        Fin_Mientras
FIN_ACCION

"""
