# Este programa calcula o valor do terceiro ângulo de um triângulo
# Recebe o valor do primeiro ângulo
angulo1 = float(input("Digite o valor do primeiro ângulo (em graus): "))
# Recebe o valor do segundo ângulo
angulo2 = float(input("Digite o valor do segundo ângulo (em graus): "))
# Calcula o valor do terceiro ângulo
angulo3 = 180 - (angulo1 + angulo2)
# Exibe o resultado
print(f"O valor do terceiro ângulo é: {angulo3} graus")