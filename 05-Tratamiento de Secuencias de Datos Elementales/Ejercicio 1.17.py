"""
-----------------------------------------------------
Ejercicio 1.17: 
-----------------------------------------------------
Enunciado:  
Se desea calcular el costo de un telegrama, que se determina en función del número de palabras (que vale V1 
cada una),  salvo que el promedio de letras por palabra supere las cinco letras, caso en que cada palabra vale V2. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.17 ES 
    AMBIENTE 
        telegrama: Secuencia de Caracter
        t: Caracter
        cant_letras,cant_palabras,V1, V2: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(telegrama);Avanzar(telegrama,t)
        Escribir("Ingresar los posibles valores de las palabras V1 y V2")
        Leer(V1,V2)
        cant_palabras:=0
        cant_letras:=0
        Mientras NFDS(telegrama) hacer
            Mientras t = " " hacer
                Avanzar(telegrama,t)
            Fin_Mientras
            Mientras t<> " " y NFDS(telegrama) hacer
                cant_letras:=cant_letras + 1
                Avanzar(telegrama,t)
            Fin_Mientras
            cant_palabras:=cant_palabras + 1
        Fin_Mientras
        SI cant_letras/cant_palabras > 5 entonces
            Escribir("El costo del telegrama es: ",(cant_palabras*V2))
        SINO
            Escribir("El costo del telegrama es: ",(cant_palabras*V1))
        FIN_SI
FIN_ACCION

"""

def main():
    pass
            
if __name__ == "__main__":
    main()
