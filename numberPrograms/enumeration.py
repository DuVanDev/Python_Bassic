""" Enumeración exaustiva """
""" 
    En esta se verifican todas las posibles soluciones
"""
# objetivo = int(input('Escoge un numero enter'))
# respuesta = 0

# while respuesta**2 < objetivo:
#     respuesta += 1

# if respuesta**2 == objetivo:
#     print(f'La raiz cuadrada de {objetivo} es {respuesta}')
# else:
#     print(f'{objetivo} no tiene raiz cuadrada exacta')

""" Aproximacion de solucioens """
""" 
    - La aproximación de soluciones no necesita una respuesta exacta
    - se aproxima las soluciones con un margen de error que llamamos 'epsilon'

    entre más pequeño 'epsilon' , más proceso de computo para la maquina
"""
objetivo = int(input('Escoge un numero : '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo :
    respuesta += paso
    # print(respuesta)
    print(abs(respuesta**2 - objetivo))

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta} ')
