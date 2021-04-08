import random


def number_is_higher_or_less(user_number,random_number):
    return user_number > random_number

def run():
    random_number = random.randint(1,100)
    user_number = int(input('Selecciona un numero del 1 al 100 : '))

    while user_number != random_number:
        if number_is_higher_or_less(user_number,random_number):
            print('El numero debe ser más pequeño ->')
        else:
            print('El numero debe ser más grande -> ')
        user_number = int(input('Selecciona un numero del 1 al 100 : '))
    
    print('Es correcto el numero es '+ str(user_number) + ' - ' + str(random_number) )


if __name__ == "__main__":
    run()