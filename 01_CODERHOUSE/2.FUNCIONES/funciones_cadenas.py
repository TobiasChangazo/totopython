#funciones en las cadenas

cadena = 'hola a todos'

#la cadena va a estar toda en mayuscula

cadena.upper()

#la cadena va a estar toda en minuscula

cadena.lower()

#convierte la primer caracter en mayuscula

cadena.capitalize()

#convierte la primera letra de cada palabra en mayuscula

cadena.title()

#nos dice cuantas veces se repite un mismo elemento 

cadena.count("a")

#busca dentro del string la primera letra o plabra que deseo dentro de la cadena

cadena.find("o")

#busca dentro del string la ultima letra o plabra que deseo dentro de la cadena

cadena.rfind("o")

#nos sirve para dividir la cadena por el caracter el cual queremos dividirla

cadena.split() #si no le especificamos un caracter a la cadena la va a dividir entre las palabras
cadena.split("a") #va a dividir la cadena pero sin la letra "a"

#si utilizamos split y queremos volver a la cadena como era antes se usa un separador 

' '.join(cadena)

#elimina caracteres dentro de la cadena

cadena_ejemplo = "--------------hola a todos-------------"

cadena.strip("-")

#nos permite reemplazar un caracter por otro dentro de la cadena

cadena.replace("h", "H")