""" 

1. Son imutables
2. Pueden tener cualquier tipo de objeto (hasta funciones)
3. Pueden usarse para retornar varios valores a la vez
"""

""" Asignar una tupla con un solo valor """
one_tuple = ( 1 ,)
print(one_tuple)
""" Asignar una tupla con multiples valores """
one_tuple = (1 ,2 ,3)
print(one_tuple)

""" Desenpaquetar tuplas """
def coordenadas ():
    return (5 , 2)

x , y = coordenadas()
print(f' {x} {y}')