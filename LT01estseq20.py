"""
Receba  3  coeficientes  A,  B  e  C  de  uma  equação  do  2º  grau  da  fórmula 
AX²+BX+C=0.  Verifique  e  mostre  a  existência  de  raízes  reais  e  se  caso 
exista, calcule e mostre.
"""

A = int(input('Valor de A: '))
# Recebe o valor de B
B = int(input('Valor de B: '))
# Recebe o valor de C
C = int(input('Valor de C: '))
# Verifica se é uma equação do 2º grau
if A == 0:
    print("Não é uma equação do 2º grau.")
else:
    # Calcula o delta
    delta = B**2 - 4*A*C
    print(f"Delta: {delta}")
    # Verifica se existem raízes reais
    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        # Calcula a raiz única
        x = -B / (2*A)
        print(f"Existe uma raiz real: x = {x}")
    else:
        # Calcula as duas raízes reais
        x1 = (-B + delta**0.5) / (2*A)
        x2 = (-B - delta**0.5) / (2*A)
        print(f"Existem duas raízes reais: x1 = {x1}, x2 = {x2}")