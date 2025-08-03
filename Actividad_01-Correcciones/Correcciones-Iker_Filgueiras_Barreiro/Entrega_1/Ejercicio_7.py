"""7. Implementar con todos sus componentes la clase Polinomio, de manera que se
puedan ejecutar todas las operaciones sobre polinomios
"""

#Creamos la clase
class polinomial:
    def __init__(self, coeficientes):
        coefs = []
        for r in coeficientes:
            coefs.append(float(r))
        self.coefs = coefs
        
    #Representacion de los polinomios de la forma 'a(0)z**n +...+ a(n-1)z + a(n)', donde (i) son los coeficientes
    def __str__(self):
        string = ""
        suma_str = " + "
        for n in range(len(self.coefs)):
            n_coef = str(self.coefs[n])
            if n < len(self.coefs) - 2:
                string = string + n_coef + "z**"+ \
                str(len(self.coefs) - n - 1) + suma_str
            elif n < len(self.coefs) - 1:
                string = string + n_coef + "z" + suma_str
            else:
                string = string + n_coef
        return string

    def __repr__(self):
        return str(self)
    
    #Metodo que devuelve los coeficientes añadidos a la variable elevada al x grado
    def coef(self, i):
        if 0 <= i < len(self.coefs):
            return self.coefs[-1 - i]
        else:
            return 0.0

    #Metodo para sumar dos polinomios
    def suma(self, other):
        rev_poli = []
        rev_self_coefs = self.coefs[::-1]
        rev_other_coefs = other.coefs[::-1]
        
        for n in range(len(rev_self_coefs)):
            if n <= len(rev_other_coefs) - 1:
                rev_poli.append(rev_self_coefs[n] + rev_other_coefs[n])
            else:
                rev_poli.append(rev_self_coefs[n])
                
        if len(rev_other_coefs) > len(rev_self_coefs):
            for n in range(len(rev_self_coefs), len(rev_other_coefs)):
                rev_poli.append(rev_other_coefs[n])
                
        new_poli = rev_poli[::-1]
        return polinomial(new_poli)

    def __suma__(self, other):
        return self.suma(other)
    
    #Metodo para multiplicar dos polinomios
    def mul(self, other):
        new_poli = polinomial([0])
        rev_self_coefs = self.coefs[::-1]
        rev_other_coefs = other.coefs[::-1]
        
        for n in range(len(rev_self_coefs)):
            if n == 0:
                rev_poli_term = [r * rev_self_coefs[n] for \
                r in rev_other_coefs]
            else:
                rev_poli_term = [0 for m in range(n)] + \
                [r * rev_self_coefs[n] for r in rev_other_coefs]
            poli_term = rev_poli_term[::-1]
            new_poli = new_poli + polinomial(poli_term)
        return new_poli

    def __mul__(self, other):
        return self.mul(other)
    
    #Metodo para evaluar un polinomio cambiando la variable z por un input de valor v
    def val(self, v):
        rev_self_coefs = self.coefs[::-1]
        value = 0
        
        for n in range(len(rev_self_coefs)):
            value = value + rev_self_coefs[n]*(v**(n))
        return value

    def __call__(self, v):
        return self.val(v)
    
    #Metodo que encuentra las raices de un polinomio de ordeb 2 o menos
    def raices(self):
        if len(self.coefs) == 1:
            print ("La raiz no existe")
        elif len(self.coefs) > 3:
            
            rev_self_coefs = self.coefs[::-1]
            resultado = True
            for n in range(3,len(rev_self_coefs)):
                resultado = resultado and rev_self_coefs[n] == 0
            if resultado:
                rev_self_coefs = rev_self_coefs[:3]
                self.coefs = rev_self_coefs[::-1]
                return self.raices()
            else:
               print ("Grado demasiado elevado para resolver por raices")
        elif len(self.coefs) == 2:
    
            if self.coefs[0] == 0:
                print ("La raiz no existe")
            else: 
                raiz = (0 - self.coefs[1]) / self.coefs[0]
                return raiz
        else:
            a = self.coefs[0]
            b = self.coefs[1]
            c = self.coefs[2]
            
            if a == 0:
                if b == 0:
                    print ("La raiz no existe")
                    return None
                else:
                    return -c / b
                
            elif b**2 < 4*a*c:
                import cmath
                raiz1 = (-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a)
                raiz2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)
            else:
                raiz1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
                raiz2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
            resultado = [raiz1, raiz2]
            return resultado

pol1=polinomial([1 ,2 ,3])
pol2=polinomial([2,3,4])
pol3=polinomial.suma(pol1,pol2)
pol4=polinomial.raices(pol1)
pol5=pol1.val(1)
print('Polinomio 1 ->',pol1)
print('Polinomio 2 ->',pol2)
print('Suma ->',pol3)
print('Multiplicacion ->',pol4)
print('Evaluado en el valor 1',pol5)
