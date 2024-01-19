#importar la libreria (sys)

import sys

#se va a ejecutar si se le envian dos argumentos reales
if len(sys.argv) == 3:

    cadena = sys.argv[1]

    repeticiones = int(sys.argv[2])

    for repeticiones in range(0, repeticiones):
        print(cadena)
else:
    print("error , introduce bien los argumentos")
    
