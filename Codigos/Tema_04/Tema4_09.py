# Tama4_09
from Class_Tablas_Hash import TablaHash


H = TablaHash()
H[54] = "gato"
H[26] = "perro"
H[93] = "leon"
H[17] = "tigre"
H[77] = "pajaro"
H[31] = "vaca"
H[44] = "cabra"
H[55] = "cerdo"
H[20] = "pollo"
print(H.slots)
print(H.datos)

print(H[20])

print(H[17])
H[20] = 'pato'
print(H[20])
print(H[99])
print(H.slots)
print(H.datos)
