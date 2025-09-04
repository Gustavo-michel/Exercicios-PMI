# Este programa calcula a diferença do maior pelo menor valor entre dois inteiros
# Recebe o primeiro número inteiro
num1 = int(input("numero 1: "))
# Recebe o segundo número inteiro
num2 = int(input("numero 2: "))
# Verifica qual é o maior e calcula a diferença
if num1 > num2:
    diferenca = num1 - num2
    print(f"A diferença do maior {num1} pelo menor {num2} é: {diferenca}")
elif num1 < num2:
    diferenca = num2 - num1
    print(f"A diferença do maior {num2} pelo menor {num1} é: {diferenca}")
else:
    print("Numeros iguais")

