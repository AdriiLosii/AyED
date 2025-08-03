from Clase_Fechas import Fecha  #Importamos todas las funciones de la clase fechas.

formato = "%d-%m-%y"#establcemos el formato.


f1=Fecha(31,4,1978)#Generamos las dos fechas.
f2=Fecha(29,2,2003)
print("Fecha 1: "+str(f1))#Y las imprimimos.
print("Fecha 2: "+str(f2))
print(str(f1),"<",str(f2),":",f1<f2)#Comprobamos si la primera es menor que la segunda.
print(str(f1),"<=",str(f2),":",f1<=f2)#Comprobamos si la primera es menor o igual que la segunda.
print(str(f1),">",str(f2),":",f1>f2)#Comprobamos si la primera es mayor que la segunda.
print(str(f1),">=",str(f2),":",f1>=f2)#Comprobamos si la primera es mayor o igual que la segunda.
print(str(f1),"==",str(f2),":",f1==f2)#Comprobamos si son iguales.
print(str(f1),"!=",str(f2),":",f1!=f2)#Comprobamos si son distintas.
