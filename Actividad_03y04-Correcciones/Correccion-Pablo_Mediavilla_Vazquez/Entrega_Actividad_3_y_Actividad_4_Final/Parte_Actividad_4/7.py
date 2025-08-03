from  Class_Tabla_Hash_T import hash_table
from random import *

th = hash_table()

for i in range(20):
    num = randint(0,20)
    th.Insert(str(num))

number_delete = randint(0,20)

print('Lista antes de borrar el numero {0}'.format(number_delete))

print(th.table, '\n')

th.Remove(str(number_delete))

print('\n',th.table)