import json

data = {}

data["clientes"] = []


data["clientes"].append({
    'nombre': 'aron',
    'apellido': 'lopez',
    'edad': 18})

data["clientes"].append({
    'nombre': 'jeremias',
    'apellido': 'perez',
    'edad': 24})

data["clientes"].append({
    'nombre': 'roberto',
    'apellido': 'suarez',
    'edad': 68})

# with open("miarchivojson.json", "w") as file:                   esto crea un archivo aparte
#     json.dump(data, file, indent=3)

with open("miarchivojson.json") as file:                        # esto muestra la info en consola
    data_lectura = json.load(file)                              
    
for cliente in data_lectura['clientes']:
    print('Nombre', cliente['nombre'])
    print('Edad', cliente['edad'])
    print('Apellido', cliente['apellido'])
    print('')
    
    
    