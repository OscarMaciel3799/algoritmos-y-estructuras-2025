"""
-----------------------------------------------------
Ejercicio 9: Calcular la edad
-----------------------------------------------------
Enunciado:
Escriba un algoritmo que permita conocer la edad de una persona, con solo ingresar la fecha de nacimiento y la 
fecha actual, ambas en el formato: DIA, MES, AÑO.  


RESOLUCION EN PSEUDOCODIGO

ACCION ordenar ES 
    AMBIENTE 
        dia_nacimiento,mes_nacimiento,año_nacimiento: Entero
        dia_actual,mes_actual,año_actual: Entero
    PROCESO
        Escribir("Este algoritmo calcula la edad de una persona")
        Escribir("Ingrese la fecha de nacimiento siguiendo el siguiente formato: DIA,MES,AÑO")
        Leer(dia_nacimiento,mes_nacimiento,año_nacimiento)
        Escribir("Ingrese la fecha de actual siguiendo el siguiente formato: DIA,MES,AÑO")
        Leer(dia_actual,mes_actual,año_actual)
        SI año_actual = año_nacimiento entonces
            Escribir("Tiene Cero años")
        SINO
            SI mes_nacimiento <= mes_actual entonces
                Si dia_nacimiento <= dia actual entonces
                    Escribir("La edad es: ",(año_actual-año_nacimiento))
                sino
                    Escribir("La edad es: ", (año_actual-año_nacimiento-1))
                FIn_Si
            SINO
                Escribir("La edad es: ", (año_actual-año_nacimiento-1))
            Fin_Si
        Fin_SI
FIN_ACCION

"""

def main():
    print("Este programa calcula la edad de una persona")
    dia_nacimiento,mes_nacimiento,año_nacimiento=map(int,input("Ingrese la fecha de nacimiento siguiendo el siguiendo el siguinte formato DIA MES AÑO: ").split())
    dia_actual,mes_actual,año_actual=map(int,input("Ingrese la fecha actual siguiendo el siguiendo el siguinte formato DIA MES AÑO: ").split())
    if año_nacimiento == año_actual:
        print("La edad es Cero años.")
    else:
        if mes_nacimiento<=mes_actual:
            if dia_nacimiento<=dia_actual:
                print("La edad es: ",(año_actual-año_nacimiento)," años.")
            else:
                print("La edad es: ",(año_actual-año_nacimiento-1)," años.")
        else:
            print("La edad es: ",(año_actual-año_nacimiento-1)," años.")

if __name__ == "__main__":
    main()