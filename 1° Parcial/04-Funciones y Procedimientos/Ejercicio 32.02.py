"""
-----------------------------------------------------
Ejercicio 32.02: Suma de Digitos
-----------------------------------------------------
Enunciado:  
Diseñe una función que devuelva la suma de los dígitos del número natural suministrado como parámetro.

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_2 ES 
    AMBIENTE 
        num: Entero
        Funcion suma_digitos(n: Entero):Entero Es
            Ambiente
                suma,digito: Entero
            Proceso
                suma:=0
                Mientras n > 9 hacer
                    digito:= n MOD 10
                    n:= n DIV 10
                    suma:=suma+digito
                Fin Mientras
                suma:=suma+n
                suma_digitos:=suma
        Fin_Funcion
    PROCESO
                
        Escribir("Este algoritmo suma los dígitos del número suministrado")
        Escribir("Ingrese un número")
        Leer(num)
        Escribir("La suma de los digitos del número ",num," es: ",suma_digitos(num))
        
FIN_ACCION

"""

def suma_digitos(n):
    suma=0
    while n > 9 :
        digito=n%10
        n=n//10
        suma+=digito
    
    suma+=n
    return suma
            
if __name__ == "__main__":
    print("Este algoritmo suma los dígitos del número suministrado")
    num=int(input("Ingrese un número: "))
    print("La suma de los digitos del número ",num," es: ",suma_digitos(num))
