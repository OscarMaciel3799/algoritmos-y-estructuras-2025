"""
Ejercicio Completo por Fila 

La empresa posee información de las ventas realizadas durante el año 2023 a sus clientes 
en una secuencia de datos, con el siguiente formato: 

FechaCompra (ddmm) | ID CLIENTE (4 caracteres)| CantidadProductosComprados (2 Caracteres) | Apellido y Nombre |#|  

Nota: Los ID CLIENTE son únicos (aparecen una sola vez por cliente, ya que corresponde a la 
última venta que se le realizó a dicho cliente) 

El detalle de cada compra se encuentra en otra secuencia (pero esta vez de enteros) con el siguiente formato:
 
ID | CATEGORIA | PRODUCTO | PRECIO 

El ID CATEGORÍA se corresponde a alguno de los siguientes valores: (1)Carniceria (2)Limpieza (3)Farmacia (4)Bazar 

Nota: Considerar además, que la segunda secuencia tendrá tantos productos como indique 
CantidadProductos comprados por cliente 

Se le solicita: 
"""
"""
FILA 1 
    a) Generar una secuencia de salida con el apellido y nombre de todos los clientes que 
    han realizado compras en un mes en particular (que ingresa el usuario), y cuyos montos superen los $50.000 

    b) Informar además, la cantidad de productos vendidos que corresponden a la Categoría de "Farmacia" 

    --- VOY A ASUMIR QUE LOS APELLIDOS Y NOMBRES NO SE PUEDEN REPETIR ---
    --- VOY A ASUMIR QUE LOS PRODUCTOS DE CATEGORIA FARMACIA ES PARA CUALQUIER MES ---  
    
RESOLUCION EN PSEUDOCODIGO

ACCION FILA_1 ES 
    AMBIENTE 
        informacion,salida: Secuencia de Caracter
        i: Caracter
        compra:Secuencia de Entero
        c: Entero
        cont,cant_productos,mes_ingresado,mes_compra, cant_farmacia: Entero
        cumple_condicion: Booleano
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(informacion);Avanzar(informacion,i)
        Arrancar(compra)
        Crear(salida)
        Escribir("Ingrese el mes que desea evaluar con el formato mm: ")
        Leer(mes_ingresado)
        cant_farmacia:=0
        Mientras NFDS(informacion) hacer
            Avanzar(informacion,i)
            Avanzar(informacion,i)
            
            mes_compra:=convertirANum(i)*10
            Avanzar(informacion,i)
            mes_compra:=mes_compra + convertirANum(i)
            Avanzar(informacion,i)
            
            Avanzar(informacion,i)
            Avanzar(informacion,i)
            Avanzar(informacion,i)
            Avanzar(informacion,i)
            
            cant_productos:=convertirANum(i)*10
            Avanzar(informacion,i)
            cant_productos:=cant_productos + convertirANum(i)
            Avanzar(informacion,i)
            
            cumple_condicion:=FALSO
            SI cant_productos>0 entonces
                Para cont:=1 hasta cant_productos hacer
                        Avanzar(compra,c)
                        SI c=3 entonces
                            cant_farmacia:=cant_farmacia + 1
                        FIN_SI
                        Avanzar(compra,c)
                        Avanzar(compra,c)
                        Avanzar(compra,c)
                        SI c>50000 Y mes_compra=mes_ingresado entonces
                            cumple_condicion:= VERDADERO
                        FIN_SI
                    FIN_PARA
            FIN_SI
            SI cumple_condicion entonces
                Mientras i <> '#' hacer
                    Escribir(salida,i)
                    Avanzar(informacion,i)
                FIN_Mientras
            SINO
                Mientras i <> '#' hacer
                    Avanzar(informacion,i)
                FIN_Mientras
            FIN_SI  
            Avanzar(informacion,i)      
        FIN_Mientras
        Cerrar(salida)
        Escribir("La cantidad de productos de la categoria farmacia vendidos es: ", cant_farmacia)
        
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
        
def Fila_1():
    print("Este algoritmo ....")
    informacion="1203C10103GomezLaura#1504C10202FernandezMarcos#0703C10303MartinezLucia#"
    compra=[1,1,11,69823,2,2,12,12369,3,4,3,1200,3,3,1,56784,5,2,5,500,6,1,6,1300,7,1,8,1100,3,4,8,72589,9,3,9,650]
    
    posI=0
    mes_ingresado=int(input("Ingrese el mes que desea evaluar con el formato mm: ")) # 03
    cant_farmacia=0
    posC=-1
    salida=None
    while posI <len(informacion):
        
        posI+=1
        posI+=1
        i=informacion[posI]            
        mes_compra=convertirANum(i)*10
        posI+=1
        i=informacion[posI]
        mes_compra+= convertirANum(i)
        posI+=1
        posI+=1
        posI+=1
        posI+=1
        posI+=1
        i=informacion[posI]        
            
        cant_productos=convertirANum(i)*10
        posI+=1
        i=informacion[posI]
        cant_productos+= convertirANum(i)
        posI+=1
        i=informacion[posI]
        cumple_condicion=False
        if cant_productos>0:
            for cont in range(0,cant_productos):
                posC+=1
                c=compra[posC]
                if c==3 :
                    cant_farmacia+= 1
                posC+=1
                posC+=1
                posC+=1
                c=compra[posC]
                if c>50000 and mes_compra==mes_ingresado:
                    cumple_condicion=True
            if cumple_condicion:
                
                while i!='#':
                    if salida==None:
                        salida=i
                    else:
                        salida+=i
                    posI+=1
                    i=informacion[posI]
            else:
                while i!='#':
                    posI+=1
                    i=informacion[posI]   
            posI+=1
    print("La secuencia de salida resultante es: ",salida)
    print("La cantidad de productos de la categoria farmacia vendidos es: ", cant_farmacia)
        

"""
FILA 2 
    a) Mostrar un listado con el siguiente formato. 
    ID CLIENTE | FECHA COMPRA | IMPORTE TOTAL 
    
    b) Indicar al final la cantidad de productos comprados por categoría 
    
