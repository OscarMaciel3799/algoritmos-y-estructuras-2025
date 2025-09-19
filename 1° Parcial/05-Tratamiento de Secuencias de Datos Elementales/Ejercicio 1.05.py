"""
-----------------------------------------------------
Ejercicio 1.05: Secuencia de Socios que no figuran
-----------------------------------------------------
Enunciado:  
La secuencia de  socios del problema anterior tiene el inconveniente  de que los números están ordenados pero 
no son correlativos.  Se desea generar una secuencia que contenga los números de socios que no figuran en la 
secuencia de socios. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.05 ES 
    AMBIENTE 
        s,sal: Secuencia de Enteros
        v,pos: Entero
    PROCESO
        Escribir("Este algoritmo genera una secuencia que contenga los números de socios que no figuran en la 
secuencia de socios.")
        Crear(sal)
        Arrancar(s)
        Avanzar(s,v)
        pos:=v
        Mientras NFDS(s) hacer
            Mientras pos<v hacer
                Escribir(sal,pos)
                pos:=pos+1
            Fin_Mientras
            pos:=pos+1
            avanzar(s,v)
        Fin_Mientras
        Cerrar(s)
        Cerrar(sal)
        
FIN_ACCION

"""
#A fines practicos en python las secuencias las consideraremos Listas
#Y usaremos bucles para recorrer las secuencias
def main():
    print("Este algoritmo genera una secuencia que contenga los números de socios que no figuran en la secuencia de socios.")
    sec=input("Ingrese la secuencia de socios separados por coma: ").split(',') #1,4,5,8,9,12
    pos=int(sec[0])
    cont=0
    sal=[]
    while cont<len(sec): 
        v=int(sec[cont])
        while pos<v:
            sal.append(pos)
            pos+=1
        cont+=1
        pos+=1
    print("Los socios que no figuran en la secuencia original son: ",sal)
            
if __name__ == "__main__":
    main()
