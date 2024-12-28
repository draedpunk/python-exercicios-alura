# Mesma questão, mas agora usando o método reduce()
# reduce(function, collection)

from functools import reduce

valores = [10, 20, 30, 40, 50]
soma_total = reduce(lambda a, b: a + b, valores)

print("A soma total das receitas é de: R$",soma_total)


