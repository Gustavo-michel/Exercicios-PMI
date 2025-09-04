# Este programa calcula o valor de um depósito com rendimento de 1,3%
# Recebe o valor do depósito
deposito = float(input('valor de deposito: '))
# Calcula o valor final com rendimento
valorFinal = deposito + (deposito * 0.013)
# Exibe o valor final
print('valor do deposito: ', valorFinal)