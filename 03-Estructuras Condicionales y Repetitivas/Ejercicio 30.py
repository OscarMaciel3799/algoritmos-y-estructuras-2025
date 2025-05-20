"""
-----------------------------------------------------
Ejercicio 30: 
-----------------------------------------------------
Enunciado:  
Escriba un algoritmo que acepte un número entero que representa una suma de dinero e indique cuántos billetes 
de cada denominación necesita, suponiendo que solo existen billetes de 500, 100, 50, 20, 10, 5 y 1 peso

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_30 ES 
    AMBIENTE 
        monto,i: Entero
        billetes=(500, 100, 50, 20, 10, 5, 1)
        b_500,b_100,b_50,b_20,b_10,b_5,b_1: Entero
        
    PROCESO
        Escribir("Este algoritmo ....")
        Escribir("Ingrese la cantidad de dinero: ")
        Leer(monto)
        Mientras monto > 0 hacer
            segun monto hacer
                >=500 : 
                        b_500:=monto DIV 500
                        monto:=monto MOD 500
                >=100 : 
                        b_100:=monto DIV 100
                        monto:=monto MOD 100
                >=50 : 
                        b_50:=monto DIV 50
                        monto:=monto MOD 50
                >=20 : 
                        b_20:=monto DIV 20
                        monto:=monto MOD 20
                >=10 : 
                        b_10:=monto DIV 10
                        monto:=monto MOD 10
                >=5 : 
                        b_5:=monto DIV 5
                        monto:=monto MOD 5
                >=1 : 
                        b_1:=monto DIV 1
                        monto:=monto MOD 1        
            Fin Segun
        Fin Mientras
        Escribir("La cantidad de billetes de 500 es: ",b_500)
        Escribir("La cantidad de billetes de 100 es: ",b_100)
        Escribir("La cantidad de billetes de 50 es: ",b_50)
        Escribir("La cantidad de billetes de 20 es: ",b_20)
        Escribir("La cantidad de billetes de 10 es: ",b_10)
        Escribir("La cantidad de billetes de 5 es: ",b_5)
        Escribir("La cantidad de billetes de 1 es: ",b_1)
        
FIN_ACCION

"""

def main():
    print("Este algoritmo calcula cuántos billetes se necesitan para representar una cantidad de dinero.")
    monto = int(input("Ingrese la cantidad de dinero: "))

    b_500 = b_100 = b_50 = b_20 = b_10 = b_5 = b_1 = 0

    while monto > 0:
        if monto >= 500:
            b_500 = monto // 500
            monto = monto % 500
        elif monto >= 100:
            b_100 = monto // 100
            monto = monto % 100
        elif monto >= 50:
            b_50 = monto // 50
            monto = monto % 50
        elif monto >= 20:
            b_20 = monto // 20
            monto = monto % 20
        elif monto >= 10:
            b_10 = monto // 10
            monto = monto % 10
        elif monto >= 5:
            b_5 = monto // 5
            monto = monto % 5
        elif monto >= 1:
            b_1 = monto // 1
            monto = monto % 1

    print("La cantidad de billetes de 500 es:", b_500)
    print("La cantidad de billetes de 100 es:", b_100)
    print("La cantidad de billetes de 50 es:", b_50)
    print("La cantidad de billetes de 20 es:", b_20)
    print("La cantidad de billetes de 10 es:", b_10)
    print("La cantidad de billetes de 5 es:", b_5)
    print("La cantidad de billetes de 1 es:", b_1)
            
if __name__ == "__main__":
    main()
