"""
1ER Parcial - julio 2024, Comisión D - Tema A

EJERCICIO № 1:
Una cadena de hoteles necesita un informe de ocupación y pagos para el mes de JUNIO. Para esto, se cuenta con dos secuencias de datos:

Secuencia de caracteres:
Estructura: Hotel (cantidad indeterminada de caracteres) & cantidad de reservas (3 caracteres) hotel &
cantidad de reservas....FDS

Ejemplo: HotelAlas&340Hotel Bahia&999... FDS

Secuencia de enteros:
Estructura: Para cada reserva. 

Nro de reserva, tipo de habitación (1: single, 2: doble, 3: suite), cantidad de noches, importe.

Ejemplo 1234 | 1 | 3 | 120.000 2345 | 3 | 2 | 65.000 | ...FDS

Nota: La función ConvertiraNumero(caracter) puede ser utilizada si se considera necesario para convertir 
un carácter a un dato entero.

Se pide escribir un algoritmo que permita:
1) Generar una secuencia de salida de enteros que contenga el número de reserva y el importe, 
    cuando el importe sea menor a 90.000.
2) Informe, para cada hotel, cuál fue la reserva (NroReserva) con mayor cantidad de noches (y la cantidad de noches).

RERESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1 ES 
    AMBIENTE 
        hoteles: Secuencia de Caracter
        h: Caracter
        reservas,salida: Secuencia de Entero
        r: Entero
        cont,cant_reservas,nro_reserva,nro_noches, mayor_noches_nro,mayor_noches_cantidad: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(hoteles);Avanzar(hoteles,h)
        Arrancar(reservas);Avanzar(reservas,r)
        Crear(salida)
        Mientras NFDS(hoteles) hacer
            Escribir("Para el hotel")
            Mientras h<> '&' hacer
                Escribir(h)
                Avanzar(hoteles,h)
            Fin_Mientras
            Avanzar(hoteles,h)
            
            cant_reservas:=ConvertiraNumero(h)*100
            Avanzar(hoteles,h)
            cant_reservas:=cant_reservas + ConvertiraNumero(h)*10
            Avanzar(hoteles,h)
            cant_reservas:=cant_reservas + ConvertiraNumero(h)
            Avanzar(hoteles,h)

            mayor_noches_nro:=0
            mayor_noches_cantidad:=-1
            Para cont:=1 hasta cant_reservas hacer
                nro_reserva:=r
                Avanzar(reservas,r)
                Avanzar(reservas,r)
                SI r> mayor_noches_cantidad entonces
                    mayor_noches_nro:=nro_reserva
                    mayor_noches_cantidad:=r
                FIN_SI
                Avanzar(reservas,r)
                SI r > 90000 entonces
                    Escribir(salida,nro_reserva)
                    Escribir(salida,r)
                FIN_SI
                Avanzar(reservas,r)
            Fin_Para
            Escribir("La mayor cantidad de noches fue: ",mayor_noches_cantidad," en la reserva: ",mayor_noches_nro)
        Fin_Mientras
        Cerrar(salida)
FIN_ACCION

"""
def convertirANum(i):
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
def Ejercicio_1():
    print("Este algoritmo ....")
    hoteles="Hotel Sol&005Hotel Aurora&003Hotel Horizonte&004#"
    reservas=[1001,1,3,45000,1002,2,5,95000,1003,3,2,120000,1004,2,1,18000,1005,1,2,30000,1006,3,4,200000,1007,1,2,28000,1008,2,3,57000,1009,1,1,15000,1010,2,2,36000,1011,3,3,180000,1012,1,2,30000,0]
    salida=[]
    posH=0
    posR=0
    
    while posH <len(hoteles)-1:
        h=hoteles[posH]
        print("Para el hotel")
        while h!= '&':
            print(h)
            posH+=1
            h=hoteles[posH]
        posH+=1
        h=hoteles[posH]
            
        cant_reservas=convertirANum(h)*100
        posH+=1
        h=hoteles[posH]
        cant_reservas+= convertirANum(h)*10
        posH+=1
        h=hoteles[posH]
        cant_reservas+= convertirANum(h)
        posH+=1
        h=hoteles[posH]

        mayor_noches_nro=0
        mayor_noches_cantidad=-1
        for cont in range (0,cant_reservas):
            r=reservas[posR]
            nro_reserva=r
            posR+=1
            posR+=1
            r=reservas[posR]
            if r> mayor_noches_cantidad:
                mayor_noches_nro=nro_reserva
                mayor_noches_cantidad=r
            posR+=1
            r=reservas[posR]
            if r > 90000:
                salida.append(nro_reserva)
                salida.append(r)
            posR+=1
        print("La mayor cantidad de noches fue: ",mayor_noches_cantidad," en la reserva: ",mayor_noches_nro)
    print("La secuencia de salida resultante es: ",salida)

if __name__ == "__main__":
    Ejercicio_1()