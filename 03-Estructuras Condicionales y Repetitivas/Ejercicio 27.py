"""
-----------------------------------------------------
Ejercicio 27: Domingo de Pascua
-----------------------------------------------------
Enunciado:  
La fecha del domingo de Pascua corresponde al primer domingo después de la primera luna llena que sigue al 
equinoccio de primavera. La secuencia de cálculos que permite conocer esta fecha es: 
 
A = año mod 19 
B = año mod 4 
C = año mod 7 
D = (19*A + 24 ) mod 30  
E = (2*B + 4*C + 6*D + 5) mod 7 
N = (22+ D + E) 
 
Donde N indica el número del día del mes de marzo (o abril si N es superior a 31) correspondiente al domingo de 
Pascua. Realizar un algoritmo que determine esta fecha para los años comprendidos entre 1990 y 2010. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_27 ES 
    AMBIENTE 
        a,b,c,d,e,año,n: Entero
    PROCESO
        Escribir("Este algoritmo determina la fecha del domingo de Pascua corresponde para los años comprendidos entre 1990 y 2010")
        Para año:=1990 hasta 2010 hacer
            a:= año mod 19
            b:= año mod 4
            c:= año mod 7
            d:=(19*a +24) mode 30
            e:= (2*b + 4*c + 6*d +5) mod 7
            n:=(22 + d + e)
            SI n>31 entonces
                Escribir("El domingo de Pascua del año ",año," será el dia: ",(n-31),"de Abril.")
            SINO
                Escribir("El domingo de Pascua del año ",año," será el dia: ",(n),"de Marzo.")
        Fin_Para
FIN_ACCION

"""

def main():
    print("Este algoritmo determina la fecha del domingo de Pascua corresponde para los años comprendidos entre 1990 y 2010")
    for año in range(1990,2011):
            a= año%19
            b= año% 4
            c= año% 7
            d=(19*a +24) % 30
            e= (2*b + 4*c + 6*d +5) % 7
            n=int((22 + d + e))
            if n>31 :
                print("El domingo de Pascua del año ",año," será el dia: ",(n-31),"de Abril.")
            else:
                print("El domingo de Pascua del año ",año," será el dia: ",(n),"de Marzo.")
        
            
if __name__ == "__main__":
    main()
