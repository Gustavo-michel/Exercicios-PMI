# Este programa calcula quantos dias o alimento irá durar
# Recebe a quantidade de alimento em kg
alimento_kg = float(input("Quantidade de alimento (kg): "))
# Calcula a quantidade de dias (considerando 50g por dia)
dias = (alimento_kg * 1000) // 50
# Exibe o resultado
print(f"O alimento durará {int(dias)} dias.")
