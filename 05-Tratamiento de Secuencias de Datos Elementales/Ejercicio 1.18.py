"""
-----------------------------------------------------
Ejercicio 1.18: 
-----------------------------------------------------
Enunciado:  
Escribir un algoritmo que produzca una secuencia de salida que contenga una oración formada por por las 
palabras en posición par de cada oración de una secuencia texto de entrada, que además comienzan con la letra “M”.

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.18 ES 
    AMBIENTE 
        oraciones,salida: Secuencia de Caracter
        o: Caracter
        posicion: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(oraciones);Avanzar(oraciones,o)
        Crear(salida)
        
        Mientras NFDS(oraciones) hacer
            posicion:=1
            Mientras o<>'.' hacer
                Mientras o =" " hacer
                    Avanzar(oraciones,o)
                Fin_Mientras
                SI posicion MOD 2 = 0 y o = 'M' entonces
                    Mientras o <> " " y o <> "."hacer
                        Escribir(salida,o)
                        Avanzar(oraciones,o)
                    Fin_Mientras
                SINO
                    Mientras o <> " " y o <> ". hacer
                        Avanzar(oraciones,o)
                    Fin_Mientras
                Fin_SI
            Fin_Mientras
            Avanzar(oraciones,o)
        Fin_Mientras
        Cerrar(salida)
FIN_ACCION

"""

def main():
    pass
            
if __name__ == "__main__":
    main()
