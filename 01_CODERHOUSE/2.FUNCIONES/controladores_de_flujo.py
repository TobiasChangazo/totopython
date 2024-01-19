# sentencias de controladores de flujo

# if (si)

# elif (si no, si)

# else (si no)



#ejemplo

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

cumple_condiciones = (nombre != "****") and (5 < edad < 20) and (4 <= len(nombre) < 8) and  (edad * 3 > 35)

if cumple_condiciones:
        print("se cumplen las condiciones")
else:
        print("no se cumplen las condiciones")


# f-strings

valor = 5
cadena = f"la suma entre 5 y 10 es {valor+10}"

#format()

cadena1 = "la suma entre {} y 10 es {}".format(valor, valor+10)

#while 

num = 5
while num>0:
        print(f"{num}")
        num-=1
        print("Una vuelta al bucle")


#continue (imprime por pantalla todos los numeros exepto el 3)

i = 0

while i < 6:
        i+=1
        if i == 3:
                continue
        print("i vale", i)


#pass (imprime por pantalla todos los numeros sin modificaciones)

i = 0

while i < 10:
        i+=1
        if i == 2:
                pass
        print("i vale", i)


#break (rompe con el bucle)

i = 0

while i < 6:
        i+=1
        if i == 3:
                break
        print("i vale", i)


#while-else

chance = 1
while chance <= 3:
     texto = input("escriba si: ")   
     if texto == "si":
        print("lo lograste en el intento ", chance)
        break
     chance +=1
else:
       print("agotaste tus intentos")


#for 

lista = [1,2,3,4,5]
for elemento in lista:
       print("soy un elemento de la lista y valgo", elemento)

# oto ejemplo de for multiplicando los numeros

lista = [1,2,3,4,5]
for elemento in lista:
       print("soy un elemento de la lista y valgo", elemento)
       elemento*=5 
       print("me actualice y ahora valgo", elemento)

#enumerate

numeros = [0,1,2,3,4,5]
for indice, numeros in enumerate(numeros):
       numeros[indice]*=5
       print(numeros)


#range (secuencia de numeros)

for numero in range(10):
        print(numero)

for numero in range(5,10):
       print(numero)

for numero in range(0,20,2):
       print(numero)


#otro ejemplo de range (va del numero 0 al 8 ignorando el 2 y rompiendose en el 8 el bucle)

for numero in range(10):
       pass
       if numero==2:
              continue
       elif numero==8:
              break
       else:
              print("el numero es ", numero)

#funcion sum() sirve para sumar

print(sum(2,2))

#  = 4