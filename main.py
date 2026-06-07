import os  # Importa a biblioteca do Python que permite trabalhar com arquivos e pastas

# Define o nome da pasta onde ficam os documentos da biblioteca
PASTA_DOCUMENTOS = "documentos"


def listar_documentos():
    # Função que lista todos os arquivos da pasta documentos
    print("\n=== Documentos da Biblioteca ===")

    arquivos = os.listdir(PASTA_DOCUMENTOS)  # Pega a lista de arquivos da pasta

    if len(arquivos) == 0:  # Verifica se a pasta está vazia
        print("Nenhum documento encontrado.")
    else:
        for i, arquivo in enumerate(arquivos, start=1):  # Percorre cada arquivo da lista
            print(f"{i} - {arquivo}")  # Exibe o número e o nome do arquivo


def menu():
    # Função que exibe o menu de opções na tela
    print("\n=== Biblioteca Digital ===")
    print("1 - Listar documentos")
    print("2 - Adicionar documento")
    print("3 - Renomear documento")
    print("4 - Remover documento")
    print("5 - Sair")


# while True significa: repete o programa infinitamente até o usuário escolher sair
while True:
    menu()  # Chama a função menu para exibir as opções
    opcao = input("\nDigite uma opção: ")  # Aguarda o usuário digitar algo

    if opcao == "1":
        listar_documentos()  # Chama a função de listar
    elif opcao == "2":
        print("\nFunção adicionar - em breve")
    elif opcao == "3":
        print("\nFunção renomear - em breve")
    elif opcao == "4":
        print("\nFunção remover - em breve")
    elif opcao == "5":
        print("\nEncerrando o sistema. Até logo!")
        break  # break encerra o loop e fecha o programa
    else:
        print("\nOpção inválida. Tente novamente.")  # Caso o usuário digite algo que não existe no menu