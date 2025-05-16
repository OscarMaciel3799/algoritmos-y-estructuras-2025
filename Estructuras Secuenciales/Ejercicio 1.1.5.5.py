"""
-----------------------------------------------------
Ejercicio 1.1.5.5: Calcular la Sección de un condutor
-----------------------------------------------------
Enunciado:
Se desea calcular el valor de la sección (S) de un conductor, la cual se determina en función de
la corriente eléctrica I y de la conductividad C del material ( C =I/S ). Ademas, a la sección 
así obtenida se le incrementa un 25% por razones de seguridad.


RESOLUCION EN PSEUDOCODIGO

ACCION calcular_seccion ES 
    AMBIENTE 
        seguridad= 1,25
        corriente,conductividad,seccion: Real
    PROCESO
        Escribir("Este algoritmo calcula la sección de un condutor")
        Escribir("Ingrese el valor de la corriente electrica y de la conductividad")
        Leer(corriente,conductividad)
        seccion:= corriente/conductividad * seguridad
        Escribir("La sección calculada es: ",sección)
FIN_ACCION

"""

def main():
    seguridad=1.25
    print("Este programa calcula la sección de un conductor")
    corriente,conductividad=map(float,input("Ingrese el valor de la corriente electrica y de la conductividad separados por un espacio: ").split())
    seccion=corriente/conductividad*seguridad
    print("La sección calculada es: ",seccion)

if __name__ == "__main__":
    main()