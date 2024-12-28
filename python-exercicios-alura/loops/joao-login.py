# João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

# O nome de usuário deve ter pelo menos 5 caracteres.
# A senha deve ter pelo menos 8 caracteres.
# João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

# Crie um programa que implemente essa lógica usando um laço while.

nome = input("Informe o seu nome: ")
senha = input("Informe a sua senha: ")

while len(nome) < 5 or len(senha) < 8:
    print("O NOME de usuário deve ter pelo menos 5 caracteres e a SENHA pelo menos 8 caracteres.")
    nome = input("Informe novamente o seu nome: ")
    senha = input("Informe novamente a sua senha: ")
else:
    print("Cadastro realizado com sucesso!")