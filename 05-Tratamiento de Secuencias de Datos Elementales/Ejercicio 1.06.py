"""
-----------------------------------------------------
Ejercicio 1.06: 
-----------------------------------------------------
Enunciado:  
Dada una secuencia de enteros que almacena la cantidad de habitantes de las ciudades capitales de las 23 
provincias de la República Argentina, discriminados 4 categorías: menores de 18 años (varones y mujeres) y mayores 
de 18 años (varones y mujeres). Se pide determinar la población total y los siguientes porcentajes: masculinos, 
femeninos, mayores de 18 y menores de 18. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.06 ES 
    AMBIENTE 
        s: Secuencia de Enteros
        v,pos,opcion: Entero
        total,menor_H,menor_M,mayor_H,mayor_M: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(s)
        Avanzar(s,v)
        menor_H:=0
        menor_M:=0
        mayor_H:=0
        mayor_M:=0
        Para pos:=1 Hasta 92 hacer
            opcion:=pos MOD 4
            Segun opcion hacer
                1: menor_H:=menor_H+v
                2: menor_M:=menor_M+v
                3: mayor_H:=mayor_H+v
                0: mayor_M:=mayor_M+v
            Fin_Segun
            Avanzar(s,v)
        Fin_Para
        total:=menor_H+menor_M+mayor_H+mayor_M
        
        Escribir("El total de habitantes es: ",total)
        Escribir("El porcentaje de habitantes masculinos es: ",(menor_H+mayor_H)*100/total)
        Escribir("El porcentaje de habitantes femeninos es es: ",(menor_M+mayor_M)*100/total)
        Escribir("El porcentaje de habitantes mayores de 18 es: ",(mayor_M+mayor_H)*100/total)
        Escribir("El porcentaje de habitantes menores de 18 es: ",(menor_H+menor_M)*100/total)
FIN_ACCION

"""
#A fines practicos en python las secuencias las consideraremos Listas
#Y usaremos bucles para recorrer las secuencias
def main():
    print("Este algoritmo ....")
    sec=input("Ingrese la secuencia de habitantes separados por coma: ").split(',')
    #1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4
    
    for i in range(0,92):
            opcion=int(i % 4)
            v=sec[i]
            opciones(opcion,v)
            
    total=menor_H+menor_M+mayor_H+mayor_M
        
    print("El total de habitantes es: ",total)
    print("El porcentaje de habitantes masculinos es: ",(menor_H+mayor_H)*100/total)
    print("El porcentaje de habitantes femeninos es es: ",(menor_M+mayor_M)*100/total)
    print("El porcentaje de habitantes mayores de 18 es: ",(mayor_M+mayor_H)*100/total)
    print("El porcentaje de habitantes menores de 18 es: ",(menor_H+menor_M)*100/total)

def opciones(n,v):
    global menor_H, menor_M, mayor_H, mayor_M
    v=int(v)
    match n:
        case 1: menor_H+=v
        case 2: menor_M+=v
        case 3: mayor_H+=v
        case 4: mayor_M+=v

if __name__ == "__main__":
    menor_H=0
    menor_M=0
    mayor_H=0
    mayor_M=0
    main()
