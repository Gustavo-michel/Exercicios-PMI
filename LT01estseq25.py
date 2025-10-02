'''
Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do 
jogo  em  horas  e  minutos,  sabendo  que  o  tempo  máximo  é  menor  que  24 
horas e pode começar num dia e terminar noutro.
'''

inicio = int(input("horas de inicio: "))
final = int(input("horas final: "))

if inicio < 24 and final < 24:
    if inicio > fim:
        print("O tempo de jogo é: ", final-inicio)
    else:
        print("O tempo de jogo é: ", inicio-final)