
class Person:
    def __init__(self , name , age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            raise ValueError('Name not could empty')
        self._name = new_name
    

danilo = Person('Danilo', 20)

print(f'El nombre es { danilo.name }')

danilo.name = 'Joven muy diferente'

print(f'El nombre es { danilo.name }')