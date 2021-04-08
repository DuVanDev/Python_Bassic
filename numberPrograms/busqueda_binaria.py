""" Busqueda binaria """
""" 
-   Cuando la respuesta se encuentra en un conjunto ordenado,
    podemos utilizar búsqueda binaria

-   Es altamente eficiente, pues corta el espacio de búsqueda
    en dos por cada iteración

La busqueda binaria recorta a la mitad el conjunto de posibilidades

NOTA solo funciona cuando nuestro conjunto de valores tiene un orden
"""

objetivo = int(input('Escoge un numero : '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0 , objetivo)
respuesta = alto + bajo
print(respuesta)
respuesta = respuesta / 2
print(respuesta)


while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo = {bajo} , alto = {alto} , respuesta = {respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo ) / 2

print(f'la reiz de {objetivo} es {respuesta}')