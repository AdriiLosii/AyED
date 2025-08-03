from Clase_horas import *#Importamos todas las funciones de la clase horas.

formato = "%d:%m:%y"#establcemos el formato.


hora1=Hora(14,28,36)#Generamos las dos horas.
hora2=Hora(19,5,3)
print("Hora 1: "+str(hora1))#Y las imprimimos.
print("Hora 2: "+str(hora2))
print(str(hora1),"<",str(hora2),":",hora1<hora2)#Comprobamos si la primera es menor que la segunda.
print(str(hora1),"<=",str(hora2),":",hora1<=hora2)#Comprobamos si la primera es menor o igual que la segunda.
print(str(hora1),">",str(hora2),":",hora1>hora2)#Comprobamos si la primera es mayor que la segunda.
print(str(hora1),">=",str(hora2),":",hora1>=hora2)#Comprobamos si la primera es mayor o igual que la segunda.
print(str(hora1),"==",str(hora2),":",hora1==hora2)#Comprobamos si son iguales.
print(str(hora1),"!=",str(hora2),":",hora1!=hora2)#Comprobamos si son distintas.
