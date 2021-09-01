# Python

# Table of Contents

1. [List](#List)
2. [Dict](#Dict)
3. [venv - virtual environment](#venv)

# List

## List comprehensions

### Sintax

`[element for element in iterable if condition]` 

### Example

``` python
squares = [ i**2 for i in range(1 , 10) if i % 3 != 0]  # [9 , 36 , 81] 
```

#Dict

## Dict comprehensions

### Sintax

`{ key : value for value in iterable if condition}` 

### Example

``` python
squares = { i : i**3 for i in range(1 , 10) if i % 3 != 0 } ## { 3: 9 , 6: 38 , 9 : 81 } 

```

---


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
