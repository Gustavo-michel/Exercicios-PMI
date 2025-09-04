# Este programa calcula o salário líquido com dependentes e desconto
# Recebe a quantidade de horas trabalhadas
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
# Recebe o valor por hora
valor_hora = float(input("Digite o valor por hora: "))
# Recebe o percentual de desconto
percentual_desconto = float(input("Digite o percentual de desconto (%): "))
# Recebe o número de dependentes
num_dependentes = int(input("Digite o número de dependentes: "))
# Calcula o salário bruto
salario_bruto = horas_trabalhadas * valor_hora
# Calcula o valor do desconto
desconto = salario_bruto * (percentual_desconto / 100)
# Calcula o salário líquido
salario_liquido = salario_bruto - desconto
# Adiciona o valor dos dependentes
salario_liquido += num_dependentes * 100
# Exibe o salário a receber
print(f"Salário a receber: R$ {salario_liquido:.2f}")