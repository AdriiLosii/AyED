from Ej6_Clase import *
from datetime import *

fechaactual = str(datetime.now()).strip()
h = str(fechaactual[11:-7]).replace(':',' ').split()
horaactual = Hora(int(h[0]), int(h[1]), int(h[2]))

print("Hora actual ->", horaactual)
print("\nNos encontramos en la", horaactual.partedeldia())

while 1:
    try:

        dato = input("\nIntroduce la hora como hh:mm:ss o hh/mm/ss: ").strip()

        if dato[-3] == ':':
            d = dato.replace(':',' ')
            t = d.split()

            horaintroducida = Hora(int(t[0]), int(t[1]), int(t[2]))

            break

        elif dato[-3] == '/':
            d = dato.replace('/',' ')
            t = d.split()

            horaintroducida = Hora(int(t[0]), int(t[1]), int(t[2]))
            
            break

        else:
            1/0
    except:
        print("\nPor favor, introduzca una hora valida\n")


if horaintroducida.es_menor(horaactual) == 1:
    print("\nLa hora introducida es menor que la actual\n")
elif horaintroducida.es_menor(horaactual) == "Igual":
    print("\nLa hora introducida es igual que la actual\n")
else:
    print("\nLa hora introducida es mayor que la actual\n")

