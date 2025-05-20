"""
-----------------------------------------------------
Ejercicio 32.04: Claves
-----------------------------------------------------
Enunciado:  
Elaborar una función que reciba un número entero y retorne -1 si el número es negativo. 
Si el número es positivo debe devolver una clave calculada de la siguiente manera: Se suma cada dígito que 
compone el número y a esa suma se le calcula el módulo 7. 
Por ejemplo: para la cifra 513, la clave será 5+1+3 =9; 9 mod 7 =2. 
Utilice la función para diseñar un algoritmo que permita leer varios valores y determine, para cada uno, si el número 
leído fue negativo o, si fue positivo, que clave le corresponde. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_4 ES 
    AMBIENTE 
        num: Entero
        seguir:('S','N')
        Funcion clave (n:Entero):Entero es
            Ambiente
                digito,suma: Entero
            Proceso
                SI n>0 entonces
                    suma:=0
                    Mientras n > 9 hacer
                        digito:=n MOD 10
                        n:= n DIV10
                        suma:=suma + digito
                    Fin_Mientras
                    suma:=suma+n
                    clave:=suma
                Sino
                    clave:=-1
                Fin_SI
        Fin_Funcion
    PROCESO
        Escribir("Este algoritmo devuelve la clave de números")
        Escribir("Desea ingresar el primer número? S para Si, cualquier tecla para NO: ")
        Leer(seguir)
        Mientras seguir='S' hacer
            Escribir("Ingrese el número: ")
            Leer(num)
            Escribir("La clave del número ",num," es: ",clave(num))
            Escribir("Desea ingresar otro número? S para SI")
            Leer(seguir)
        Fin_Mientras
FIN_ACCION

"""

def clave(n):
    suma=0
    while n > 9:
        digito=n% 10
        n=n//10
        suma+=digito
    suma+=n
    return suma%7
            
if __name__ == "__main__":
    print("Este algoritmo...")
    seguir=str(input("Desea ingresear un numero?? S para SI: "))
    while seguir=="S":
        num=int(input("Ingrese el número: "))
        print("La clave del número ",num," es: ",clave(num))
        seguir=str(input("Desea ingresar otro número? S para Si: "))