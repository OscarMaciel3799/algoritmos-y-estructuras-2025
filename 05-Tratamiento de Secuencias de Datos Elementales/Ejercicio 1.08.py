"""
-----------------------------------------------------
Ejercicio 1.08: 
-----------------------------------------------------
Enunciado:  
Teniendo en cuenta el ejercicio anterior, se solicita que la secuencia de salida sea una secuencia de caracteres 
y los CUIT se separen unos de otros con el caracter "-". 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.08 ES 
    AMBIENTE 
        s: Secuencia de Enteros
        sal: Secuencia de Caracteres
        v,i,Caracter: Enteros
        opciones=(0,1,2,3)
        vacio: Boolean
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(s)
        Avanzar(s,v)
        Crear(sal)
        vacio:=VERDADERO
        Mientras v<>0 hacer
            SI v MOD 10 EN opciones entonces
                SI vacio entonces
                    vacio:=FALSO
                SINO
                    Escribir(sal,'-')
                divisor:=10
                Para i:=1 hasta 11 hacer
                    num:= v DIV (10**(divisor))
                    v:= v MOD divisor
                    divisor:=divisor-1
                    Segun num hacer
                        0: Escribir(sal,'0')
                        1: Escribir(sal,'1')
                        2: Escribir(sal,'2')
                        3: Escribir(sal,'3')
                        4: Escribir(sal,'4')
                        5: Escribir(sal,'5')
                        6: Escribir(sal,'6')
                        7: Escribir(sal,'7')
                        8: Escribir(sal,'8')
                        9: Escribir(sal,'9')
                    Fin_Segun
                Fin_Para
                
            FIn_SI
            Avanzar(s,v)
        Fin_Mientras
        Cerrar(sal)
FIN_ACCION

"""

def main():
    print("Este algoritmo ....")
    sec=input("Ingrese la secuencia de cuits separados por coma: ").split(',')
    # 20345678901,27123456789,20234567890,23345678901,27234567891,27112233445,23234567890,20398765432,0
    opciones={0,1,2,3}
    sal=None
    pos=0
    v=int(sec[pos])
    vacio=True
    while v!=0:
        print("Entramos al while, el valor de v es: ",v)
        if v%10 in opciones:
            if vacio:
                vacio=False
            else:
                sal+='-'
            divisor=10
            for i in range(1,12):
                print("Entramos al for, el divisor es: ",divisor)
                num=int(v/(10**divisor))
                print("el numero es: ",num)
                v=int(v % (10**divisor))
                print("El nuevo valor de v es: ",v)
                divisor-=1
                print("el divisor es: ",divisor)
                if sal==None:
                    sal=str(transf_caracter(num))
                else:
                    sal+=str(transf_caracter(num))
                print("El valor de sal, durante el for es: ",sal)
        pos+=1
        v=int(sec[pos])
    print("Los cuits que terminan en 0, 1, 2 o 3 son: ",sal)                

def transf_caracter(n):
    n=int(n)
    match n:
        case 0: return '0'
        case 1: return '1'
        case 2: return '2'
        case 3: return '3'
        case 4: return '4'
        case 5: return '5'
        case 6: return '6'
        case 7: return '7'
        case 8: return '8'
        case 9: return '9'
    

if __name__ == "__main__":
    main()
