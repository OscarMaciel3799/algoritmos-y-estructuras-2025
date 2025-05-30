"""

Ejercicio 1 

Dada un secuencia de caracteres con la información de los alumnos que se encuentran 
cursando la materia de Algoritmos y Estructura de datos , con la siguiente estructura: 
LEGAJO (4 caracteres) Edad (2 caracteres) Apellido Y Nombre (#) 

a) Generar una secuencia de salida con los Apellidos y Nombre de todos los alumnos 
cuya edad sea mayor a un valor que ingrese un usuario. Separar cada apellido con un 
caracter "&" 
b) Al final, determinar el promedio de edad de los alumnos que cursan Algoritmos. 


RESOLUCION EN PSEUDOCODIGO

ACCION Ejercicio_1 ES 
    AMBIENTE 
        informacion,salida: Secuencia de Caracter
        i: Caracter
        cont,total_alumnos,total_edad, edad_ingresada,edad_alumno: Entero
        vacio:Boolean
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(informacion);Avanzar(informacion,i)
        Crear(salida)
        Escribir("Ingrese la edad con la que desea trabajar: ")
        Leer(edad_ingresada)
        vacio:=VERDADERO
        total_alumnos:=0
        total_edad:=0
        Mientras NFDS(informacion) hacer
            Para cont:=0 hasta 4 hacer
                Avanzar(informacion,i)
            Fin_Para
            
            edad_alumno:=convertirANum(i)*10
            Avanzar(informacion,i)
            edad_alumno:=edad_alumno + convertirANum(i)
            Avanzar(informacion,i)
            
            SI edad_alumno > edad_ingresada entonces
                SI vacio entonces
                    vacio:=FALSO
                SINO
                    Escribir(salida,'&')
                FIN_SI
                Mientras i<>'#' hacer
                    Escribir(salida,i)
                    Avanzar(informacion,i)
                FIn_Mientras
            SINO
                Mientras i<>'#' hacer
                    Avanzar(informacion,i)
                FIn_Mientras
            Fin_SI
            avanzar(informacion,i)
            total_edad:=total_edad+edad_alumno
            total_alumnos:=total_alumnos+1
        FIN_Mientras
        Escribir("El promedio de edad de los alumnos es: ", (total_edad/total_alumnos)," años.")
        Cerrar(salida)
        
FIN_ACCION
"""

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
#A fines practicos en python las secuencias de Caracteres las consideraremos Strings
def Ejercicio_1():
    print("Este algoritmo ....")
    informacion="A12320GonzalezJuan#B45619MartinezLaura#C78922RamirezPedro#D32118LopezAna#E65421FernandezLucia#F98723DiazMarcos#"
    edad_ingresada=int(input("Ingrese la edad con la que desea trabajar: "))
    vacio=True
    total_alumnos=0
    total_edad=0
    posI=0
    salida=None
    while posI<len(informacion):
        for cont in range(0,4):
                posI+=1
        i=informacion[posI]
        edad_alumno=convertirANum(i)*10
        posI+=1
        i=informacion[posI]
        edad_alumno+= convertirANum(i)
        posI+=1
        
        if edad_alumno > edad_ingresada:
            i=informacion[posI]
            if vacio:
                vacio=False
            else:
                salida+='&'
                
            while i!='#' :
                if salida==None:
                   salida=i
                else:
                    salida+=i
                posI+=1
                i=informacion[posI]
        else:
            while i!='#' :
                posI+=1
                i=informacion[posI]
        posI+=1        
        total_edad+=edad_alumno
        total_alumnos=total_alumnos+1
    print("La secuencia de salida es: ",salida)
    print("El promedio de edad de los alumnos es: ", (total_edad/total_alumnos)," años.")
    


