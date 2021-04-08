def factorial(n):
    """ 
    calcula el factorial de n
    param int n,  n > 0
    return n!
    """
    if n == 1:
        return 1
    
    return n * factorial(n - 1 )


n = int(input('Escribe un numero entero'))

print(factorial(n))