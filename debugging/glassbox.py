""" 
testing 

if 
debe probar todas las condiciones
1. probar if principal
2. probar elif 
3. probar else

loop
probar
1. donde no se entre al loop
2. donde se entre 1 vez
3. donde se entre mas de una vez al loop

recursiones
probar
1. donde no se entre al loop
2. donde se entre 1 vez
3. donde se entre mas de una vez al loop

while loop
probar
1. donde la condicion de prueba es falsa
2. una prueba donde se realiza los break
"""


import unittest

def is_adut(age):
    if age >= 18:
        return True
    else:
        return False

class TestGlassBox ( unittest.TestCase):
    
    def test_is_adult(self):
        age = 20

        result = is_adut(age)

        self.assertEquals(result , True)
    
    def test_is_not_adult(self):
        age = 10

        result = is_adut(age)

        self.assertEquals(result , False)
    



if __name__ == '__main__':
    unittest.main()