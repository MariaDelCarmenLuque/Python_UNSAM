#EJERCICIO 1.13

# Escribí un programa llamado esfera.py que le pida al usuario que ingrese por teclado 
# el radio r de una esfera y calcule e imprima el volumen de la misma. 
# Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.

# Finalmente, ejecutá el programa desde la línea de comandos para responder 
# ¿cuál es el volumen de una esfera de radio 6? Debería darte 904.7786842338603.

import math
# r -> Radio de la esfera 
r = int(input("Ingrese radio de esfera: "))
volumen= (4/3)* math.pi*(r**3)
print(volumen)

#INPUT
# Ingrese radio de esfera: 6
# 904.7786842338603