# Este programa troca os valores de X e Y
# Recebe o valor de X
X = float(input('Insira de X:'))
# Recebe o valor de Y
Y = float(input('Insira de Y: '))
# Cria variável temporária
temp = None
# Exibe valores antes da troca
print('valor de X antes: ',X)
print('valor de Y antes: ', Y)
# Troca os valores
temp = X
X = Y
Y = temp
# Exibe valores após a troca
print('valor de X: ',X)
print('valor de Y: ', Y)