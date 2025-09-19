"""
-----------------------------------------------------
Ejercicio 10: Calculo total de compra
-----------------------------------------------------
Enunciado:
Escriba un algoritmo que lea el monto total de una compra en un supermercado y determine el total a pagar según 
los siguientes criterios: 
Si el monto de la compra supera los $ 200.000, se aplica un 15% de descuento. 
 
Luego, se consulta el tipo de entrega (el usuario ingresa el número de opción): 
 - Opción 1 → retiro en sucursal, no se suma ningún cargo adicional. 
 - Opción 2 → envío a domicilio dentro de Resistencia, se suma un 5% sobre el monto final. 
 - Opción 3 → envío a domicilio fuera de Resistencia, se suma un 10% sobre el monto final.  


RESOLUCION EN PSEUDOCODIGO

ACCION ordenar ES 
    AMBIENTE 
        retiro_sucursal=1
        envio_resistencia=1,05
        envio_fuera=1,1
        desc_200=0,85
        monto_compra: Real
        eleccion:1...3
    PROCESO
        Escribir("Este algoritmo calcula el monto total de una compra")
        Escribir("Ingrese el monto de la compra")
        Leer(monto_compra)
        SI monto_compra > 200000 entonces
        monto_compra:=monto_compra*desc_200
            Escribir("La compra tiene un descuento del 15% por lo que le sale: ",monto_compra)
        Fin_Si
        Escribir("Elija el tipo de retiro de la compra:
            1 → retiro en sucursal, no se suma ningún cargo adicional. 
            2 → envío a domicilio dentro de Resistencia, se suma un 5% sobre el monto final. 
            3 → envío a domicilio fuera de Resistencia, se suma un 10% sobre el monto final. ")
        Leer(eleccion)
        Segun eleccion hacer
            1: Escribir("El costo final de su compra es: ", monto_compra)
            2: Escribir("El costo final de su compra es: ",(monto_compra*envio_resistencia))
            3: Escribir("El costo final de su compra es: ",(monto_compra*envio_fuera))
FIN_ACCION

"""

def main():
    envio_resistencia=1.05
    envio_fuera=1.1
    desc_200=0.85
    print("Este programa calcula el monto total de una compra")
    monto_compra=float(input("Ingrese el monto de la compra: "))
    if monto_compra>200000:
        monto_compra*=desc_200
        print("La compra tiene un descuento del 15% por lo que le sale: ",monto_compra)
    print("Elija el tipo de retiro de la compra:")
    print("1 → retiro en sucursal, no se suma ningún cargo adicional.")
    print("2 → envío a domicilio dentro de Resistencia, se suma un 5% sobre el monto final.")
    print("3 → envío a domicilio fuera de Resistencia, se suma un 10% sobre el monto final.")
    eleccion=int(input())
    if eleccion==1:
        print("El costo final de su compra es: ", monto_compra)
    elif eleccion==2:
        print("El costo final de su compra es: ",round((monto_compra*envio_resistencia), 2))
    else:
        print("El costo final de su compra es: ",round((monto_compra*envio_fuera), 2))
            
if __name__ == "__main__":
    main()