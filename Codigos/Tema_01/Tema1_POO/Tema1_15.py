import random

from Class_Empleados import Persona, Empleado

p1 = Persona("Jose", 18)
p2 = Empleado("Jose", 18, "Usc", "jangel@usc.es")

if __name__ == "__main__":
    random.seed()
    p = random.choice([p1, p2])
    print(p)
