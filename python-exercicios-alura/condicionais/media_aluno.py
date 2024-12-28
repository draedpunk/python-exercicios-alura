# Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado
# Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

um = float(input("Informe a primeira nota --> "))
dois = float(input("Informe a segunda nota --> "))
tres = float(input("Informe a terceira nota --> "))

media = (um + dois + tres)/3

print("A sua média é: ", media)

if (media >=7):
    print("Você está aprovado.")
elif (5 <= media < 7):
    print("Você está em recuperação.")
else: 
    print("Você está reprovado.")