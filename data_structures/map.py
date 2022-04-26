## Applies the function pew on the list and returns the list as a map object which can be turned back into a list

y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def pew(x):
    return x**x

print(list(map(pew, y)))

## Filter function - applies some kind of filter (user defined) to a list and returns only the True values.

def isOdd(x):
    return x % 2 != 0

print( list(filter(isOdd, y)) )