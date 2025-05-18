"""
-----------------------------------------------------
Ejercicio 22: Estafas al cliente
-----------------------------------------------------
Enunciado:  
Escribir un algoritmo que, dado un importe dinero, permita calcular e informar cuánto corresponde pagar por un 
impuesto, en cuántas cuotas y el valor de las mismas. Tener en cuenta los siguientes datos: 
 
 - IMPUESTO = 10% del importe dado. 
 - Los importes mayores que $ 10.000 y menor  o igual que $ 50.000 se pagan en dos cuotas. 
 - Los mayores de $ 50.000 en tres cuotas. 
El algoritmo debe permitir tratar varios importes, finalizando cuando se ingresa 9999 como importe.

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_22 ES 
    AMBIENTE 
        importe,impuesto: Real
        Seguir:('V','F')
    PROCESO
        Escribir("Este algoritmo estafa al cliente")
        Escribir("Desea ingresar el primer importe? V para SI, F para NO")
        Leer(seguir)
        Mientras seguir='V' hacer
            Escribir("Ingrese el importe de dinero")
            Leer(importe)
            impuesto:=importe*0,1
            Si impuesto > 10000 y impuesto< 50000 entonces
                Escribir("Su impuesto puede ser pagado en dos cuotas")
            SINO
                SI impuesto > 50000
                    Escribir("Su impuesto puede ser pagado en tres cuotas")
                Fin_SI
            Fin_Si
            Escribir("Desea ingresar otro importe? V para SI, F para NO")
            Leer(seguir)
        Fin_Mientras
FIN_ACCION

"""

def main():
    print("Este algoritmo estafa al cliente")
    seguir=str(input("Desea ingresar el primer importe? V para SI, F para NO: "))
    while seguir=="V":
        importe=float(input("Ingrese el importe de dinero: "))
        impuesto=importe*0.1
        print("Su impuesto es de: ",impuesto)
        if impuesto > 10000 and impuesto < 50000:
            print("Y puede ser pagado en dos cuotas")
        elif impuesto > 50000:
            print("Y puede ser pagado en tres cuotas")
        
        seguir=str(input("Desea ingresar otro importe? V para SI, F para NO: "))
        
            
if __name__ == "__main__":
    main()
