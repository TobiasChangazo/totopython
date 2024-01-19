# MICRODESAFÍO SEMANA 1

cadena_1  = "versátil"
cadena_2  = "Python"
cadena_3  = "es un lenguaje"
cadena_4  = "de programación"

cadena_5 = "\n"

cadena_total = cadena_2 + cadena_5 + cadena_3 + cadena_5 + cadena_4 + cadena_5 + cadena_1

print(cadena_total)


cadena_6 = "Python es un lenguaje \n  \t de programación versátil"


print(cadena_6)


# Ejemplo en vivo: Torneo de Futbol

partidos_totales = 15

#puntos por partido:
ganado = 5
empate = 2
perdido = 1

nombre_del_equipo = input('Ingrese el nombre del equipo: ')

partidos_ganados = int(input('Ingrese el número de partidos ganados: '))
partidos_empatados = int(input('Ingrese el número de partidos empatados: '))
partidos_perdidos = int(input('Ingrese el número de partidos perdidos: '))

promedio = (partidos_ganados * ganado + partidos_empatados * empate + partidos_perdidos * perdido) / partidos_totales

print("El promedio del equipo", nombre_del_equipo, "es:", promedio)