RESOLUCION EN PSEUDOCODIGO

ACCION FILA_2 ES 
    AMBIENTE 
        informacion,salida: Secuencia de Caracter
        i: Caracter
        compra: Secuencia de Entero
        c: Entero
        d1,d2,m1,m2: Caracter
        importe_total: Entero
        cont,cant_prod,cant_carniceria, cant_limpieza, cant_farmacia, cant_bazar: Entero
        
        Procedimiento escribir_importe(n:Entero) es
            Ambiente
                aux: Entero
                cant,cantidad_digitos: Entero
            Proceso
                SI n = 0 ENTONCES
                    cantidad_digitos := 1
                SINO
                    aux := n
                    cantidad_digitos := 0
                    MIENTRAS aux > 0 HACER
                        aux := aux DIV 10
                        cantidad_digitos := cantidad_digitos + 1
                    FINMIENTRAS
                FINSI
                
                Para cant:=1 hasta cantidad_digitos-1 hacer
                    aux:= n DIV 10**(cantidad_digitos-cant)
                    Escribir(salida,convertirACaracter(aux))
                    n:= n MOD 10**(cantidad_digitos-cant)
                FIN_Para
                Escribir(salida,convertirACaracter(n))
        FIN_Procedimiento
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(informacion);Avanzar(informacion,i)
        Crear(salida)
        cant_carniceria:=0
        cant_limpieza:=0
        cant_farmacia:=0
        cant_bazar:=0
        
        Mientras NFDS(informacion) hacer
            d1:=i
            Avanzar(informacion,i)
            d2:=i
            Avanzar(informacion,i)
            m1:=i
            Avanzar(informacion,i)
            m2:=i
            Avanzar(informacion,i)
            
            Escribir(salida,i)
            Avanzar(informacion,i)
            Escribir(salida,i)
            Avanzar(informacion,i)
            Escribir(salida,i)
            Avanzar(informacion,i)
            Escribir(salida,i)
            Avanzar(informacion,i)
            
            cant_productos:=convertirANum(i)*10
            Avanzar(informacion,i)
            cant_productos:=cant_productos + convertirANum(i)
            Avanzar(informacion,i)
            
            SI cant_productos>0 entonces
                Avanzar(compra,c)
                importe_total:=0
                Para cont:=1 hasta cant_productos hacer
                    Segun c hacer
                        1: cant_carniceria:=cant_carniceria + 1
                        2: cant_limpieza:=cant_limpieza + 1
                        3: cant_farmacia:=cant_farmacia + 1
                        4: cant_bazar:=cant_bazar + 1
                    FIN_Segun
                    Avanzar(compra,c)
                    Avanzar(compra,c)
                    Avanzar(compra,c)
                    importe_total:=importe_total + c
                FIN_PARA
                Escribir(salida,d1)
                Escribir(salida,d2)
                Escribir(salida,m1)
                Escribir(salida,m2)
                
                escribir_importe(importe_total)
                
                
            FIN_SI
            Mientras i <> '#' hacer
                Avanzar(informacion,i)
            FIN_Mientras
            Avanzar(informacion,i)      
        FIN_Mientras
        Cerrar(salida)
        Escribir("La cantidad de productos de la categoria carniceria vendidos es: ", cant_carniceria)
        Escribir("La cantidad de productos de la categoria limpieza vendidos es: ", cant_limpieza)
        Escribir("La cantidad de productos de la categoria farmacia vendidos es: ", cant_farmacia)
        Escribir("La cantidad de productos de la categoria bazar vendidos es: ", cant_bazar)
        
