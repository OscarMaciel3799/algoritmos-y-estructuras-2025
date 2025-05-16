"""
-----------------------------------------------------
Ejercicio 12: Unidad, Decena y Centena
-----------------------------------------------------
Enunciado:
Escriba un algoritmo que acepte un número entero mayor a 100 y menor a 1000, y muestre cómo está compuesto 
(unidades, decenas y centenas) y si es múltiplo de 3.   


RESOLUCION EN PSEUDOCODIGO

ACCION descomposicion ES 
    AMBIENTE 
        num,decena,centena,unidad: Entero
        
    PROCESO
        Escribir("Este algoritmo descompone un número en unidad, decena y centena")
        Escribir("Ingrese el un número entre 100 y 1000")
        Leer(num)
        unidad:= num MOD 10
        decena:= (num DIV 10) MOD 10
        centena:= num DIV 100
        Escribir("La centena es: ",centena)
        Escribir("La decena es: ",decena)
        Escribir("La unidad es: ",unidad)
        Si num MOD 3 = 0 entonces
            Escribir("El número ",num," es multiplo de 3")
        SINO
            Escribir("El número ",num," NO es multiplo de 3")
        Fin_SI
FIN_ACCION

"""

def main():
    print("Este programa descompone un número en unidad, decena y centena")
    num=int(input("Ingrese un número entre 100 y 1000: "))
    print("La centena es: ",(int(num/100)))
    print("La decena es: ",(int((num/10)%10)))
    print("La unidad es: ", (num%10))
    if num%3==0:
        print("El número ",num," es multiplo de 3")
    else:
        print("El número ",num," NO es multiplo de 3")
    
    

if __name__ == "__main__":
    main()