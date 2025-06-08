"""
-----------------------------------------------------
Ejercicio 1.15: 
-----------------------------------------------------
Enunciado:  
Se desea saber la cantidad promedio de palabras que contienen las oraciones de una secuencia de caracteres.  
Supóngase que los puntos son siempre contiguos al último caracter de la palabra. La secuencia finaliza con una 
marca.

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.15 ES 
    AMBIENTE 
        oraciones: Secuencias de Caracter
        o: Caracter
        cant_palabras,cant_oraciones:=Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(oraciones);Avanzar(oraciones,o)
        cant_oraciones
        Mientras NFDS(oraciones) hacer
            Mientras o<>'.' hacer
                Mientras o=' ' hacer
                    Avanzar(oraciones,o)
                Fin_Mientras
                Mientras o<>' ' y o<>'.' hacer
                    Avanzar(oraciones,o)
                Fin_Mientras
                cant_palabras:= cant_palabras + 1
            Fin_Mientras
            Avanzar(oraciones,o)
            cant_oraciones:=cant_oraciones + 1
        Fin_Mientras
        Escribir("La cantidad promedio de palabras que contienen las oraciones es: ", cant_oraciones/cant_palabras)
FIN_ACCION

"""

