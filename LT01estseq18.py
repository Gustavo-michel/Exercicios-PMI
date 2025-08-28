"""
Receba  2  valores  inteiros.  Calcule  e  mostre  o  resultado  da  diferença  do 
maior pelo menor valor.
"""

num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))

if num1 > num2:
    diferenca = num1 - num2
    print(f"A diferença do maior {num1} pelo menor {num2} é: {diferenca}")
elif num1 < num2:
    diferenca = num2 - num1
    print(f"A diferença do maior {num2} pelo menor {num1} é: {diferenca}")
else:
    print("Numeros iguais")

