"""
-----------------------------------------------------
Ejercicio 26: Calcular el peso de varias piezas de tela
-----------------------------------------------------
Enunciado:  
Una fábrica textil produce telas de dos calidades distintas (primera y segunda) y de dos materiales distintos (seda 
y algodón).
Generar un algoritmo que calcule el peso de varias piezas de tela, el cual está dado por la suma del peso 
neto más un porcentaje por el apresto, más el peso del núcleo de cartón. 
Para realizar el cálculo, tener en cuenta la siguiente información, para cada pieza:
- El peso del m2 y la longitud de cada pieza. 
- Al peso neto de la tela hay que sumarle un porcentaje por cada pieza, debido al apresto, el cual es del 2% para 
las telas de seda y del 7% para las de algodón. 
- También se debe considerar el núcleo de cartón, que es de 400 gr. para los rollos de telas de primera y de 300 
gr. en los de segunda. 
Finalizar cuando la variable FIN sea igual a  'SI'. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_26 ES 
    AMBIENTE 
        apresto_seda=1,02
        apresto_algodon=1,02
        peso_m2,largo,peso_neto,peso_apresto,peso_total: Real
        material,calidad,FIN: Caracter
    PROCESO
        Escribir("Este algoritmo Calcular el peso de varias piezas de telas")
        Escribir("Desea ingresar los datos de la primer tela? (S/N): ")
        Leer(FIN)
        Mientras FIN ='S' Hacer
            Escribir("Ingrese material S para SEDA o A para ALGODON: ")
            Leer(material)
            Escribir("Ingrese calidad 1 para PRIMERA o 2 para SEGUNDA: ")
            Leer(calidad)
            Escribir("Ingrese peso por m2: ")
            Leer(peso_m2)
            Escribir("Ingrese largo de la pieza en m2: ")
            Leer(largo)

            peso_neto:=peso_m2 * largo

            Si material = 'S' Entonces
                peso_total:=peso_neto * apresto_seda
            Sino
                peso_total_=peso_neto * apresto_algodon
            FinSi

            Si calidad = '1' Entonces
                peso_total:=peso_total + 400
            Sino
                peso_total:=peso_total + 300
            FinSi

            Escribir("El peso total de la pieza es: ", peso_total, " gramos")

            Escribir("¿Finalizar? (S/N): ")
            Leer(FIN)
        FinMientras
FIN_ACCION

"""

def main():
    apresto_seda=1.02
    apresto_algodon=1.07
    print("Este algoritmo Calcular el peso de varias piezas de telas")
    FIN=str(input("Desea ingresar los datos de la primer tela? (S/N): "))
    while FIN.upper() == "S":
        material = input("Ingrese material (SEDA o ALGODON): ").upper()
        calidad = input("Ingrese calidad (PRIMERA o SEGUNDA): ").upper()
        peso_m2 = float(input("Ingrese peso por m2: "))
        largo = float(input("Ingrese largo de la pieza en m2: "))

        peso_neto = peso_m2 * largo

        if material == "SEDA":
            peso_total = peso_neto * apresto_seda
        else:
            peso_total = peso_neto * apresto_algodon

        if calidad == "PRIMERA":
            peso_total = peso_total + 400
        else:
            peso_total = peso_total + 300

        print(f"El peso total de la pieza es: {peso_total:.2f} gramos")

        FIN = str(input("¿Finalizar? (S/N): "))
            
if __name__ == "__main__":
    main()
