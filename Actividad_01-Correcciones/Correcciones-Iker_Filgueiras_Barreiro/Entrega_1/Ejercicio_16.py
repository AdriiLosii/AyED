#¿Puedes mejorar el algoritmo del problema anterior para que sea lineal? Explica.


###################################### METODO DE BUSQUEDA O(log(n)) ####################################################
#La búsqueda binaria uniforme guarda el índice del elemento del medio y el número de elementos alrededor del elemento del medio que no hemos eliminado todavía. 
#La búsqueda binaria es más eficiente que la búsqueda lineal en los arreglos ordenados, exceptuando los arreglos que contenga pocos elementos. 
#Funcion para devolver el k-esimo numero mas pequeño  
def kesimo(arr, n, k):
 
    # Sortea el array dado
    arr.sort()
 
    # Devuelve el k-esimo numero mas pequeño del array sorteado
    return arr[k-1]
 
# Codigo principal
if __name__=='__main__':
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 2
    print("El k-esimo numero mas pequeño es: ",
          kesimo(arr, n, k))





######################################### METODO DE BUSQUEDA LINEAL ####################################################     
#La busqueda lineal es un simple algoritmo de búsqueda que comprueba cada elemento hasta que encuentre el valor buscado.
#La busqueda lineal en el peor y en el promedio de los casos es O(n)
#La busqueda lineal en el mejor de los casos es O(1)
import random

#creating random list
l =list(range(1000))
random.shuffle(l)

a=min(l)
b=max(l)

ch = [0 for i in range(a,b)]

i=a
while i<=b:
    pos = l[i] - a
    ch[pos] = ch[pos] + 1
    i += 1
sum=0
pos = 0
k = int(input("enter the value of kth element to find"))
while sum<k:
    sum = ch[pos] + sum
    pos = pos +1

x= ch[pos-1] + a
print("%d is the K'th element of the list" % (x))