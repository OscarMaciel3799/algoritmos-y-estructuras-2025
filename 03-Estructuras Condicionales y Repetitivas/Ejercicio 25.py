"""
-----------------------------------------------------
Ejercicio 25: Sueldo de 100 Choferes
-----------------------------------------------------
Enunciado:  
Escriba un algoritmo para resolver el siguiente problema: Una empresa de transportes desea conocer el sueldo de 
sus 100 choferes.
Estos se calculan teniendo en cuenta la categoría (1 o 2) y la asistencia (perfecta: sí o no). 
El sueldo se obtiene sumando el sueldo básico, más el 2% de  antigüedad por cada año trabajado y $200.000 de 
premio por asistencia. 
El sueldo básico es de $700.000 para choferes de categoría 1 y de $600.000 para los de categoría 2. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_25 ES 
    AMBIENTE 
        antiguedad=1,02
        i, categoria,años: Entero
        asistencia: Caracter
        sueldo_basico, sueldo_total: Real
    PROCESO
        Escribir("Este algoritmo calcula el sueldo de sus 100 choferes")
        Para i:=1 Hasta 100 Hacer
            Escribir("Chofer ", i)
            Escribir("Ingrese categoría (1 o 2): ")
            Leer(categoria)
            Escribir("Ingrese años de antigüedad: ")
            Leer(años)
            Escribir("¿Asistencia perfecta? (S/N): ")
            Leer(asistencia)

            Si categoria = 1 Entonces
                sueldo_basico:=700000
            Sino
                sueldo_basico:=600000
            Fin_Si

            sueldo_total:=sueldo_basico * antiguedad * años

            Si asistencia = 'S' Entonces
                sueldo_total:=sueldo_total + 200000
            Fin_Si

            Escribir("El sueldo del chofer ", i, " es: $", sueldo_total)
        FinPara
FIN_ACCION

"""

def main():
    antiguedad=1.02
    for i in range(1, 101):
        print(f"Chofer {i}")
        categoria = int(input("Ingrese categoría (1 o 2): "))
        años = int(input("Ingrese años de antigüedad: "))
        asistencia = input("¿Asistencia perfecta? (S/N): ").upper()

        if categoria == 1:
            sueldo_basico = 700000
        else:
            sueldo_basico = 600000

        sueldo_total = sueldo_basico* antiguedad * años

        if asistencia == "SI":
            sueldo_total += 200000

        print(f"El sueldo del chofer {i} es: ${sueldo_total:,.2f}")
            
if __name__ == "__main__":
    main()
