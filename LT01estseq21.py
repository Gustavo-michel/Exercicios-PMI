'''
Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. 
Mostre a mensagem de acordo com a média: 
a. Se a média for >= 6,0 exibir “APROVADO”; 
b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”; 
c. Se a média for < 3,0 exibir “RETIDO”.
'''

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6.0:
    print("APROVADO")
elif media >= 3.0 and media < 6.0:
    print("EXAME")
elif media < 3.0:
    print("RETIDO")