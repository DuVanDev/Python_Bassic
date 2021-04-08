
def expo_number_2(expo):
    
    return 2 ** int(expo)

def run_while():
    count = 1
    LIMITE = 1000
    # while count <= LIMITE :
    #     expo = expo_number_2(count)
    #     print('2 elevado a ' + str(count) + ' es ' + str(expo) )
    #     count = count + 1

    count = 1
    potencia_2 = expo_number_2(count)
    while potencia_2 <= LIMITE:
        print('2 elevado a ' + str(count) + ' es ' + str(potencia_2) )
        count += 1
        potencia_2 = expo_number_2(count)


def run_for():
    LIMITE = 101
    for contador in range(1,LIMITE):
        print(contador)
    
    for i in range(10):
        print(11 * i)


def run_loop_string():
    # nombre = input('Escribe tu nombre:')
    # for letra in nombre:
    #     print(letra)
    
    sentece = input('Escribe una frase:')
    for character in sentece:
        print(character.upper())

def run_break_and_continue():
    for counter in range(11):
        if counter % 2 != 0:
            continue
        print('Numero modulo 2 es ' + str(counter))
    
    for i in range(20):
        print('Numero es ' + str(i))
        if i == 10:
            break
    

if __name__ == "__main__":
    # run_while()
    # run_for()
    # run_loop_string()
    run_break_and_continue()