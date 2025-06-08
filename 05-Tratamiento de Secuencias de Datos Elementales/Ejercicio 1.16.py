"""
-----------------------------------------------------
Ejercicio 1.16: 
-----------------------------------------------------
Enunciado:  
Se dispone de una secuencia de números de DNI asignados a un circuito electoral, 
generar otra secuencia de números que contenga los DNI múltiplos de 3. 

RESOLUCION EN PSEUDOCODIGO

ACCION ejercicio_1.16 ES 
    AMBIENTE 
        dni_asignados,dni_multiplos:Secuencia de Enteros
        a: Entero
        
    PROCESO
        Escribir("Este algoritmo ....")
        Arrancar(dni_asignados);Avanzar(dni_asignados,a)
        Crear(dni_multiplos)
        
        Mientras NFDS(dni_asignados) hacer
            SI a MOD 3=0 entonces
                Escribir(dni_multiplos,a)
            Fin_SI
            Avanzar(dni_asignados,a)
        Fin_Mientras
        Cerrar(dni_multiplos)
        
FIN_ACCION

"""
