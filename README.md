# Python

# Table of Contents

1. [list](#list)
2. [Dict](#dict)
3. [Functions](#functions)
4. [venv - virtual environment](#venv)
5. [Errors](#errors)

---

# list

## List comprehensions

### Sintax

`[element for element in iterable if condition]` 

### Example

``` python
squares = [ i**2 for i in range(1 , 10) if i % 3 != 0]  # [9 , 36 , 81] 
```
---

# dict

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



