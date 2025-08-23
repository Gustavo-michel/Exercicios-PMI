alimento_kg = float(input("Quantidade de alimento (kg): "))

alimento_g = alimento_kg * 1000

consumo_diario = 50

dias = alimento_g // consumo_diario
print(f"O alimento durará {int(dias)} dias.")
