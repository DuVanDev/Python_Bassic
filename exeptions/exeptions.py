def divide_elements_list(my_list , divide):
    try:
        return [ i / divide for i in my_list]
    except ZeroDivisionError as e:
        print(e)
        return my_list

my_list = list(range(10))
divide = 0 

print(divide_elements_list(my_list , divide))

""" EAFP (easy to ask for forgiveness) """
""" LBYL (look before you leap) """


def add(a , b):
    assert type(a) == int or type(a) == float  , f'{a} no es un int o float'
    assert type(b) == int or type(b) == float   , f'{b} no es un int o float'
    return a + b

print(add(1 ,5))
