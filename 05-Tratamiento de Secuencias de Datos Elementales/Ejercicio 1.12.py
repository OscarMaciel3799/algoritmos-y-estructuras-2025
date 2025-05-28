"""
-----------------------------------------------------
Ejercicio 1.12: 
-----------------------------------------------------
Enunciado:  
Se dispone de una secuencia de caracteres.  Se desea listar las palabras que comiencen con "ALG". 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.12 ES 
    AMBIENTE 
        oracion,palabra,sal: Secuencia de Caracteres
        v,v2: Caracter
        cont,opcion: Entero
        existe_A,existe_L,existe_G,vacio: Booleano
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(oracion)
        Avanzar(oracion,v)
        vacio:=VERDADERO
        Mientras NFDS(oracion) hacer
            Mientras v=' '  hacer
                avanzar(oracion,v)
            Fin_Mientras
            cont:=1
            existe_A:=FALSO
            existe_L:=FALSO
            existe_G:=FALSO
            Crear(Palabra)
            Mientras v<>' ' y NFDS(oracion)  hacer
                Segun opcion hacer
                    1: 
                        SI v='A' entonces
                            existe_A:=VERDADERO
                        FIN_SI
                    2: 
                        SI v='L' entonces
                            existe_L:=VERDADERO
                        FIN_SI
                    3: 
                        SI v='G' entonces
                            existe_G:=VERDADERO
                        FIN_SI
                FIn_Segun
                Escribir(palabra,v)
                cont:=cont+1
                avanzar(oracion,v)
            Fin_Mientras
            
            SI existe_A y existe_L y existe_G entonces
                Arrancar(Palabra)
                SI vacio entonces
                    vacio:=FALSO
                SINO
                    Escribir(sal,'-')
                FIN_SI
                PARA aux=1 hasta cont
                    Avanzar(Palabra,v2)
                    Escribir(sal,v2)
                FIN_Para
            FIN_SI
        Fin_Mientras
        Cerrar(sal)
FIN_ACCION

"""

#A fines practicos en python las secuencias de Enteros las consideraremos Listas
#A fines practicos en python las secuencias de Caracteres las consideraremos Strings
#Y usaremos bucles para recorrer las secuencias
def main():
    print("Este algoritmo ....")
    sec=str(input("Ingrese la secuencia: "))
    # Algunas personas usan algoritmos para resolver ciertos problemas de forma más eficiente.
    sal=None
    pos=0
    v=sec[pos]
    vacio=True
    while pos<len(sec)-1:
        v=str(sec[pos])
        while  v==' ':
            pos+=1
            v=str(sec[pos])
        cont=1
        existe_A=False
        existe_L=False
        existe_G=False
        palabra=None
        while v!=' ' and  pos<len(sec)-1:
            match cont:
                case 1:
                    if v.upper()=='A':
                            existe_A=True
                case 2: 
                        if v.upper()=='L':
                            existe_L=True
                case 3: 
                        if v.upper()=='G':
                            existe_G=True
            if palabra==None:
                palabra=v
            else:
                palabra+=v
            cont+=1
            pos+=1
            v=str(sec[pos])
        if existe_A and existe_L and existe_G:
            if vacio:
                vacio=False
            else:
                print("Entra?")
                sal+=" "
            for i in range(0,cont-1):
                if sal==None:
                    sal=palabra[i]
                else:
                    sal+=palabra[i]
    print("La Secuencia resultante es: ",sal)
            
if __name__ == "__main__":
    main()