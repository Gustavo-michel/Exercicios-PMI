X = float(input('Insira de X:'))
Y = float(input('Insira de Y: '))
temp = None

print('valor de X antes: ',X)
print('valor de Y antes: ', Y)

temp = X
X = Y
Y = temp

print('valor de X: ',X)
print('valor de Y: ', Y)