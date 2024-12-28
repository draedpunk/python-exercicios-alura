# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.
# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

a = int(input("Informe os dias para a atividade A --> "))
b = int(input("Informe os dias para a atividade B --> "))
c = int(input("Informe os dias para a atividade C --> "))
tempo_total_projeto = (a+b+c)

if (a < 0 or b <0  or c < 0):
    print("ERROR: Os dias não podem ser negativos!")
else:
    print("O tempo total do projeto é de ",tempo_total_projeto," dias")