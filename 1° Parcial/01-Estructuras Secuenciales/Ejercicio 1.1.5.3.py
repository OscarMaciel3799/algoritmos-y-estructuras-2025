"""
-----------------------------------------------------
Ejercicio 1.1.5.3: Calcular el precio total de la venta
-----------------------------------------------------
Enunciado:
Se desea comprar una PC y una impresora. Calcular el precio total: el cual está dado por 
la suma de los precios de costos, los porcentajes de ganancia del vendedor y un 21% de IVA.
Supóngase una ganancia del vendedor del 12% por la PC y 7% por la impresora. Se leen los
costos y se imprimen el precio total de ventas.



RESOLUCION EN PSEUDOCODIGO

ACCION calculo_venta ES 
    AMBIENTE 
        ganancia_pc= 1,12
        ganancia_impresora= 1,07
        iva= 1,21
        costo_pc,costo_impresora,total: Real
    PROCESO
        Escribir("Este algoritmo calcula el precio total de la venta")
        Escribir("Ingrese el costo de la pc y el costo de la impresora")
        Leer(costo_pc,costo_impresora)
        total:= (costo_pc*ganancia_pc+costo_impresora*ganancia_impresora)*iva
        Escribir("El costo total de la venta es: ",total)
FIN_ACCION

"""

def main():
    ganancia_pc=1.12
    ganancia_impresora=1.07
    iva=1.21
    print("Este programa el precio total de la venta")
    costo_pc,costo_impresora=map(float,input("Ingrese el costo de la pc y el costo de la impresora separados por espacios: ").split())
    total=(costo_pc*ganancia_pc+costo_impresora*ganancia_impresora)*iva
    print("El precio de la venta es: ",total)

if __name__ == "__main__":
    main()