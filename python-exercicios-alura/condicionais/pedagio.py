# Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

# Até 100 km: R$ 10,00
# Entre 100 km e 200 km: R$ 20,00
# Acima de 200 km: R$ 30,00
# Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.

d = float("Informe a distância percorrida (km) --> ")

if (d < 100):
    print("Valor do pedágio: R$ 10.00")
elif (100 <= d < 200):
    print("Valor do pedágio: R$ 20.00")
else:
    print("Valor do pedágio: R$ 30.00")