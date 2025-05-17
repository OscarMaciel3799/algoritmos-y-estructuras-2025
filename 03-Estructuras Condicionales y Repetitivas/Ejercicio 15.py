"""
-----------------------------------------------------
Ejercicio 15: Calculo de altura de Edificios
-----------------------------------------------------
Enunciado:  
a) Hacer un algoritmo que calcule la altura aproximada de un edificio en pies, ingresando como dato la cantidad 
de pisos del mismo y la altura promedio de cada piso, en metros. (1 m = 3.28 pies) 
b) Modifique el algoritmo del punto a) para que permita calcular la altura de 50 edificios. 
c) Modifique el algoritmo del punto a) para que permita calcular la altura de una cantidad indeterminada de 
edificios. Prevea una condición de fin. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_15a ES 
    AMBIENTE
        metros_a_pies=3,28 
        cantidad_pisos: Entero
        altura_promedio: Real
        
    PROCESO
        Escribir("Este algoritmo calcula la altura en pies de un edificio")
        Escribir("Ingrese la cantidad de pisos y la altura promedio en pies")
        Leer(cantidad_pisos,altura_promedio)
        Escribir("La altura del edificio es: ",(cantidad_pisos*altura_promedio*metros_a_pies)," pies.")
FIN_ACCION

ACCION ejercicio_15b ES 
    AMBIENTE
        metros_a_pies=3,28 
        cantidad_pisos: Entero
        altura_promedio: Real
        edificio: Entero
    PROCESO
        Escribir("Este algoritmo calcula la altura en pies de 50 edificios")
        Para edificio:=1 hasta 50 hacer
            Escribir("Ingrese la cantidad de pisos y la altura promedio en pies, para el edificio N°",edificio)
            Leer(cantidad_pisos,altura_promedio)
            Escribir("La altura del edificio N°",edificio," es: ",(cantidad_pisos*altura_promedio*metros_a_pies)," pies.")
        Fin_Para
FIN_ACCION

ACCION ejercicio_15c ES 
    AMBIENTE
        metros_a_pies=3,28 
        cantidad_pisos: Entero
        altura_promedio: Real
        seguir: ('V','F')
    PROCESO
        Escribir("Este algoritmo calcula la altura en pies de una cantidad indefinida de edificios")
        Escribir("Desea ingresar la cantidad de pisos y la altura promedio en pies para el primer edificio? V para SI, F para NO")
        Leer(seguir)
        Mientras seguir='V' hacer
            Escribir("Ingrese la cantidad de pisos y la altura promedio en pies")
            Leer(cantidad_pisos,altura_promedio)
            Escribir("La altura del edificio es: ",(cantidad_pisos*altura_promedio*metros_a_pies)," pies.")
            Escribir("Desea ingresar los datos de otro edificio? V para SI, F para NO")
        Fin_Mientras
FIN_ACCION

"""

def a():
    print("Este programa calcula la altura en pies de un edificio")
    cantidad_pisos=int(input("Ingrese la cantidad de pisos: "))
    altura_promedio=float(input("Ingrese la altura promedio en pies: "))
    total=round((cantidad_pisos*altura_promedio*metros_a_pies),2)
    print("La altura del edificio es: ",total," pies.")
    
def b():
    print("Este programa calcula la altura en pies de 50 edificios")
    for edificio in range(1,50):
        cantidad_pisos=int(input("Ingrese la cantidad de pisos del edificio",edificio,": "))
        altura_promedio=float(input("Ingrese la altura promedio en pies del edificio",edificio,": "))
        total=round((cantidad_pisos*altura_promedio*metros_a_pies),2)
        print("La altura del edificio N°",edificio," es: ",total," pies.")
    
def c():
    print("Este programa calcula la altura en pies de una cantidad indefinida de edificios")
    seguir=str(input("Desea ingresar la cantidad de pisos y la altura promedio en pies para el primer edificio? V para SI, F para NO: "))
    while seguir=="V":
        cantidad_pisos=int(input("Ingrese la cantidad de pisos del edificio: "))
        altura_promedio=float(input("Ingrese la altura promedio en pies del edificio: "))
        total=round((cantidad_pisos*altura_promedio*metros_a_pies),2)
        print("La altura del edificio es: ",total," pies.")
        seguir=str(input("Desea ingresar los datos de otro edificio? V para SI, F para NO: "))
        
        
if __name__ == "__main__":
    metros_a_pies=3.28
    a()
    #b()
    #c()