FIN_ACCION    
"""

def escribir_importe(salida,n):
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

def Fila_2():
    print("Este algoritmo ....")
    informacion="1203C10103GomezLaura#1504C10202FernandezMarcos#0703C10303MartinezLucia#"
    compra=[1,1,11,69823,2,2,12,12369,3,4,3,1200,3,3,1,56784,5,2,5,500,6,1,6,1300,7,1,8,1100,3,4,8,72589,9,3,9,650]
    posI=0
    posC=-1
    salida=None
    cant_carniceria=0
    cant_limpieza=0
    cant_farmacia=0
    cant_bazar=0
        
    while posI<len(informacion)-1:
        i=informacion[posI]
        d1=i
        posI+=1
        i=informacion[posI]
        d2=i
        posI+=1
        i=informacion[posI]
        m1=i
        posI+=1
        i=informacion[posI]
        m2=i
        posI+=1
        i=informacion[posI]
        
        if salida==None:
            salida=i
        else:
            salida+=i
        posI+=1
        i=informacion[posI]
        salida+=i
        posI+=1
        i=informacion[posI]
        salida+=i
        posI+=1
        i=informacion[posI]
        salida+=i
        posI+=1
        i=informacion[posI]
        cant_productos=convertirANum(i)*10
        posI+=1
        i=informacion[posI]
        cant_productos+=convertirANum(i)
        posI+=1
        i=informacion[posI]
            
        if cant_productos>0 :
            importe_total=0
            for cont in range(0,cant_productos):
                posC+=1
                c=compra[posC]
                match c:
                    case 1: cant_carniceria += 1
                    case 2: cant_limpieza += 1
                    case 3: cant_farmacia += 1
                    case 4: cant_bazar += 1
                posC+=1
                posC+=1
                posC+=1
                c=compra[posC]
                importe_total += c
            salida+=d1
            salida+=d2
            salida+=m1
            salida+=m2
            salida=escribir_importe(salida,importe_total)
                
                
        while i !='#' :
            posI+=1
            i=informacion[posI]
        posI+=1
    print("La secuencia de salida es: ",salida)
    print("La cantidad de productos de la categoria carniceria vendidos es: ", cant_carniceria)
    print("La cantidad de productos de la categoria limpieza vendidos es: ", cant_limpieza)
    print("La cantidad de productos de la categoria farmacia vendidos es: ", cant_farmacia)
    print("La cantidad de productos de la categoria bazar vendidos es: ", cant_bazar)

"""
FILA 3 
    a) Generar dos secuencias de enteros de salidas:  
        i) Una secuencia de enteros con los id de los clientes que superan un monto dado (ingresado por el usuario). 
        
        ii) La otra con los id de los clientes que no cumplieron la condición. 
    
    b) Informar al final el ID CLIENTE que más gasto. 
    
    
RESOLUCION EN PSEUDOCODIGO

