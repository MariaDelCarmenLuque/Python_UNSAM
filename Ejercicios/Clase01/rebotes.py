# EJERCICIO 1.5 
# Una pelota de goma es arrojada desde una altura
# de 100 metros y cada vez que toca el piso salta 
# 3/5 de la altura desde la que cayó. 
# Escribí un programa que imprima una tabla mostrando
# las alturas que alcanza en cada uno de sus primeros 
# diez rebotes.

altura=100 #altura de lanzamiento en metros
i=0 # contador de rebotes

while i<10:
    altura=round(altura*0.6,4)
    i+=1
    print (i,altura)
