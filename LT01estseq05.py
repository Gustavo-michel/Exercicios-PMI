from math import sqrt

A = int(input('Valor de A: '))
B = int(input('Valor de B: '))
C = int(input('Valor de C: '))

x1 = (-B + sqrt(B** -4*A*C))/2*A
x2 = (-B - sqrt(B** -4*A*C))/2*A

print('Raiz 1: ' , x1)
print('Raiz 2',  x2)