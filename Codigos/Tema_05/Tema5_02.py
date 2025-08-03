#Tema5_02
from Class_Arboles import ArbolBinario

r = ArbolBinario('a')
print(r.obtenerValorRaiz())
print(r.obtenerHijoIzquierdo())
r.insertarIzquierdo('b')
print(r.obtenerHijoIzquierdo())
print(r.obtenerHijoIzquierdo().obtenerValorRaiz())
r.insertarDerecho('c')
print(r.obtenerHijoDerecho())
print(r.obtenerHijoDerecho().obtenerValorRaiz())
r.obtenerHijoDerecho().asignarValorRaiz('hola')
print(r.obtenerHijoDerecho().obtenerValorRaiz())

