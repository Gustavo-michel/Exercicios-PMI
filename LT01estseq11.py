# Este programa calcula o comprimento de uma circunferência
# Importa a biblioteca math para usar o valor de pi
import math
# Recebe o valor do raio
raio = float(input("Digite o raio da circunferência: "))
# Calcula o comprimento da circunferência
comprimento = 2 * math.pi * raio
# Exibe o resultado
print(f"O comprimento da circunferência é: {comprimento:.2f}")