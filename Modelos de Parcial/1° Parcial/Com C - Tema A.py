"""
Ejercicio N° 1 

Un supermercado mayorista necesita un informe de ventas, para lo cual cuenta con 
una secuencia de caracteres y una secuencia de enteros, 
ambas contienen información del mes de JUNIO, para las distintas sucursales. 
La estructura de dichas secuencias es la siguiente:

Secuencia de caracteres:
Sucursal(cantidad indeterminada de caracteres)&cantidad de tickets(3 caracteres),sucursal&cantidad de tickets....FDS
Ejemplo:
Resistencia&025Barranqueras&123…FDS

Secuencia de enteros
Para cada ticket: Forma de pago (1: efectivo, 2: tarjeta débito y 3: tarjeta crédito) | Nro ticket | cantidad de artículos | importe
Ejemplo:
1 | 2345 | 9 | 12500 | 3 | 2950 | 4 | 9864 |...FDS

Si considera necesario, puede utilizar una función ConvertiraNumero(caracter), 
que recibe como parámetro un carácter y devuelve un dato entero. No es necesario desarrollar la función.

Se solicita diseñar un algoritmo que:
Genere una secuencia de salida de enteros que contenga el número de ticket y el importe, cuando el importe sea mayor a 50.000.
Informe, para cada sucursal, cuál fue el ticket de mayor importe (y el importe).

RESOLUCION EN PSEUDOCODIGO

ACCION Ejercicio_1 ES 
    AMBIENTE 
        informacion: Secuencia de Caracter
        i: Caracter
        tickets,salida: Secuencia de Entero
        t,cont,cant_tickets ,num_ticket,ticket_mayor,importe_mayor: Entero
        
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(informacion);Avanzar(informacion,i) // Primer caracter de la secuencia  'R'
        Arrancar(tickets);Avanzar(tickets,t) // Primer Entero de la secuencia 1 
        Crear(salida)
        
        Mientras NFDS(informacion) hacer
            Mientras i<>'&' hacer
                Escribir(i)
                Avanzar(informacion,i)
            Fin_Mientras // '&'
            Avanzar(informacion,i) // primer caracter del número de ticket
            cant_tickets:= ConvertiraNumero(i) * 100
            Avanzar(informacion,i) // segundo caracter del número de ticket
            cant_tickets:=cant_tickets + ConvertiraNumero(i) * 10
            Avanzar(informacion,i) // tercer caracter del número de ticket
            cant_tickets:=cant_tickets + ConvertiraNumero(i) * 1
            Avanzar(informacion,i) // Primer caracter del nombre de la sig sucursal
            importe_mayor:=0
            ticket_mayor:=1
            Para cont:=1 hasta cant_tickets hacer
                Avanzar(tickets,t) // Segundo entero de la secuencia (Numero de ticket)
                num_ticket:=t
                Avanzar(tickets,t) // Tercer entero de la secuencia (Cantidad de Articulos)
                Avanzar(tickets,t) // Cuarto entero de la secuencia (Importe)
                SI t > 50000 entonces
                    Escribir(salida,num_ticket)
                    Escribir(salida,t)
                FIn SI
                SI t > importe_mayor entonces
                    importe_mayor:=t
                    ticket_mayor:=num_ticket
                Fin_SI
                Avanzar(tickets,t) // Primer Entero del sig ticket
            Fin_Para
            
        Fin_Mientras
        Cerrar(salida)
        
        
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
def ejercicio_1():
    print("Este algoritmo ....")
    informacion="Resistencia&004Barranqueras&005Fontana&002"
    tickets=[1,101,3,23141,2,102,5,67981,3,103,2,10200,4,104,1,5678,5,105,5,54784,6,106,2,12334,7,107,4,23456,8,108,3,23690,9,109,9,89754,10,110,7,109121,11,111,11,213456]
    posI=0
    posT=0
    salida=[]
    while posI<len(informacion):
        i=informacion[posI]
        while i!='&':
            print(i)
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

        importe_mayor=0
        ticket_mayor=0
        for cont in range(0,cant_tickets):
            posT+=1
            t=tickets[posT]
            num_ticket=t
            posT+=1
            t=tickets[posT]
            posT+=1
            t=tickets[posT]
            if t > 50000:
                salida.append(num_ticket)
                salida.append(t)
                
            if t > importe_mayor:
                    importe_mayor=t
                    ticket_mayor=num_ticket
            posT+=1
        print("El importe mayor de esta sucursal es: ",importe_mayor)
        print("Y su número de tickets es: ",ticket_mayor)
    print("La secuencia de salida es: ",salida)
if __name__ == "__main__":
    ejercicio_1()

"""
Ejercicio N° 2

Un supermercado mayorista que cuenta con un sistema de atención en cajas necesita un informe de ventas, para lo cual 
cuenta con el archivo secuencial VENTAS que contiene información de todos los tickets emitidos durante el mes de JUNIO.
Para cada venta se registra: 
VENTAS, Ordenado por Nro de Caja, Forma de pago, Nro de ticket 

|--------|---------------|--------|----------|-------------|-------------|
| Nro de | Forma de Pago | Nro de | Fecha de | Cantidad de | Importe de  |
|  Caja  | (EF, TD y TC) | ticket |  Venta   |  Articulos  | la Venta    |
|--------|---------------|--------|----------|-------------|-------------|

Nota: EF: efectivo, TD: tarjeta débito y TC: tarjeta crédito. 
Se pide escribir un algoritmo que permita: 

1) Imprimir un informe del total de artículos vendidos por caja y por forma de pago. 
2) Crear un fichero de salida que contenga Nro de caja, total artículos que se pagaron en efectivo 
y total artículos que se pagaron con tarjetas (TD o TC). (1 registro por caja) 
    |--------|-----------------|------------------|
    | Nro de | Total Articulos | Total articulos  |
    |  Caja  |    Efectivo     |     Tarjetas     |
    |--------|-----------------|------------------|

3) Informar cuáles son las cajas que tuvieron mayor cantidad de artículos vendidos en efectivo 
que con tarjetas. 
"""