ACCION FILA_1 ES 
    AMBIENTE 
        informacion: Secuencia de Caracter
        i: Caracter
        compra: Secuencia de Entero
        c: Entero
        cont, cantidad_prod: Entero
        cumplen_condicion,no_cumplen_condicion :Secuencia de Entero
        monto_ingresado,id_cliente,gasto_cliente,mayor_gasto_id,mayor_gasto_monto: Entero
        
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(informacion);Avanzar(informacion,i)
        Arrancar(compra)
        Crear(cumplen_condicion)
        Crear(no_cumplen_condicion)
        
        Escribir("Ingrese el monto que desea evaluar: ")
        Leer(monto_ingresado)
        
        mayor_gasto_id:=0
        mayor_gasto_monto:=-1
        Mientras NFDS(informacion) hacer
            Avanzar(informacion,i)
            Avanzar(informacion,i)
            Avanzar(informacion,i)
            Avanzar(informacion,i)
            
            
            id_cliente:=convertirANum(i)*1000
            Avanzar(informacion,i)
            id_cliente:=id_cliente + convertirANum(i)*100
            Avanzar(informacion,i)
            id_cliente:=id_cliente + convertirANum(i)*10
            Avanzar(informacion,i)
            id_cliente:=id_cliente + convertirANum(i)
            Avanzar(informacion,i)
            
            cant_productos:=convertirANum(i)*10
            Avanzar(informacion,i)
            cant_productos:=cant_productos + convertirANum(i)
            Avanzar(informacion,i)
            
            SI cant_productos>0 entonces
                gasto_cliente:=0
                Para cont:=1 hasta cant_productos hacer
                        Avanzar(compra,c)
                        Avanzar(compra,c)
                        Avanzar(compra,c)
                        Avanzar(compra,c)
                        gasto_cliente:=gasto_cliente + c
                    FIN_PARA
                    SI gasto_cliente > monto_ingresado entonces
                        Escribir(cumplen_condicion,id_cliente)
                    SINO
                        Escribir(no_cumplen_condicion,id_cliente)
                    FIN_SI
                    SI gasto_cliente > mayor_gasto_monto entonces
                        mayor_gasto_id:=id_cliente
                        mayor_gasto_monto:=gasto_cliente
                    FIN_SI
            FIN_SI
            Mientras i <> '#' hacer
                Avanzar(informacion,i)
            FIN_Mientras 
            Avanzar(informacion,i)      
        FIN_Mientras
        Cerrar(cumplen_condicion)
        Cerrar(no_cumplen_condicion)
        Escribir("El id del cliente que más gasto es: ", mayor_gasto_id)
        
FIN_ACCION    
"""

def Fila_3():
    print("Este algoritmo ....")
    informacion="1203010103GomezLaura#1504010202FernandezMarcos#0703010303MartinezLucia#"
    compra=[1,1,11,69823,2,2,12,12369,3,4,3,1200,3,3,1,56784,5,2,5,500,6,1,6,1300,7,1,8,1100,3,4,8,72589,9,3,9,650]
    posI=0
    posC=-1
    cumplen_condicion=[]
    no_cumplen_condicion=[]
        
    monto_ingresado=int(input("Ingrese el monto que desea evaluar: ")) # 60000
        
    mayor_gasto_id=0
    mayor_gasto_monto=-1
    while posI < len(informacion):
        posI+=1
        posI+=1
        posI+=1
        posI+=1
        i=informacion[posI]
            
        id_cliente=convertirANum(i)*1000
        posI+=1
        i=informacion[posI]
        id_cliente+= convertirANum(i)*100
        posI+=1
        i=informacion[posI]
        id_cliente+= convertirANum(i)*10
        posI+=1
        i=informacion[posI]
        id_cliente+= convertirANum(i)
        posI+=1
        i=informacion[posI]
            
        cant_productos=convertirANum(i)*10
        posI+=1
        i=informacion[posI]
        cant_productos+= convertirANum(i)
        posI+=1
        i=informacion[posI]
            
        if cant_productos>0:
            gasto_cliente=0
            for cont in range(0,cant_productos):
                posC+=1
                posC+=1
                posC+=1
                posC+=1
                c=compra[posC]
                
                gasto_cliente+= c
            if gasto_cliente > monto_ingresado:
                cumplen_condicion.append(id_cliente)
            else:
                no_cumplen_condicion.append(id_cliente)
                    
            if gasto_cliente > mayor_gasto_monto:
                mayor_gasto_id=id_cliente
                mayor_gasto_monto=gasto_cliente
        while i!= '#':
                posI+=1
                i=informacion[posI]
        posI+=1      
    print("La secuencia de id de clientes que cumplen la condicion es: ",cumplen_condicion)
    print("La secuencia de id de clientes que NO cumplen la condicion es: ",no_cumplen_condicion)
    print("El id del cliente que más gasto es: ", mayor_gasto_id)
               
if __name__ == "__main__":
    print("RESOLUCION EJERCICIO Fila_1")
    Fila_1()
    print("--------------------------------------")
    print("                                      ")
    print("RESOLUCION EJERCICIO Fila_2")
    Fila_2()
    print("--------------------------------------")
    print("                                      ")
    print("RESOLUCION EJERCICIO Fila_3")
    Fila_3()
    