"""
Receba 2 valores reais. Calcule e mostre o maior deles.
"""

num1 = float(input("numero 1: "))
num2 = float(input("numero 2: "))

if num1 > num2:
    print(f"O maior é: {num1}")
elif num1 < num2:
    print(f"O maior é: {num2}")
else:
    print("Numeros iguais")
