# Este programa calcula a hipotenusa de um triângulo retângulo
# Importa a biblioteca math para usar a função sqrt
import math
# Recebe o valor do primeiro cateto
cateto1 = float(input("Digite o valor do primeiro cateto: "))
# Recebe o valor do segundo cateto
cateto2 = float(input("Digite o valor do segundo cateto: "))
# Calcula a hipotenusa
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
# Exibe o resultado
print(f"A hipotenusa é: {hipotenusa}")