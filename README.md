# Python

# Table of Contents

1. [List](#list)
2. [Dict](#dict)
3. [Functions](#functions)
4. [venv - virtual environment](#venv)
5. [Errors](#errors)
6. [Files](#files)

---

# list

1. [List Comprehensions](##list-comprehensions)

## List comprehensions

### Sintax

`[element for element in iterable if condition]` 

### Example

``` python
squares = [ i**2 for i in range(1 , 10) if i % 3 != 0]  # [9 , 36 , 81] 
```
---

# dict

## Get

we have two forms to get dict data

### Method Get

this method allow add defined if data not exist inside dict

``` python
my_dict = { 
    'David' : 25,
    'Juan'  : 20
}

my_dict.get('Leo') ##
my_dict.get('Marko' , 0) ## 0
my_dict.get('David') ## 25 

```

### Call key

``` python
my_dict = { 
    'David' : 25,
    'Juan'  : 20
}

my_dict['Leo'] ## Error KeyError 
my_dict['Marko'] ## Error KeyError
my_dict['David'] ## 25 

```

## Dict comprehensions

### Sintax

`{ key : value for value in iterable if condition}` 

### Example

``` python
squares = { i : i**3 for i in range(1 , 10) if i % 3 != 0 } ## { 3: 9 , 6: 38 , 9 : 81 } 

```

---

# functions

## Lambda Functions

Anonim functions that not required name

> lambda functions  only have one code line.

### Syntax

```python
lambda arguments : expersions
```

### Example

```python
palindrome = lambda string : string = string[::-1]

palindrome('ana')

```

## High Order Functions

is a functions that **receive** a **function as parameter**

### Example

```python

def greeting(func):
  func()

def sayHi:
  print('Hi')

def sayBye():
  print('Bye')

greeting(sayHi) # 'Hi'
greeting(sayBye) # 'Bye'

```

### filter

```python
my_list = [1,2,3,4]

odd = list(filter(lambda x: x % 2 != 0 , my_list))

print(odd) ## [1,3]

```

### map

```python

my_list = [1,2,3,4]

odd = list(map(lambda x: x**2 , my_list))

print(odd) ## [2, 4 , 9 , 16]

```

### reduce

```python

from functools import reduce

my_list = [ 2, 2, 2]

all_multiply = reduce(lambda a , b : a * b, my_list)

print(all_multiply) ## 2

```

# venv

## create venv

`py -m venv venv`

## Dependencies

### Show dependecies
`pip freeze`

### Create dependencies file

`pip freeze > requirements.txt`

this command help to creat and update our `requirement.txt` file
`requirements.txt` not automatic updated

### Install dependecies inside requirements.txt

`pip install -r requirements.txt`

# errors

## type errors

### SyntaxError

This error stop all code and not execute line code.

### Exception

This error stop the code only when find one exception error.

## Handler Errors

### try - except

```python

try: 
  # code here
except TypeError:
  # handle except error

```

### raise

Create custome execption error that help code correct runtime code.

```python

try: 
  if len(value) == 0:
    raise ValueError('No is value required')
  # code here
except ValueError as ve:
  print(ve)
  # handle except error
```

### finally

this handle, help to run code inside **finally** if error exit or not.

```python

try: 
  #code here
except:

finally: 
  # code finally here

```

### Assert statements

Assert are affirmations that help catch error.

```python

def name_function(string):
  assert len(string) > 0, "Can't get into empty string" # AssertionError: Can't get into empty string

```

# files

## modes

- R (read)
- W (write)
- A (append)

### Read
```python
with open("[file route]" , "r" , encoding="utf-8") as f:
  # code to work with file
```

### Write
```python
with open("[file route]" , "w" , encoding="utf-8") as f: 
  # code to work with file
```

### Append
```python
with open("[file route]" , "a" , encoding="utf-8") as f: 
  # code to work with file
```
