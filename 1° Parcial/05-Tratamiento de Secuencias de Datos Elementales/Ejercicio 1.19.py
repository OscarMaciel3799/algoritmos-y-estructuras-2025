"""
-----------------------------------------------------
Ejercicio 1.19: 
-----------------------------------------------------
Enunciado:  
Dada una secuencia de caracteres, generar otra secuencia con todas las palabras de tres caracteres. Informar 
el porcentaje de las mismas, sobre el total de palabras de la secuencia de entrada. Considerar que puede haber más 
de un blanco entre palabras. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.19 ES 
    AMBIENTE 
        palabras, Salida: Secuencia de Caracter
        p: Caracter
        c1,c2,c3: Caracter
        palabras_total,palabras_3c: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(palabras);Avanzar(palabras,p)
        Crear(salida)
        palabras_total:=0
        palabras_3c:=0
        Mientras NFDS(palabras) hacer
            Mientras p=" " hacer
                Avanzar(palabras,p)
            Fin_Mientras
            c1:=p
            Avanzar(palabras,p)
            c2:=p
            Avanzar(palabras,p)
            c3:=p
            Avanzar(palabras,p)
            Si p=" " O NFDS(palabras) entonces
                palabras_3c:=palabras_3c + 1
                Escribir(salida,c1)
                Escribir(salida,c2)
                Escribir(salida,c3)
            SINO
                Mientras p <> " " Y NFDS(palabras) hacer
                    Avanzar(palabras,p)
                Fin_Mientras 
            FIN_SI
            palabras_total:= palabras_total + 1
        FIN_Mientras
        Escribir("El porcentaje de palabras de tres caracteres es:", (palabras_3c*100/palabras_total)," %")
FIN_ACCION

"""

def main():
    pass
            
if __name__ == "__main__":
    main()
