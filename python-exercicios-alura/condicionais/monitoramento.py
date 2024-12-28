# Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.
# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

banana = int(input("Informe a quantidade de banana(s) vendidas --> "))
maca = int(input("Informe a quantidade de maçãs vendidas --> "))

if (banana > maca):
    print("\nA fruta mais vendida foi banana 🍌!")
elif (banana == maca):
    print("\nHouve empate entre o número de vendas das bananas e das maçãs.")
else: 
    print("\nA fruta mais vendida foi maçã 🍎!")