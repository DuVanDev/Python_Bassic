""" 
    - Es una secuencia de enteros
    - range(comienzo, fin, pasos)
    - son inmutables
    - Son eficientes en uso de memoria
"""

my_range = range(1, 5)

def print_range(range):
    for i in range:
        print(i)
    

print_range(my_range)
""" 
return 
1
2
3
4
"""
print(f'------- my_range 0,7,2')
my_range = range(0 , 7 ,2)
print_range(my_range)


print(f'------- my_range 0,8,2')
my_other_range = range(0 , 8 ,2)
print_range(my_other_range)


""" Value Equality """
print(f'------- my_range == my_other_range')
print(my_range == my_other_range)


""" Object Equality """
print(f'------- my_range is my_other_range')
print(my_range is my_other_range)


""" Object Equality """
print(f'------- Impares')
my_range_none = range(1 , 100 , 2)
print_range(my_range_none)




