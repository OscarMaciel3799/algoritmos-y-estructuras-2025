"""
-----------------------------------------------------
Ejercicio 1.03: Secuencia de salida
-----------------------------------------------------
Enunciado:  
Se dispone de una secuencia de caracteres y se desea obtener una secuencia de salida que resulte de copiar la 
secuencia de entrada, descartando el caracter "$". 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.03 ES 
    AMBIENTE 
        s,sal: Secuencia de Caracter
        v: Caracter
    PROCESO
        Escribir("Este algoritmo devuelve una secuencia descartando el '$' de la secuencia de entrada.")
        Arrancar(s)
        Avanzar(s,v)
        Crear(sal)
        Mientras NFDS(s) hacer
            SI v <> '$' entonces
                Escribir(sal,v)
            Fin_Si
            Avanzar(s,v)
        Fin_Mientras
        Cerrar(s)
        Cerrar(sal)        
FIN_ACCION

"""
#A fines practicos en python las secuencias las consideraremos Strings
#Y usaremos bucles para recorrer las secuencias
def main():
    print("Este algoritmo devuelve una secuencia descartando el '$' de la secuencia de entrada.")
    sec=str(input("Este algoritmo devuelve una secuencia descartando el '$' de la secuencia de entrada: "))
    pos=0
    salida=None
    while pos<len(sec): 
        if sec[pos]!='$':
            if salida is None:
                salida=sec[pos]
            else:
                salida+=sec[pos]
        pos+=1
    print(salida)
if __name__ == "__main__":
    main()
