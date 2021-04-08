
def decorator_function (function):
    def wrapper():
        print('Este mensaje es un mesaje inicial')
        function()
        print('Este mensaje es un mesaje Final')
    return wrapper


@decorator_function
def Buzzz():
    print('BUzzzzzzzzzzzzzz')

Buzzz()