"""
-----------------------------------------------------
Ejercicio 10: Conversion de monedas
-----------------------------------------------------
Enunciado:
Una persona decide realizar un viaje a Europa, para lo cual necesita una determinada cantidad de euros.
La persona tiene ahorrada una cierta suma en dólares y desea saber si es suficiente y, 
en caso de haber diferencia (de más o de menos) a cuántos pesos equivale.
Realice un algoritmo que solucione el problema, para lo cual deberá prever que se ingresen las equivalencias 
de monedas que considere necesarias (por ejemplo  la cotización en pesos de  dólar y/o del euro, 
o a cuantos euros equivale un dólar).   


RESOLUCION EN PSEUDOCODIGO

ACCION ordenar ES 
    AMBIENTE 
        dolares_a_euros=0,90
        euros_a_pesos= 1275,83
        precio_euros,ahorro_dolares,diferencia_pesos: Real
        
    PROCESO
        Escribir("Este algoritmo calcula la diferencia entre el precio del viaje y la cantidad ahorrada")
        Escribir("Ingrese el costo del viaje en euros")
        Leer(precio_euros)
        Escribir("Ingrese la cantidad ahorrada en dolares")
        Leer(ahorro_dolares)
        diferencia:= (precio_euros-ahorro_dolares*dolares_a_euros)*euros_a_pesos
        SI diferencia <= 0 entonces
            Escribir("Tiene la cantidad de dinero necesaria para el viaje y le sobra: ",diferencia)
        SINO
            Escribir("No le alcanza para pagar el viaje, le falta: ",diferencia)
        Fin_SI
FIN_ACCION

"""
def main():
    dolares_a_euros=0.90
    euros_a_pesos= 1275.83
    print("Este programa calcula la diferencia entre el precio del viaje y la cantidad ahorrada")
    precio_euros=float(input("Ingrese el costo del viaje en euros: "))
    ahorro_dolares=float(input("Ingrese la cantidad ahorrada en dolares: "))
    diferencia=(precio_euros-ahorro_dolares*dolares_a_euros)*euros_a_pesos
    if diferencia <= 0:
        print("Tiene la cantidad de dinero necesaria para el viaje y le sobra: ",diferencia)
    else:
        print("No le alcanza para pagar el viaje, le falta: ",diferencia," pesos.")

if __name__ == "__main__":
    main()