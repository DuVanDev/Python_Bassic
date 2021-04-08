""" 
1. Las funciones tienen un tipo
2. Se pueden pasar como argumentos
3. Se pueden utilizar en expresiones
4. Se puede incluir en variables estructuradas de datos como (listas, tuplas, diccionarios etc.)
"""

def multiply ( a , b ):
    return a * b

def add ( a , b ):
    return a + b

def operations ( f , a , b ):
    result = []
    return f(a , b)

print(f' {operations(multiply , 2 ,5)} ')
print(f' {operations(add , 2 ,5)} ')


""" other for to create functions """

add_lambda = lambda x , y : x + y

print(f' {add_lambda(2 ,4)} ')

""" operation into list """

def operation_2 (a , b):
    operation = [ add , multiply ]
    result = []
    for oper in operation:
        result.append(oper(a, b))
    return result

print(f' {operation_2(3 , 7)} ')