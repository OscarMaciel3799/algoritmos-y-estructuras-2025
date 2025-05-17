"""
-----------------------------------------------------
Ejercicio 20: Números primos menores a N
-----------------------------------------------------
Enunciado:  
Escriba un algoritmo para imprimir los números primos menores a un valor dado n. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_20 ES 
    AMBIENTE 
        n,i,c: Entero
        esprimo,salida: Boolean
    PROCESO
        Escribir("Este algoritmo imprime los números primos menores a un valor dado n.")
        Escribir("Ingrese un número")
        Leer(n)
        c:=2
        para i:=2 hasta n-1 hacer
            esprimo:=verdadero
            salida:=falso
            Mientras c<i y salida<> verdadero hacer
                Si i mod c =0 entonces
                    salida:=verdadero
                    esprimo:=falso
                Sino
                    c:=c+1
                Fin_si
            Fin_Mientras
            SI esprimo entonces
                Escribir("El número ",i," es primo")
            Fin_SI
        Fin_Para
FIN_ACCION

"""

def main():
    print("Este programa imprime los números primos menores a un valor dado n.")
    n=int(input("Ingrese un número: "))
    for i in range(2,n):
        c=2
        esprimo=True
        salida=False
        while c<i and salida is False:
            if i%c ==0:
                salida=True
                esprimo=False
            else:
                c+=1
            
        if esprimo :
            print("El número ",i," es primo")
            
            
if __name__ == "__main__":
    main()
