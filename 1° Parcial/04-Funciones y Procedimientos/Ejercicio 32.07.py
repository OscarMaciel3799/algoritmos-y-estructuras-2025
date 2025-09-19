"""
-----------------------------------------------------
Ejercicio 32.07: Es caracter?
-----------------------------------------------------
Enunciado:  
Repita el ejercicio del punto 5 pero utilice procedimiento en lugar de función. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_5 ES 
    AMBIENTE 
        digito: Caracter
        Procedimiento es_caracter(s:Caracter) es
            SI s='0' o s='1' o s='2' o s='3' o s='4' o s='5' o s='6' o s='7' o s='8' o s='9' entonces
                Escribir("El caracter ",s," es un digito")
            SINO
                Escribir("El caracter ",s," NO es un digito")
            Fin_si
        Fin_Procedimiento
    PROCESO
        Escribir("Este algoritmo verifica si un caracter introducido es un dígito o no.")
        Escribir("Ingrese un Caracter")
        Leer(digito)
        es_caracter(digito)
FIN_ACCION

"""

def es_caracter(s):
    if s in ("0","1","2","3","4","5","6","7","8","9"):
        print("El caracter ",s," es un digito")
    else: 
        print("El caracter ",s," NO es un digito")
            
if __name__ == "__main__":
    print("Este algoritmo verifica si un caracter introducido es un dígito o no.")
    digito=str(input("Ingrese un Caracter: "))
    if len(digito)==1:
        es_caracter(digito)
    else:
        print("El valor ingresado no es un caracter")
