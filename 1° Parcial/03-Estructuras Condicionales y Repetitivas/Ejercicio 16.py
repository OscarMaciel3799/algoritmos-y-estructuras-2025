"""
-----------------------------------------------------
Ejercicio 16: Calcular porcentajes de egresados
-----------------------------------------------------
Enunciado:  
a) Diseñe un algoritmo que obtenga el porcentaje de alumnos de ISI, IQ e IEM, sobre el total de egresados de la 
UTN-FRRe de un año. 
b) Modifique el algoritmo del punto a) para que permita obtener e informar los mismos porcentajes, pero para 
varias Facultades y al final emitir el total de alumnos por carrera y total general. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_16a ES 
    AMBIENTE 
        isi,iq,iem,total: Entero
    PROCESO
        Escribir("Este algoritmo calcula el porcentaje de egresados por carrera")
        Escribir("Ingrese la cantidad de egresados que tuvo ISI,IQ e IEM en ese orden")
        Leer(isi,iq,iem)
        total:=isi+iq+iem
        Escribir("El porcentaje de alumnos que se recibieron de ISI es: ",(isi*100/total),"%")
        Escribir("El porcentaje de alumnos que se recibieron de IQ es: ",(iq*100/total),"%")
        Escribir("El porcentaje de alumnos que se recibieron de IEM es: ",(iem*100/total),"%")
FIN_ACCION

ACCION ejercicio_16b ES 
    AMBIENTE 
        isi,iq,iem,total,total_isi,total_iq,total_iem,total_general: Entero
        seguir:('V','F')
    PROCESO
        Escribir("Este algoritmo calcula el porcentaje de egresados por carrera para un número indefinido de facultades")
        total_general:=0
        total_isi:=0
        total_iq:=0
        total_iem:=0
        Escribir("Quiere ingresar los datos de la primera facultad? V para SI, F para NO")
        Leer(seguir)
        Mientras seguir='V' hacer
            Escribir("Ingrese la cantidad de egresados que tuvo ISI,IQ e IEM en ese orden")
            Leer(isi,iq,iem)
            total_isi:=total_isi+isi
            total_iq:=total_iq+iq
            total_iem:=total_iem+iem
            total:=isi+iq+iem
            total_general:=total_general+total
            Escribir("El porcentaje de alumnos que se recibieron de ISI en esta facultad es: ",(isi*100/total),"%")
            Escribir("El porcentaje de alumnos que se recibieron de IQ en esta facultad es: ",(iq*100/total),"%")
            Escribir("El porcentaje de alumnos que se recibieron de IEM en esta facultad es: ",(iem*100/total),"%")
            Escribir("Desea ingresar los datos de la siguiente facultad? V para SI, F para NO")
            Leer(seguir)
        Fin_Mientras
        Si total_general=0 entonces
            Escribir("El total de alumnos que se recibieron en todas las facultades es: ",total_general)
            Escribir("El porcentaje de alumnos que se recibieron de ISI en todas las facultades es: ",(0),"%")
            Escribir("El porcentaje de alumnos que se recibieron de IQ een todas las facultades es: ",(0),"%")
            Escribir("El porcentaje de alumnos que se recibieron de IEM en todas las facultades es: ",(0),"%")
        Sino
            Escribir("El total de alumnos que se recibieron en todas las facultades es: ",total_general)
            Escribir("El porcentaje de alumnos que se recibieron de ISI en todas las facultades es: ",(total_isi*100/total_general),"%")
            Escribir("El porcentaje de alumnos que se recibieron de IQ een todas las facultades es: ",(total_iq*100/total_general),"%")
            Escribir("El porcentaje de alumnos que se recibieron de IEM en todas las facultades es: ",(total_iem*100/total_general),"%")
        Fin_Si
FIN_ACCION

"""

def a():
    print("Este programa calcula el porcentaje de egresados por carrera")
    isi,iq,iem=map(int,input("Ingrese la cantidad de egresados que tuvo ISI,IQ e IEM en ese orden: ").split())
    total=isi+iq+iem
    print("El porcentaje de alumnos que se recibieron de ISI es: ",round((isi*100/total),2),"%")
    print("El porcentaje de alumnos que se recibieron de IQ es: ",round((iq*100/total),2),"%")
    print("El porcentaje de alumnos que se recibieron de IEM es: ",round((iem*100/total),2),"%")

def b():
    print("Este programa calcula el porcentaje de egresados por carrera para un número indefinido de facultades")
    total_general=0
    total_isi=0
    total_iq=0
    total_iem=0
    seguir=str(input("Quiere ingresar los datos de la primera facultad? V para SI, F para NO: "))
    while seguir=='V':
        isi,iq,iem=map(int,input("Ingrese la cantidad de egresados que tuvo ISI,IQ e IEM en ese orden: ").split())
        total_isi+=isi
        total_iq+=iq
        total_iem+=iem
        total=isi+iq+iem
        total_general+=total
        print("El porcentaje de alumnos que se recibieron de ISI en esta facultad es: ",round((isi*100/total),2),"%")
        print("El porcentaje de alumnos que se recibieron de IQ en esta facultad es: ",round((iq*100/total),2),"%")
        print("El porcentaje de alumnos que se recibieron de IEM en esta facultad es: ",round((iem*100/total),2),"%")
        seguir=str(input("Desea ingresar los datos de la siguiente facultad? V para SI, F para NO: "))
    if total_general==0:
        print("El total de alumnos que se recibieron en todas las facultades es: ",total_general)
        print("El porcentaje de alumnos que se recibieron de ISI en todas las facultades es: ",(0),"%")
        print("El porcentaje de alumnos que se recibieron de IQ een todas las facultades es: ",(0),"%")
        print("El porcentaje de alumnos que se recibieron de IEM en todas las facultades es: ",(0),"%")
    else:
        print("El total de alumnos que se recibieron en todas las facultades es: ",total_general)
        print("El porcentaje de alumnos que se recibieron de ISI en todas las facultades es: ",round((total_isi*100/total_general),2),"%")
        print("El porcentaje de alumnos que se recibieron de IQ een todas las facultades es: ",round((total_iq*100/total_general),2),"%")
        print("El porcentaje de alumnos que se recibieron de IEM en todas las facultades es: ",round((total_iem*100/total_general),2),"%")
    
        
        
if __name__ == "__main__":
    a()
    b()