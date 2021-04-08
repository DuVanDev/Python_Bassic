menu = """
Bienvenido al conversor de monedas 

1- Pesos colombianos
2- Pesos Argentidos
3- Pesos Mexicanos

Elige una opción
"""

def conversor(tipo_pesos, value_dolar):
    money = input('¿Cuántos pesos'+ tipo_pesos +'argentinos tienes?:')
    money = float(money)
    dolars = money / value_dolar
    dolars = round(dolars,2)
    print("Tienes $"+ str(dolars)+ " dólares")

option  = int(input(menu))

if option == 1:
    conversor('colombianos', 3875)
elif option == 2:
    conversor('Argentinos',65)
elif option == 3:
    conversor('Argentinos',24)
else:
    int(input(menu))

""" 
money_colombia = input('¿Cuántos pesos colombianos tienes?:')
money_colombia = float(money_colombia)

value_dolar = 3875

dolars = money_colombia / value_dolar
dolars = round(dolars,2)
print("Tienes $"+ str(dolars)+ " dólares") """
