# Este programa calcula a idade futura do usuário
# Recebe o ano de nascimento
ano_nascimento = int(input("Digite o ano de nascimento: "))
# Recebe o ano atual
ano_atual = int(input("Digite o ano atual: "))
# Calcula a idade atual
idade_atual = ano_atual - ano_nascimento
# Calcula a idade daqui a 17 anos
idade_futura = idade_atual + 17
# Exibe a idade futura
print(f"Daqui a 17 anos você terá: {idade_futura} anos")