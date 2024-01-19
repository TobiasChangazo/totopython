
f = open("archivo.txt", "w")

content = f.read()

f.write("esto es un texto")
f.write("esto es un texto, pero el segundo")
f.write("esto es un texto, pero el tercero")


f.close()
