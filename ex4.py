print("\nBem-vindo à livraria do Lucas Sanchez Vicente!")

lista_livro = []
id_global = 0

# função de cadastro de livros
def cadastrar_livro(id):
    print("\nCADASTRO DE LIVRO")
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    livro = {"id": id, "nome": nome, "autor": autor.lower(), "editora": editora}
    lista_livro.append(livro)
    print(f"Livro de ID {id} cadastrado com sucesso!")

# função para consultar livros
def consultar_livro():
    while True:
        print("\nMENU CONSULTAR LIVRO")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar por ID")
        print("3 - Consultar por Autor")
        print("4 - Retornar ao Menu Principal")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                if not lista_livro:
                    print("Nenhum livro cadastrado.")
                for livro in lista_livro:
                    print(f"\nID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
            elif opcao == 2:
                id_pesquisa = int(input("Digite o ID do livro que deseja consultar: "))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_pesquisa:
                        print(f"\nID: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}")
                        encontrado = True
                if not encontrado:
                    print("Livro com esse ID não encontrado.")
            elif opcao == 3:
                autor_busca = input("Digite o nome do autor: ").lower()
                encontrados = [livro for livro in lista_livro if livro['autor'] == autor_busca]
                if encontrados:
                    print(f"\nLivros encontrados do autor {autor_busca}:")
                    for livro in encontrados:
                        print(f"\nID: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Editora: {livro['editora']}")
                else:
                    print(f"Não há livros cadastrados do autor {autor_busca}.")
            elif opcao == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Digite apenas números válidos.")

# função para remover livro
def remover_livro():
    while True:
        try:
            id_remover = int(input("Digite o ID do livro que deseja remover: "))
            for livro in lista_livro:
                if livro["id"] == id_remover:
                    lista_livro.remove(livro)
                    print(f"Livro de ID {id_remover} removido com sucesso.")
                    return
            print("ID inválido. Tente novamente.")
        except ValueError:
            print("Digite apenas números válidos.")

# Estrutura principal (main)
while True:
    print("\nMENU PRINCIPAL")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Encerrar Programa")
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            id_global += 1
            cadastrar_livro(id_global)
        elif escolha == 2:
            consultar_livro()
        elif escolha == 3:
            remover_livro()
        elif escolha == 4:
            print("Encerrando o programa. Obrigado por usar o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Digite apenas números válidos.")