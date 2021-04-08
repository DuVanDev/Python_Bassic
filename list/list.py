""" 
Las listas son mutables
"""

my_list = [1, 2, 3 ]

""" ingresar un valor """
my_list.append(4)
print(my_list)

my_list[0] = 'a'
print(my_list)

my_list.pop()

for element in my_list:
    print(element)

lista_a = [ 1 , 2 ,3]
lista_b = lista_a

lista_b[0] = 'abc'
print(lista_a)
print(lista_b)

""" Clone list """
print('Clone List')

a = [1 , 2 , 3]
""" Methodo 1 """
print('--- Methodo1 ---')
b = list(a)
b.append(4)
b[0] = 'a'

print(a)
print(b)

""" Methodo 2 """
print('--- Methodo2 ---')
b = a[::]
b.append(4)
b[0] = 'a'

print(a)
print(b)

""" List Conebehention """
my_list = list(range(100))

double = [ i * 2 for i in my_list]
print(double)

even = [ i for i in my_list if i % 2 == 0]
print( even )