"""
-----------------------------------------------------
Ejercicio 7: Ordenar números
-----------------------------------------------------
Enunciado:
Escriba un algoritmo que permita ingresar 3 valores numéricos y 
determine cuál es el mayor, el medio y el menor.


RESOLUCION EN PSEUDOCODIGO

ACCION ordenar ES 
    AMBIENTE 
        num1,num2,num3: Real
        menor, medio, mayor: Real
    PROCESO
        Escribir("Este algoritmo determina el menor, el del medio y el mayor de 3 números")
        Escribir("Ingrese los tres números")
        Leer(num1,num2,num3)
        
        SI num1 >= num2 y num1 >= num3 entonces
            mayor:=num3
            si num2 >= num3 entonces
                medio:=num3
                menor:=num2
            sino
                medio:=num2
                menor:=num3
            Fin_si
        SINO
            SI num2 >= num1 y num2 >= num3 entonces
                mayor:=num2
                SI num1>=num3 entonces
                    medio:=num3
                    menor:=num1
                sino
                    medio:=num1
                    menor:=num3
                Fin_si
            SINO
                mayor:=num3
                SI num1 >=num2 entonces
                    medio:=num2
                    menor:=num1
                SINO
                    medio:=num1
                    menor:=num2
                Fin_si
            Fin_SI
        Fin_Si
        
        Escribir("El número menor es: ",menor)
        Escribir("El número del medio es: ",medio)
        Escribir("El número mayor es: ",mayor)
FIN_ACCION

"""
def main():
    print("Este programa determina el número menor, el del medio y el mayor de tres números")
    num1,num2,num3=map(float,input("Ingrese los tres números separados por un espacio: ").split())
    if num1>=num2 and num1>=num3:
        mayor=num1
        if num2>=num3:
            medio=num2
            menor=num3
        else:
            medio=num3
            menor=num2
    elif num2>=num1 and num2>=num3:
        mayor=num2
        if num1>=num3:
            medio=num1
            menor=num3
        else:
            medio=num3
            menor=num1
    else:
        mayor=num3
        if num1>=num2:
            medio=num1
            menor=num2
        else:
            medio=num2
            menor=num1
    
    print("El número menor es: ",menor)
    print("El número del medio es: ",medio)
    print("El número mayor es: ",mayor)

if __name__ == "__main__":
    main()