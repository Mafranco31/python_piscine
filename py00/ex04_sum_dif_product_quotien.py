import sys

arg = sys.argv[1:]
if not arg:
    print('This program needs exactly 2 arguments.')
    exit()
if len(arg) != 2:
    print('This program needs exactly 2 arguments.')
    exit()
try:
    a = int(arg[0])
    b = int(arg[1])
except ValueError:
    print('InputError: only numbers')
    exit()
def sum(a, b):
    return(a + b)
def difference(a, b):
    return(a - b)
def product(a, b):
    return(a * b)
def quotient(a, b):
    if b == 0:
        return('ERROR (div by zero)')
    return(a / b)
def remainder(a, b):
    if b == 0:
        return('ERROR (modulo by zero)')
    return(a % b)

print('Sum: ', sum(a, b), '\nDifference: ', difference(a, b), '\nProduct: ', product(a, b), '\nQuotient: ', quotient(a, b), '\nRemainder: ', remainder(a, b))