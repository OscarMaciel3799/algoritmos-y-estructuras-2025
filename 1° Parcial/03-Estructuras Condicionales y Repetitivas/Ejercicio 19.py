"""
-----------------------------------------------------
Ejercicio 19: El número es primo?
-----------------------------------------------------
Enunciado:  
Escriba un algoritmo que determine si un número es primo. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_19 ES 
    AMBIENTE 
        num,i: Entero
        salida,esprimo: boolean
    PROCESO
        Escribir("Este algoritmo determina si un número es primo.")
        Escribir("Ingrese un número")
        Leer(num)
        i:=2
        esprimo:=verdadero
        salida:=falso
        Mientras i<num y salida<> verdadero hacer
            Si num mod i =0 entonces
                salida:=verdadero
                esprimo:=falso
            Sino
                i:=i+1
            Fin_si
        Fin_Mientras
        SI esprimo entonces
            Escribir("El número ",num," es primo")
        SINO
            Escribir("El número ",num," NO es primo")
        Fin_SI
FIN_ACCION

"""

def main():
    print("Este programa determina si un número es primo.")
    num=int(input("Ingrese un número: "))
    esprimo=True
    cont=2
    salida=False
    while cont<num and salida is False:
            if num % cont ==0:
                salida=True
                esprimo=False
            else:
                cont+=1
            
    if esprimo :
        print("El número ",num," es primo")
    else:
        print("El número ",num," NO es primo")

            
if __name__ == "__main__":
    main()
