# José está desenvolvendo uma funcionalidade no sistema do Buscante para interromper a busca assim que um livro específico é encontrado.
# Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>" assim que o livro "O Hobbit" for encontrado. Após encontrar o livro, o programa deve parar imediatamente a busca, sem verificar os livros restantes.

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if (livro == "O Hobbit"):
        print("Livro encontrado: O Hobbit")
        break
    print(livro)