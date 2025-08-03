from Class_ListaEnlazadaCircular_01 import ListaCircular

robot = ListaCircular([0,0,0])

robot.agregar([0,0,1])
robot.agregar([0,1,0])
robot.agregar([0,1,1])
robot.agregar([1,0,0])
robot.agregar([1,0,1])
robot.agregar([0,-1,0])
robot.agregar([0,-1,1])
robot.agregar([-1,0,0])
robot.agregar([-1,0,1])

print(robot)

print("\nPrint de simulación:")
robot.Coger_pieza("coger pieza de",[0,0,0])
robot.Go_to("trasladándose a",[0,1,1])
robot.Dejar_pieza("dejar pieza en",[0,1,0])
print()
robot.Coger_pieza("coger pieza de",[0,1,0])
robot.Go_to("trasladándose a",[1,0,1])
robot.Dejar_pieza("dejar pieza en",[1,0,0])
print()
robot.Coger_pieza("coger pieza de",[1,0,0])
robot.Go_to("trasladándose a",[0,-1,1])
robot.Dejar_pieza("dejar pieza en",[0,-1,0])
print()
robot.Coger_pieza("coger pieza de",[0,-1,0])
robot.Go_to("trasladándose a",[0,0,1])
robot.Dejar_pieza("dejar pieza en",[0,0,0])

input("\nPulse ENTER para finalizar.")