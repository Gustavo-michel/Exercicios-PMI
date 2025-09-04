# Este programa calcula a quantidade de litros gastos em uma viagem
# Recebe o tempo de percurso em horas
tempo = float(input("Digite o tempo de percurso (em horas): "))
# Recebe a velocidade média em km/h
velocidade_media = float(input("Digite a velocidade média (em km/h): "))
# Calcula a distância percorrida
distancia = tempo * velocidade_media
# Calcula os litros gastos (12 km/l)
litros_gastos = distancia / 12
# Exibe o resultado
print(f"Quantidade de litros gastos na viagem: {litros_gastos:.2f} litros")