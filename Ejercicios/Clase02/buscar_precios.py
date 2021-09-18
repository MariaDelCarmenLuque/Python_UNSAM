def buscar_precio(fruta):
    #abrir el archivo precio.csv
    f = open('E:\PYTHON\Programacion_Python_UNSAM\ejercicios_python\ejercicios_python\Data\precios.csv', 'rt',encoding='utf8')
    for i in f:
        columna =i.split(',')
        if(len(columna)>=2):
            fruta_buscada= str (columna[0])
            precio = float(columna[1])
            if fruta == fruta_buscada:
                mensaje= print("El precio de un cajón de ",fruta, "es :", precio)
                return mensaje
    mensaje=" No figura en el listado de precios."
   #print(fruta,mensaje)
    f.close()
    return mensaje
buscar_fruta=input("Ingrese la fruta que desea buscar:")
precio= buscar_precio(buscar_fruta)
print(precio)