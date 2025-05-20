"""
-----------------------------------------------------
Ejercicio 31: 
-----------------------------------------------------
Enunciado:  
Todo número cuya suma de sus dígitos sea múltiplo de 3 lo es también. 
Ej: 117  →    1+1+7 = 9 que es múltiplo de 3 , entonces 117 es múltiplo de 3 
Realizar un algoritmo que determine si un número es múltiplo de 3 en función de la afirmación antes realizada. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_31 ES 
    AMBIENTE 
        numero,suma,digito: Entero
    PROCESO
        Escribir("Este algoritmo determina si un número es múltiplo de 3 sumando sus dígitos.")
        Escribir("Ingrese un número entero: ")
        Leer(numero)
        suma:=0

        Mientras numero > 0 Hacer
            digito:=numero MOD 10
            suma:=suma + digito
            numero:=numero DIV 10
        FinMientras

        Si suma MOD 3 = 0 Entonces
            Escribir("El número es múltiplo de 3")
        Sino
            Escribir("El número no es múltiplo de 3")
        FinSi
        
FIN_ACCION

"""

def main():
    print("Este algoritmo determina si un número es múltiplo de 3 sumando sus dígitos.")
    numero = int(input("Ingrese un número entero: "))
    aux=numero
    suma_digitos = 0
    while numero>0:
        digito=int(numero%10)
        suma_digitos += digito
        numero=numero//10
    

    if suma_digitos % 3 == 0:
        print(f"{aux} es múltiplo de 3, porque la suma de sus dígitos ({suma_digitos}) es múltiplo de 3.")
    else:
        print(f"{aux} no es múltiplo de 3, porque la suma de sus dígitos ({suma_digitos}) no es múltiplo de 3.")
            
if __name__ == "__main__":
    main()
