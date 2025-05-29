"""
Ejercicio N° 1 

Un supermercado mayorista necesita un informe de ventas, para lo cual cuenta con una secuencia 
de caracteres y una secuencia de enteros, ambas contienen información del mes de JUNIO, para 
las distintas sucursales. La estructura de dichas secuencias es la siguiente: 

Secuencia de caracteres: 
Sucursal (cantidad indeterminada de caracteres) & cantidad de tickets (3 caracteres), sucursal & 
cantidad de tickets....FDS 

Ejemplo: 
Resistencia&025Barranqueras&123…FDS 

Secuencia de enteros 
Para cada ticket: Forma de pago (1: efectivo, 2: tarjeta débito y 3: tarjeta crédito) | Nro ticket | 
cantidad de artículos | importe 

Ejemplo: 
1 | 2345 | 9 | 12500 | 3 | 2950 | 4 | 9864 |...FDS 

Si considera necesario, puede utilizar una función ConvertiraNumero(caracter), que recibe como 
parámetro un carácter y devuelve un dato entero. No es necesario desarrollar la función. 

Se solicita diseñar un algoritmo que: 

1) Genere una secuencia de salida de caracteres que contenga el nombre de la sucursal y la 
cantidad de ventas en efectivo. 
2) Informe el porcentaje de ventas en efectivo sobre el total de tickets. 

RESOLUCION EN PSEUDOCODIGO

ACCION Ejercicio_1 ES 
    AMBIENTE 
        informacion,salida: Secuencia de Caracter
        i: Caracter
        tickets: Secuencia de Entero
        t,cont,cant_tickets,cant_vent_efectivo ,total_ventas_efectivo,total_tickets: Entero
        Funcion ConvertirACaracter(pos:Entero,num:Entero): Caracter
            Ambiente
                aux: Caracter
            Proceso
                Segun pos hacer
                    1: 
                        aux:= num DIV 100
                    2:
                        aux:= num MOD 100
                        aux:= aux DIV 10
                    3:
                        aux:= num MOD 10
                Fin_Segun
                Segun aux hacer
                    '0': ConvertirACaracter:=0
                    '1': ConvertirACaracter:=1
                    '2': ConvertirACaracter:=2
                    '3': ConvertirACaracter:=3
                    '4': ConvertirACaracter:=4
                    '5': ConvertirACaracter:=5
                    '6': ConvertirACaracter:=6
                    '7': ConvertirACaracter:=7
                    '8': ConvertirACaracter:=8
                    '9': ConvertirACaracter:=9
                FIn_Segun
        Fin_Funcion
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(informacion);Avanzar(informacion,i) // Primer caracter de la secuencia  'R'
        Arrancar(tickets);Avanzar(tickets,t) // Primer Entero de la secuencia 1 
        Crear(salida)
        total_ventas_efectivo:=0
        total_tickets:=0
        Mientras NFDS(informacion) hacer
            Mientras i<>'&' hacer
                Escribir(salida,i)
                Avanzar(informacion,i)
            FIn_Mientras
            Avanzar(informacion,i)
            cant_cant_tickets:= ConvertiraNumero(i) * 100
            Avanzar(informacion,i)
            cant_tickets:=cant_tickets + ConvertiraNumero(i) * 10
            Avanzar(informacion,i)
            cant_tickets:=cant_tickets + ConvertiraNumero(i) * 1
            Avanzar(informacion,i)
            cant_vent_efectivo:=0
            Para cont:=1 hasta cant_tickets hacer
                SI t=1 entonces
                    cant_vent_efectivo:=cant_vent_efectivo+1
                FIN_SI
                Avanzar(tickets,t)
                Avanzar(tickets,t)
                Avanzar(tickets,t)
                Avanzar(tickets,t)
            Fin_Para
            total_ventas_efectivo+=total_ventas_efectivo+cant_vent_efectivo
            total_tickets:=total_tickets + cant_tickets
            Escribir(salida,ConvertirACaracter(1,cant_vent_efectivo))
            Escribir(salida,ConvertirACaracter(2,cant_vent_efectivo))
            Escribir(salida,ConvertirACaracter(3,cant_vent_efectivo))
        FIn_Mientras
        Escribir("El porcentaje de ventas en efectivos de todas las sucursales es: ", (total_ventas_efectivo*100/total_tickets)," %")
        
FIN_ACCION

"""
#A fines practicos en python las secuencias de Enteros las consideraremos Listas
#A fines practicos en python las secuencias de Caracteres las consideraremos Strings
def ConvertiraNumero(i):
    match i :
        case '0': return 0
        case '1': return 1
        case '2': return 2
        case '3': return 3
        case '4': return 4
        case '5': return 5
        case '6': return 6
        case '7': return 7
        case '8': return 8
        case '9': return 9
def ConvertiraCaracter(n,num):
    match n:
        case 1: 
            aux=num//100
        case 2:
            aux= num%100
            aux=aux//10
        case 3:
            aux= num % 10
    match aux:
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
def ejercicio_1():
    print("Este algoritmo ....")
    informacion="Resistencia&004Barranqueras&005Fontana&002"
    tickets=[1,101,3,23141,2,102,5,67981,1,103,2,10200,3,104,1,5678,1,105,5,54784,3,106,2,12334,2,107,4,23456,1,108,3,23690,2,109,9,89754,1,110,7,109121,3,111,11,213456]
    posI=0
    posT=0
    salida=None
    total_ventas_efectivo=0
    total_tickets=0
    while posI<len(informacion):
        i=informacion[posI]
        while i!='&':
            if salida==None:
                salida=i
            else:
                salida+=i
            posI+=1
            i=informacion[posI]
        posI+=1
        i=informacion[posI]
        cant_tickets= ConvertiraNumero(i) * 100
        posI+=1
        i=informacion[posI]
        cant_tickets=cant_tickets + ConvertiraNumero(i) * 10
        posI+=1
        i=informacion[posI]
        cant_tickets=cant_tickets + ConvertiraNumero(i) * 1
        posI+=1
        cant_vent_efectivo=0
        for cont in range (0,cant_tickets):
            t=int(tickets[posT])
            if t==1:
                cant_vent_efectivo+=1
            posT+=1
            posT+=1
            posT+=1
            posT+=1
        total_ventas_efectivo+=cant_vent_efectivo
        total_tickets +=cant_tickets
        salida+=ConvertiraCaracter(1,cant_vent_efectivo)
        salida+=ConvertiraCaracter(2,cant_vent_efectivo)
        salida+=ConvertiraCaracter(3,cant_vent_efectivo)
    print("La secuencia de salida es: ",salida)
    print("El porcentaje de ventas en efectivos de todas las sucursales es: ", int((total_ventas_efectivo*100/total_tickets))," %")
        

if __name__ == "__main__":
    ejercicio_1()