from Class_Tablas_Hash import TablaHash



H = TablaHash()
H[54] = "gato"
print("Comparaciones al 10%: ",H.compa())
H[26] = "perro"
H[93] = "leon"
print("Comparaciones al 25%: ",H.compa())
H[17] = "tigre"
H[77] = "pajaro"
print("Comparaciones al 50%: ",H.compa())
H[31] = "vaca"
H[44] = "cabra"
H[55] = "cerdo"
print("Comparaciones al 75%: ",H.compa())
H[20] = "pollo"
H[22] = "gusano"
print("Comparaciones al 90%: ",H.compa())
H[64] = "mono"
print("Comparaciones al 100%: ",H.compa())

print(H.slots)
print(H.datos)