""" 
https://www.datacamp.com/community/tutorials/python-dictionary-comprehension

"""

def run():
    dictionary = {
        'nombre' : 'Duván',
        'apellido': 'Moreno',
        'lenguaje' : 'Python',
        'edad' : 23
    }
    print(dictionary)
    print(dictionary['nombre'])

    for key in dictionary.keys():
        print(key)
        print(dictionary[key])

    for values in dictionary.values():
        print(values)

    for key, data in dictionary.items():
        print(key + ' - ' + str(data) )


    """ Get element and return one value if not exist """
    print( dictionary.get('estudio' , 'Universidad'))

    """ delete key """
    del dictionary['edad']
    print(dictionary)

    """ Delete all elements """
    dictionary.clear()
    print(dictionary)

if __name__ == "__main__":
    run()