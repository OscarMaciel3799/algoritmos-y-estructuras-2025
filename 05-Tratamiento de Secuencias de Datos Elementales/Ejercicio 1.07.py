"""
-----------------------------------------------------
Ejercicio 1.07: 
-----------------------------------------------------
Enunciado:  
Se tiene una secuencia de enteros que contiene todos los CUIT de los empleados de una empresa, la misma 
termina con el CUIT 0. Para evitar largas esperas en los días de pago, la empresa necesita organizarlos de acuerdo 
al último dígito de su documento, generar una secuencia con los CUIT de las personas que su número de documento 
termine con 0, 1, 2 o 3. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.07 ES 
    AMBIENTE 
        s,sal: Secuencia de Enteros
        v: Enteros
        opciones=(0,1,2,3)
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(s)
        Avanzar(s,v)
        Crear(sal)
        Mientras v<>0 hacer
            SI v MOD 10 EN opciones entonces
                Escribir(sal,v)
            FIn_SI
            Avanzar(s,v)
        Fin_Mientras
        Cerrar(sal)
FIN_ACCION

"""
#A fines practicos en python las secuencias las consideraremos Listas
#Y usaremos bucles para recorrer las secuencias
def main():
    print("Este algoritmo ....")
    sec=input("Ingrese la secuencia de cuits separados por coma: ").split(',')
    # 20345678901,27123456789,20234567890,23345678901,27234567891,20312345678,20239876543,27112233445,23234567890,20398765432,0
    opciones={0,1,2,3}
    sal=[]
    pos=0
    v=int(sec[pos])
    while v!=0:
        if v%10 in opciones:
            sal.append(v)
        pos+=1
        v=int(sec[pos])
    print("Los cuits que terminan en 0, 1, 2 o 3 son: ",sal)
            
if __name__ == "__main__":
    main()
