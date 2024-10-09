lista_de_cadastro = []


def cadastrar_livro(titulo, autor, ano, genero):
    dict_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        'genero': genero
    }
    lista_de_cadastro.append(dict_livro)
    print("Livro cadastrado com sucesso!")


def listar_cadastro():
    print("LISTA DE LIVROS")
    print("************************")
    for livro in lista_de_cadastro:
        print(f"Livro: {livro['titulo']}")


def buscar_livro(titulo):
    for livro in lista_de_cadastro:
        if livro['titulo'].lower() == titulo.lower():
            return livro
    return None


while True:

    print("************************")
    print("BIBLIOTECA")
    print("************************")
    print("1 - Cadastrar um livro")
    print("2 - Listar livros cadastrados")
    print("3 - buscar livro pelo nome")
    print("0 - Encerrar")

    opcao = int(input("Entre com a opção de escolha: "))

    if (opcao == 0):
        print("Sistema Encerrado!")
        break
    elif (opcao == 1):
        titulo = input("Título da obra: ")
        autor = input("Autor da obra: ")
        ano = input("Ano da publicação: ")
        genero = input("Genero: ")
        cadastrar_livro(titulo, autor, ano, genero)
    elif (opcao == 2):
        listar_cadastro()
    elif (opcao == 3):
        titulo_busca = input("Entre com o nome da obra: ")
        livro_encontrado = buscar_livro(titulo_busca)
        if livro_encontrado:
            print("\nLivro disponivel!\n")
        else:
            print("\nLivro não disponivél!\n")
