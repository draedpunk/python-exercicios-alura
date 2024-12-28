# Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. Essa verificação será usada para definir ações diferentes dentro do jogo. Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.

num = int(input("Informe um número inteiro positivo --> "))

if (num % 2 == 0):
    print("O número informado é par.")
else:
    print("O número informado é ímpar.")