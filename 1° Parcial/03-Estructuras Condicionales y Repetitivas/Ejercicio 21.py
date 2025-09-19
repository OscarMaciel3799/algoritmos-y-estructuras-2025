"""
-----------------------------------------------------
Ejercicio 21: 
-----------------------------------------------------
Enunciado:  
Escriba un algoritmo para calcular cada renglón de una factura (valor unitario * cantidad vendida) y el total de la 
misma, suponiendo que el número de renglones es variable. Emitir un mensaje de error si el valor unitario es <= 0. 
Realizar la prueba de escritorio con los siguientes valores: 
     Cantidad de renglones: 4 
|Valor Unitario | Cantidad vendida |
|   2           |       10         |
|   1           |       25         | 
|   3           |       15         | 
|   2           |       8,5        | 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_21 ES 
    AMBIENTE 
        cantidad_reglones,i: Entero
        valor_unitario,cantidad_vendida: Real
    PROCESO
        Escribir("Este algoritmo calcula el total de ventas por producto/reglón de una factura")
        Escribir("Ingrese la cantidad de reglones de la misma")
        Leer(cantidad_reglones)
        Para i:=1 hasta cantidad_reglones hacer
            Escribir("Ingrese el valor unitario del producto ",i," y la cantidad vendida")
            Leer(valor_unitario,cantidad_vendida)
            Si valor_unitario <> 0 entonces
                Escribir("El monto total del reglon ",i," es: ",(valor_unitario*cantidad_vendida))
            SINO
                Escribir("El valor unitario es 0 por lo que se omite este producto")
            Fin_Si
        Fin_Para
FIN_ACCION

"""

def main():
    print("Este programa calcula el total de ventas por producto/reglón de una factura")
    cantidad_reglones=int(input("Ingrese la cantidad de reglones de la misma: "))
    for i in range(1,cantidad_reglones+1):
        valor_unitario,cantidad_vendida=map(float,input(f"Ingrese el valor unitario del producto {i} y la cantidad vendida separadas por un espacio: ").split())
        if valor_unitario != 0:
            print("El monto total del producto ",i," es: ",(valor_unitario*cantidad_vendida))
        else:
            print("El valor unitario es 0 por lo que se omite este producto")
        
            
if __name__ == "__main__":
    main()
