#input (es lo que el usuario va a responder dentro de la consola)
#int (trata de convertir a numero entero)
#float(convierte el numero a decimal)

#ejemplo.   puntos por partido
ganado = 3
empatado = 1
perdido = 0

#partidos jugados 20

nombre_del_equipo = input('ingrese el nombre del equipo: ')

partidos_ganados = int(input('ingrese el numero de partidos ganados: '))
partidos_empatados = int(input('ingrese el numero de partidos empatados: '))
partidos_perdidos = int(input('ingrese el numero de partidos perdidos: '))

promedio = (partidos_ganados * ganado + partidos_empatados * empatado + partidos_perdidos * perdido) / 20

print("el promedio del equipo", nombre_del_equipo, "es:", promedio)