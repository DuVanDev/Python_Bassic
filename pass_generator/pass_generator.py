import random 

def pass_generator():
    capital_letters = ['A' , 'B' , 'C', 'D' , 'E' , 'F' , 'G']
    lowercase_letters = ['a' , 'b' , 'c', 'd' , 'e' , 'f' , 'g']
    special_symbols = ['!' , '#' , '$', '%' , '&' , '/' , '(']
    number = ['1' , '2' , '3', '4' , '5' , '6' , '7' , '8' , '9' , '0']

    characters = capital_letters + lowercase_letters + special_symbols + number
    
    password = []
    for i in range(15):
        random_character =  random.choice(characters)
        password.append(random_character)
    return ''.join(password)

def run():
    password = pass_generator()
    print('Tu nueva contraseña es '+ password)
    pass


if __name__ == "__main__":
    run()