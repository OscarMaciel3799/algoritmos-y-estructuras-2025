"""
1ER Parcial - julio 2024, Comisión D - Tema B

EJERCICIO № 1:
Una cadena de hoteles necesita un informe de ocupación y pagos para el mes de JUNIO. 
Para esto, se cuenta con dos secuencias de datos:

Secuencia de caracteres:
Estructura: 

Hotel (cantidad indeterminada de caracteres) & cantidad de reservas (3 caracteres) hotel & cantidad de reservas....FDS

Ejemplo: HotelAlas&340Hotel Bahia&999... FDS

Secuencia de enteros:
Estructura para cada reserva:

Nro de reserva, tipo de habitación (1: single, 2: doble, 3: suite), cantidad de noches, importe.

Ejemplo 1234 | 1 | 3 | 120.000 2345 | 3 | 2 | 65.000 | ...FDS

Nota: La función ConvertiraNumero(caracter) puede ser utilizada si se considera necesario para convertir un carácter a un dato entero.

Se pide escribir un algoritmo que permita:
1) Generar una secuencia de salida de caracteres que contenga el 
    nombre de cada hotel y su cantidad de reservas de habitaciones dobles.
2) Promedio de reservas de habitaciones dobles por hotel


RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1 ES 
    AMBIENTE 
        hoteles,salida: Secuencia de Caracter
        h: Caracter
        reservas: Secuencia de Entero
        r: Entero
        cont,cant_reservas,cant_hab2,total_hab2, total_hoteles: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(hoteles);Avanzar(hoteles,h)
        Arrancar(reservas);Avanzar(reservas,r)
        Crear(salida)
        total_hoteles:=0
        total_hab2:=0
        
        Mientras NFDS(hoteles) hacer
            Mientras h<> '&' hacer
                Escribir(salida,h)
                Avanzar(hoteles,h)
            Fin_Mientras
            Avanzar(hoteles,h)
            
            cant_reservas:=ConvertiraNumero(h)*100
            Avanzar(hoteles,h)
            cant_reservas:=cant_reservas + ConvertiraNumero(h)*10
            Avanzar(hoteles,h)
            cant_reservas:=cant_reservas + ConvertiraNumero(h)
            Avanzar(hoteles,h)

            cant_hab2:=0
            total_hoteles:=total_hoteles + 1
            Para cont:=1 hasta cant_reservas hacer
                Avanzar(reservas,r)
                SI r = 2 entonces
                    cant_hab2:=cant_hab2 + 1
                FIN_SI
                Avanzar(reservas,r)
                Avanzar(reservas,r)
                Avanzar(reservas,r)
            Fin_Para
            Escribir(salida,cant_hab2)
            total_hab2:=total_hab2 + cant_hab2
        Fin_Mientras
        Escribir("El promedio de reserva de habitaciones dobles fue de: ",total_hab2/total_hoteles)
        Cerrar(salida)
FIN_ACCION
"""

#A fines practicos en python las secuencias de Enteros las consideraremos Listas
#A fines practicos en python las secuencias de Caracteres las consideraremos Strings

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

def convertirACaracter(i):
    match i:
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

def escribir_cantidad_hab2(salida,n):
    if n ==0: 
        cantidad_digitos= 1
    else:
        aux = n
        cantidad_digitos= 0
        while aux > 0 :
            aux = aux // 10
            cantidad_digitos += 1
        for cant in range(1,cantidad_digitos):
            aux= n // 10**(cantidad_digitos-cant)
            salida+=convertirACaracter(aux)
            n= n % (10**(cantidad_digitos-cant))
        salida+=convertirACaracter(n)
        return salida
def Ejercicio_1():
    print("Este algoritmo ....")
    hoteles="Hotel Sol&005Hotel Aurora&003Hotel Horizonte&004#"
    reservas=[1001,1,3,45000,1002,2,5,95000,1003,3,2,120000,1004,2,1,18000,1005,1,2,30000,1006,3,4,200000,1007,1,2,28000,1008,2,3,57000,1009,1,1,15000,1010,2,2,36000,1011,3,3,180000,1012,1,2,30000,0]
    salida=None
    posH=0
    posR=0
    
    total_hoteles=0
    total_hab2=0
    while posH<len(hoteles)-1:
        h=hoteles[posH]
        while h!='&':
            if salida==None:
                salida=h
            else:
                salida+=h
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

        cant_hab2=0
        total_hoteles+= 1
        for cont in range(0,cant_reservas):
            posR+=1
            r=reservas[posR]
            if r == 2:
                cant_hab2+=1
            posR+=1
            posR+=1
            posR+=1
        total_hab2+= cant_hab2
        salida=escribir_cantidad_hab2(salida,cant_hab2)
    print("El promedio de reserva de habitaciones dobles fue de: ",total_hab2/total_hoteles)
    print("La secuencia de salida resultante es: ",salida)

if __name__ == "__main__":
    Ejercicio_1()