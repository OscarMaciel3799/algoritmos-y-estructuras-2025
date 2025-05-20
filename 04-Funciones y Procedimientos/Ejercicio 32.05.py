"""
-----------------------------------------------------
Ejercicio 32.05: Es caracter?
-----------------------------------------------------
Enunciado:  
Escribir una función que verifique si un caracter introducido es un dígito o no.

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_5 ES 
    AMBIENTE 
        digito: Caracter
        Funcion es_caracter(s:Caracter): Booleano
            SI s='0' o S='1' o S='2' o S='3' o S='4' o S='5' o S='6' o S='7' o S='8' o S='9' entonces
                es_caracter:=verdadero
            SINO
                es_caracter:=falso
            Fin_si
        Fin_Funcion
    PROCESO
        Escribir("Este algoritmo verifica si un caracter introducido es un dígito o no.")
        Escribir("Ingrese un Caracter")
        Leer(digito)
        SI es_caracter(digito) entonces
            Escribir("El caracter ",digito," es un digito")
        SINO
            Escribir("El caracter ",digito," NO es un digito")
        FIn_Si
FIN_ACCION

"""

def es_caracter(s):
    if s in ("0","1","2","3","4","5","6","7","8","9"):
        return True
    else: 
        return False
            
if __name__ == "__main__":
    print("Este algoritmo verifica si un caracter introducido es un dígito o no.")
    digito=str(input("Ingrese un Caracter: "))
    if len(digito)==1:
        if es_caracter(digito):
            print("El caracter ",digito," es un digito")
        else:
            print("El caracter ",digito," NO es un digito")
    else:
        print("El valor ingresado no es un caracter")