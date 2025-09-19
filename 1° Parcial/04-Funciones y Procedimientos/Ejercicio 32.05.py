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
        Funcion es_caracter(s:Caracter): Alfanumerico es
            SI s='0' o s='1' o s='2' o s='3' o s='4' o s='5' o s='6' o s='7' o s='8' o s='9' entonces
                es_caracter:=" es un digito"
            SINO
                es_caracter:=" NO es un digito"
            Fin_si
        Fin_Funcion
    PROCESO
        Escribir("Este algoritmo verifica si un caracter introducido es un dígito o no.")
        Escribir("Ingrese un Caracter")
        Leer(digito)
        Escribir("El caracter ",digito,es_caracter(digito))
FIN_ACCION

"""

def es_caracter(s):
    if s in ("0","1","2","3","4","5","6","7","8","9"):
        return " es un digito"
    else: 
        return " NO es un digito"
            
if __name__ == "__main__":
    print("Este algoritmo verifica si un caracter introducido es un dígito o no.")
    digito=str(input("Ingrese un Caracter: "))
    if len(digito)==1:
        print("El caracter ",digito,es_caracter(digito))
    else:
        print("El valor ingresado no es un caracter")