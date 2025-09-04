# Este programa calcula as raízes de uma equação do 2º grau
# Importa a função sqrt para calcular a raiz quadrada
from math import sqrt
# Recebe o valor de A
A = int(input('Valor de A: '))
# Recebe o valor de B
B = int(input('Valor de B: '))
# Recebe o valor de C
C = int(input('Valor de C: '))
# Calcula a primeira raiz
x1 = (-B + sqrt(B** -4*A*C))/2*A
# Calcula a segunda raiz
x2 = (-B - sqrt(B** -4*A*C))/2*A
# Exibe a primeira raiz
print('Raiz 1: ' , x1)
# Exibe a segunda raiz
print('Raiz 2 ',  x2)