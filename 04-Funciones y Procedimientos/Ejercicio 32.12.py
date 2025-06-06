"""
-----------------------------------------------------
Ejercicio 32.12: 
-----------------------------------------------------
Enunciado:  
Escribir una función que lea desde el teclado las unidades y el precio que quiere comprar, y en función de las 
unidades introducidas le haga un descuento o no (cuando las unidades excedan media docena se aplicará 4% y el 
10% cuando excedan la docena). 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_32.12 ES 
    AMBIENTE 
        desc_6=0,04
        desc_12=0,1
        cant_prod,i,unidad_prod: Entero
        precio_prod: Real
        Funcion descuento(unidad: Entero, precio: Real):Real es
            SI unidad>12 entonces
                descuento:=unidad*precio*desc_12
            SINO
                SI unidad>6 entonces
                    descuento:=unidad*precio*desc_6
                SINO 
                    descuento:=0
                Fin_SI
            Fin_Si
        Fin_Funcion
            
    PROCESO
        Escribir("Este algoritmo calcula el descuento de compras de productos")
        Escribir("Ingrese la cantidad de productos: ")
        Leer(cant_prod)
        Para i:=0 Hasta cant_prod hacer
            Escribir("Ingrese las unidades del producto y el precio")
            Leer(unidad_prod,precio_prod)
            Escribir("Su descuento por este producto es: ",descuento(unidad_prod,precio_prod))
        Fin_Para
        
FIN_ACCION

"""

def descuento(unidad,precio):
    if unidad>12:
        descuento=unidad*precio*desc_12
    elif unidad>6 :
        descuento=unidad*precio*desc_6
    else:
        descuento=0
    return round(descuento,2)
            
if __name__ == "__main__":
    desc_6=0.04
    desc_12=0.1
    print("Este algoritmo calcula el descuento de compras de productos")
    cant_prod=int(input("Ingrese la cantidad de productos: "))
    for i in range (0,cant_prod+1):
        unidad_prod=int(input("Ingrese las unidades del producto: "))
        precio_prod=float(input("Ingrese el precio del producto: "))
        print("Su descuento por este producto es: ",descuento(unidad_prod,precio_prod))
