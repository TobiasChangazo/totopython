# Repaso clase anterior
# Ejemplo tuplas:

usuario_1 = (47860983, 'Lucas Rodriguez')
usuario_2 = (31358367, 'Martin Fernandez')
usuario_3 = (50242837, 'Marina Fletcher')

lista_usuarios = [usuario_1, usuario_2, usuario_3]

print(lista_usuarios)

# Sets (Conjuntos)

mi_set = set(['Ivan', 'Maria', 'Andres', 'Maria', 'maria'])

print(mi_set)

list(mi_set)

print(mi_set)

mi_otro_set = {'Carlos', 'Tali', 'Nicolas', 'Maria'}

otro_otro_set = mi_set.difference(mi_otro_set)

print(otro_otro_set)

mi_set.intersection(mi_otro_set)

('Maria', "Tali" in mi_otro_set)

# Diccionarios

diccionario = {'uno': 1, 'dos': 2, 'tres': 3}

diccionario['dos'], diccionario['uno']

print(diccionario)

diccionario['lista'] = [45, 56, 7]

print(diccionario)

diccionario['lista'][2] = 100

print(diccionario)

diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
diccionario.update({'cuatro': 4, 'cinco': 5})

print(diccionario)


dicc_campeones = {
    1990: 'Alemania',
    1994: 'Brasil',
    1998: 'Francia',
    2002: 'Brasil',
    2006: 'Italia',
    2010: 'España',
    2014: 'Alemania',
    2018: 'Francia',
    2022: 'Francia'
}

print(dicc_campeones)

dicc_campeones[2022] = 'Argentina'
print(dicc_campeones)

# Crear diccionario con listas
anios = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]
campeones = ['Alemania', 'Brasil', 'Francia', 'Brasil', 'Italia', 'España', 'Alemania', 'Francia', 'Argentina']

dicc_campeones = dict(zip(anios, campeones))
print(dicc_campeones)

#Ejercicio Divisas

divisas = {'Dolar':'$','Euro':'€', 'Libra':'£'}

solicitud = input('Qué moneda necesita ver?: ')

print('Este es el valor de la variable: ', solicitud)

resultado = divisas.get(solicitud)

print('Símbolo: ', resultado)