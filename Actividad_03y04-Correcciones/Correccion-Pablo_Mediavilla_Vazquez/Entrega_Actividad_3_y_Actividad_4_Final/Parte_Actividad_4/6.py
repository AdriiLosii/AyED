from  Class_Tablas_Hash import TablaHash

th = TablaHash()

th[54]="tiburon"
th[78]="calamar"
th[35]="aguila"
th[62]="buho"

print("Espacios ocupados en la tabla Hash ==>",th.__len__())
print(th.datos)