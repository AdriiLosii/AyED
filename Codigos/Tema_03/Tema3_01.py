#Tema3_01
def aCadena(n,base):
   cadenaConversion = "0123456789ABCDEF"
   if n < base:
      return cadenaConversion[n]
   else:
      return aCadena(n//base,base) + cadenaConversion[n%base]

num=int(input("Dame un numero decimal: "))
base=int(input("A que base <16 lo quieres transformar: " ))
print(aCadena(num,base))
