def costo_camion(nombre_archivo):
    #abrir el archivo .csv
    f = open(nombre_archivo, 'rt',encoding='utf8' ) 
    precio_total = 0.0
    header = next(f)  # para no leer la cabecera
    for i in f:
        columna = i.split(',')
        try:
            column_precio = float(columna[2])
            precio_total  = precio_total + column_precio
            print(column_precio)
        except:
            print("An exception occurred")

    f.close()
    return precio_total

costo_total = costo_camion('Data/camion_error.csv')
print("costo: ", costo_total)