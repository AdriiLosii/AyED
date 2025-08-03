from Class_Jarras import Jarra

jarra3 = Jarra(3)
jarra4 = Jarra(4)

jarra3.llenar()
print("Llenamos la jarra de 3L -->",jarra3.__str__())

jarra3.trasladar(jarra4)
print("Jarra de 3L -->",jarra3.__str__(),jarra4.__str__(),"<-- Jarra de 4L")

jarra3.llenar()
print("Llenamos la jarra de 3L -->",jarra3.__str__())

jarra3.trasladar(jarra4)
print("Jarra de 3L -->",jarra3.__str__(),jarra4.__str__(),"<-- Jarra de 4L")

jarra4.vaciar()
print("Vaciamos la jarra de 4L -->",jarra4.__str__())

jarra3.trasladar(jarra4)
print("Jarra de 3L -->",jarra3.__str__(),jarra4.__str__(),"<-- Jarra de 4L")