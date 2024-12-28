# Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

gastos_mes = float(input("Informe os gastos deste mês --> R$ "))

if (gastos_mes < 3000):
    print("O valor gasto neste mês ainda está dentro do orçamento.")
else: 
    print("ATENÇÃO: Você ultrapassou o limite do orçamento!")