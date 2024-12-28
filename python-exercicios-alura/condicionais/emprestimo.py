# Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

# O valor da renda mensal precisa ser maior que R$ 2.000,00.
# O valor da parcela não pode ultrapassar 30% da renda.
# Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

renda = float(input("Informe o valor da renda mensal --> R$ "))
parcela = int(input("Informe o valor da parcela --> "))

parcela_maxima = 600.00

if (renda < 2000):
    print("\nEmpréstimo negado!")
    print("O valor da renda mensal não atende ao valor mínimo de R$ 2 000,00.")
if (parcela > parcela_maxima):
    print("\nEmpréstimo negado!")
    print("O valor da parcela não pode ultrapassar 30% da renda.")
else:
    print("Empréstimo aprovado!")


