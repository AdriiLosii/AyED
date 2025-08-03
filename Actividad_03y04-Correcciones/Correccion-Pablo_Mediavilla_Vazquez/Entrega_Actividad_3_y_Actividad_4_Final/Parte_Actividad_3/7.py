from random import randint

vector = []

l = int(input("Dame el numero de elementos: "))

while l<=0:
    l = int(input("Dame el numero de elementos: "))




for i in range (l):
    vector.append(randint(0,100))

print(vector)

w = []

for i in range (0,101):

    if i in vector:

        w.append(vector.index(i))

print(w)

w_ord = []

for i in range (len(w)):
    w_ord.append(vector[w[i]])

print(w_ord)

pos_k = int(input("Posicion del k-esimo: "))

print(w_ord[pos_k])