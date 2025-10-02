'''
Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
'''

valor = int(input("Digite um valor inteiro: "))

if valor % 2 == 0:
    print("é divisivel por 2")
else:
    print("Não é divisivel por 2")

if valor % 3 == 0:
    print("é divisivel por 3")
else:
    print("Não é divisivel por 3")