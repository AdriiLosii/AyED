from tablas_hash import TablaHash

H = TablaHash()
H[54] = "gaviota"
H[26] = "pez"
H[93] = "leon"
H[17] = "rengar"
H[77] = "ardilla"
H[31] = "vaca"
H[44] = "cabra"
H[55] = "cerdo"
H[20] = "pollo"
print(H.slots)
print(H.datos)

print(H.len())

print(H[20])

print(H[17])
H[20] = "peruano"
print(H[20])
print(H[99])
print(H.slots)
print(H.datos)