# EJERCICIO 1.18
# Usá una iteración sobre el string cadena para agregar la 
# sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda
#  luego de cada vocal.
cadena = input("Ingresar cadena : ")
capadepenapa = ''
for i in range(len(cadena)):
    if cadena[i] == 'a':
        capadepenapa+='apa'
    elif cadena[i] == 'e':
        capadepenapa+='epe'
    elif cadena[i] == 'i':
        capadepenapa+='ipi'
    elif cadena[i] == 'o':
        capadepenapa+='opo'
    elif cadena[i] == 'u' and len(cadena[:i])>1:
        if len(cadena[:i])>1 and(cadena[i-1]=='q'or cadena[i-1]=='g') and (cadena[i+1]=='e' or cadena[i+1]=='i'):
            capadepenapa+=cadena[i]
        else:capadepenapa+='upu'
    else:capadepenapa+=cadena[i]
print("Palabra Geringosa: ", capadepenapa)