"""
Ejercicio 2 
Dada un secuencia de caracteres con la información de los alumnos que se encuentran 
cursando la materia de Algoritmos y Estructura de datos , con la siguiente estructura:
LEGAJO (4 caracteres) Edad (2 caracteres) Apellido Y Nombre (#) 

a) Generar una secuencia de salida con los Apellido y Nombre de de todos los alumnos 
cuya edad sea mayor a un valor que ingrese un usuario. Separar cada apellido con un 
caracter "#" 
b) Al final, determinar el porcentaje de alumnos que cumplen la condición. 

RESOLUCION EN PSEUDOCODIGO

ACCION Ejercicio_1 ES 
    AMBIENTE 
        informacion,salida: Secuencia de Caracter
        i: Caracter
        cont,total_alumnos,cumplen_condicion, edad_ingresada,edad_alumno: Entero
        vacio:Boolean
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(informacion);Avanzar(informacion,i)
        Crear(salida)
        Escribir("Ingrese la edad con la que desea trabajar: ")
        Leer(edad_ingresada)
        vacio:=VERDADERO
        total_alumnos:=0
        cumplen_condicion:=0
        Mientras NFDS(informacion) hacer
            Para cont:=0 hasta 4 hacer
                Avanzar(informacion,i)
            Fin_Para
            
            edad_alumno:=convertirANum(i)*10
            Avanzar(informacion,i)
            edad_alumno:=edad_alumno + convertirANum(i)
            Avanzar(informacion,i)
            
            SI edad_alumno > edad_ingresada entonces
                SI vacio entonces
                    vacio:=FALSO
                SINO
                    Escribir(salida,'#')
                FIN_SI
                Mientras i <> '#'
                    Escribir(salida,i)
                    Avanzar(informacion,i)
                Fin_Mientras
                cumple_condicion:=cumple_condicion+1
            SINO
                Mientras i <> '#'
                    Escribir(salida,i)
                    Avanzar(informacion,i)
                Fin_Mientras
            FIN_SI
            Avanzar(informacion,i)
            total_alumnos:=total_alumnos+1
        FIN_Mientras
        Escribir("El porcentaje de alumnos que cumple la condicion es: ", (cumple_condicion*100/total_alumnos)," %.")
        Cerrar(salida)
        
FIN_ACCION
"""
#A fines practicos en python las secuencias de Caracteres las consideraremos Strings
def Ejercicio_2():
    print("Este algoritmo ....")
    informacion="A12320GonzalezJuan#B45619MartinezLaura#C78922RamirezPedro#D32118LopezAna#E65421FernandezLucia#F98723DiazMarcos#"
    edad_ingresada=int(input("Ingrese la edad con la que desea trabajar: "))
    vacio=True
    total_alumnos=0
    cumplen_condicion=0
    posI=0
    salida=None
    while posI<len(informacion):
        for cont in range(0,4):
                posI+=1
        i=informacion[posI]
        
        edad_alumno=convertirANum(i)*10
        posI+=1
        i=informacion[posI]
        edad_alumno+= convertirANum(i)
        posI+=1
        
        if edad_alumno > edad_ingresada:
            i=informacion[posI]
            if vacio:
                vacio=False
            else:
                salida+='#'
                
            while i!='#' :
                if salida==None:
                   salida=i
                else:
                    salida+=i
                posI+=1
                i=informacion[posI]
            cumplen_condicion+=1
        else:
            while i!='#' :
                posI+=1
                i=informacion[posI]
        posI+=1        
        total_alumnos=total_alumnos+1
    print("La secuencia de salida es: ",salida)
    print("El porcentaje de alumnos que cumplen la condicion es: ", round((cumplen_condicion*100/total_alumnos),2)," %.")



"""
Ejercicio 3 
Dada un secuencia de caracteres con la información de los alumnos que se encuentran 
cursando la materia de Algoritmos y Estructura de datos , con la siguiente estructura: 

COMISION (1caracter) CantidadDeAlumnos(2 caracter) [LEGAJO (4 caracteres) Apellido Y Nombre (#) … ] 

Nota: La cantidad de alumnos que figuran en [] es la que se indica en CantidadDeAlumnos, 
el “[“ y ”]” no se incluyen 
a) Generar una secuencia de salida con el nombre y apellido de todos los alumnos cuyo legajo sea PAR. 
b) Indicar por comisión, la cantidad de alumnos que cumplen la condición anterior. 

RESOLUCION EN PSEUDOCODIGO

ACCION Ejercicio_3 ES 
    AMBIENTE 
        informacion,salida: Secuencia de Caracter
        i: Caracter
        cont,cumplen_condicion,cant_alumnos,legajo: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(informacion);Avanzar(informacion,i)
        Crear(salida)
        
        Mientras NFDS(informacion) hacer
            Escribir("Para la comision: ",i)
            cumplen_condicion:=0
            
            Avanzar(informacion,i)
            cant_alumnos:=convertirANum(i)*10
            Avanzar(informacion,i)
            cant_alumnos:=cant_alumnos + convertirANum(i)
            Avanzar(informacion,i)
            
            Para cont:=0 hasta cant_alumnos hacer
                legajo:=convertirANum(i)*1000
                Avanzar(informacion,i)
                legajo:=legajo + convertirANum(i)*100
                Avanzar(informacion,i)
                legajo:=legajo + convertirANum(i)*10
                Avanzar(informacion,i)
                legajo:=legajo + convertirANum(i)*1
                Avanzar(informacion,i)
                
                SI legajo MOD 2=0 entonces
                    Mientras i<> '#'
                        Escribir(salida,i)
                        cumplen_condicion:=cumplen_condicion+1
                        Avanzar(informacion,i)
                    FIN_Mientras
                SINO
                    Mientras i<> '#'
                        Avanzar(informacion,i)
                    FIN_Mientras
                FIN_SI
            Fin_Para
            Avanzar(informacion,i)
            Escribir("La cantidad de alumnos que cumplen la condicion es: ",cumplen_condicion)
        FIN_Mientras
        Cerrar(salida)
        
FIN_ACCION
"""


