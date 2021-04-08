import unittest

def suma(number_1 , number_2):
    return number_1 + number_2

class BlackBoxTest( unittest.TestCase ):

    def test_add_two_positive_number(self):
        num_1 = 10
        num_2 = 5
        result = suma(num_1 , num_2)
        
        self.assertEqual(result , 15)
    
    def test_add_two_negative_number(self):
        num_1 = -10
        num_2 = -5
        result = suma(num_1 , num_2)
        
        self.assertEqual(result , -15)


if __name__ == "__main__":
    unittest.main()
