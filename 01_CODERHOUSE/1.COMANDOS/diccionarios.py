#los diccionarios van entre {}  Difine la clave y el valor

campeones = {2014: 'ARGENTINA', 2018: 'FRANCIA', 2022: 'ARGENTINA' }

#Definir nuevo valor a una clave

campeones[2014]='ALEMANIA'

#agregar a mi diccionario mas un valor

campeones.update({2026: 'ARGENTINA', 2030: 'ARGENTINA'})

#saber la cantidad de elementos del diccionario

len(campeones)

#elimina un elemento del diccionario

del campeones[2030]

#verificar si existe la clave en el diccionario

2022 in campeones

#borrar un diccionario

campeones.clear()

#nos sirve para traer todas las claves del diccionario

campeones.keys()

#va a intentar buscar la clave dentro del diccionarios y si no la encuentra y no le especificamos que diga nada no tira error

campeones.get(2034, 'no encontre al campeon')

#nos sirve para traer todas los valores del diccionario

campeones.values()

#nos va a dar una lista de tuplas con cada clave y valor

campeones.items()

#pasar dos listas a un diccionario

lista1 = [1, 2, 3, 4, 5]

lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]

diccionario = dict(zip(lista2, lista1))
    