#A fines practicos en python las secuencias de Caracteres las consideraremos Strings
def Ejercicio_3():
    print("Este algoritmo ....")
    informacion="A030124GomezMaria#0456LopezJuan#0789MartinezSofia#B021321FernandezLucia#1653DiazMarcos#C042987RamirezPedro#2321CastroAna#2654MendezPablo#2987TorresLucia#"
    posI=0
    salida=None
    while posI<len(informacion):
        i=informacion[posI]
        print("Para la comision: ",i)
        cumplen_condicion=0
        
        posI+=1
        i=informacion[posI]
        cant_alumnos=convertirANum(i)*10
        posI+=1
        i=informacion[posI]
        cant_alumnos+=convertirANum(i)
        
        for cont in range (0,cant_alumnos):
            posI+=1
            i=informacion[posI]
            legajo=convertirANum(i)*1000
            posI+=1
            i=informacion[posI]
            legajo+=convertirANum(i)*100
            posI+=1
            i=informacion[posI]
            legajo+=convertirANum(i)*10
            posI+=1
            i=informacion[posI]
            legajo+=convertirANum(i)
            posI+=1
            i=informacion[posI]
            
            if legajo%2==0:
                while i!='#':
                    if salida==None:
                        salida=i
                    else:
                        salida+=i
                    posI+=1
                    i=informacion[posI]
                cumplen_condicion+=1
            else:
                while i!='#':
                    posI+=1
                    i=informacion[posI]
        posI+=1
        print("La cantidad de alumnos que cumplen la condicion es: ",cumplen_condicion)
    print("La secuencia de salida es: ",salida)


"""
EJERCICIO EXTRA: 2.1.15 
Se desea saber la cantidad promedio de palabras que contienen las oraciones de una secuencia de caracteres. 
Supóngase que los puntos son siempre contiguos al último caracter de la palabra. 
La secuencia finaliza con una marca.

RESOLUCION EN PSEUDOCODIGO

ACCION Ejercicio_2.1.15 ES 
    AMBIENTE 
        oraciones: Secuencia de Caracter
        o: Caracter
        cant_palabras,cant_oraciones: Entero
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(oraciones);Avanzar(oraciones,o)
        cant_palabras:=0
        cant_oraciones:=0
        Mientras NFDS(informacion) hacer
            Mientras o<>'.' hacer
                Mientras o =' ' hacer
                    Avanzar(oraciones,o)
                FIN_Mientras
                cant_palabras:=cant_palabras+1
                Mientras o <> '.' Y o <> ' ' hacer
                    Avanzar(oraciones,o)
                FIN_Mientras
            Fin_Mientras
            cant_oraciones:=cant_oraciones+1
            Avanzar(oraciones,o)
        FIN_Mientras
        Cerrar(salida)
        Escribir("La cantidad promedio de palabra en cada oracion es: ", (cant_palabras/cant_oraciones))
        
FIN_ACCION

"""

#A fines practicos en python las secuencias de Caracteres las consideraremos Strings
def Ejercicio_Ejercicio_2_1_15():
    print("Este algoritmo ....")
    oraciones="Se desea saber la cantidad promedio de palabras que contienen las oraciones de una secuencia de caracteres.Supóngase que los puntos son siempre contiguos al último caracter de la palabra.La secuencia finaliza con una marca.#"
    posO=0
    cant_palabras=0
    cant_oraciones=0
    while posO<len(oraciones)-1:
        o=oraciones[posO]
        while o!='.':
            while o==' ':
                posO+=1
                o=oraciones[posO]
            cant_palabras+=1
            while o!= '.' and o !=' ':
                posO+=1
                o=oraciones[posO]
        cant_oraciones+=1
        posO+=1
    print("La cantidad promedio de palabra en cada oracion es: ", (cant_palabras/cant_oraciones))

if __name__ == "__main__":
    
    print("RESOLUCION EJERCICIO 1")
    Ejercicio_1()
    print("--------------------------------------")
    print("                                      ")
    print("RESOLUCION EJERCICIO 2")
    Ejercicio_2()
    print("--------------------------------------")
    print("                                      ")
    print("RESOLUCION EJERCICIO 3")
    Ejercicio_3()
    print("--------------------------------------")
    print("                                      ")
    print("RESOLUCION EJERCICIO 2_1_15")
    Ejercicio_Ejercicio_2_1_15()
