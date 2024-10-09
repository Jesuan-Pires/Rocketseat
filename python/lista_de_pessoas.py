lista_pessoas = []

while True:
    nome = input("Entre com o seu nome ou tecle [0] para sair: ")
    if nome == '0':
        break

    idade = input("Entre com a sua idade: ")
    cpf = input("Entre com o seu CPF: ")

    dict_pessoa = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf
    }

    lista_pessoas.append(dict_pessoa)

for i in lista_pessoas:
    print(
        f"Nome: {dict_pessoa["nome"]}, Idade: {dict_pessoa["idade"]}, CPF:{dict_pessoa["cpf"]}")
