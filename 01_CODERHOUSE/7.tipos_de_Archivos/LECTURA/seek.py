f = open("archivo.txt", "r")

print(f.read())
print("esto es despues del primer read ************************")
print(f.read())

f.seek(20)
print(f.read())
print("esto es despues del segundo read ************************")


f.close