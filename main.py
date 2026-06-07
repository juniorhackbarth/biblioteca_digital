import os  # Importa a biblioteca do Python que permite trabalhar com arquivos e pastas
import shutil  # Biblioteca para copiar arquivos de uma pasta para outra

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


def adicionar_documento():
    # Função que copia um arquivo de qualquer lugar do computador para a pasta documentos
    print("\n=== Adicionar Documento ===")

    caminho = input("Digite o caminho completo do arquivo: ")  # Usuário informa onde está o arquivo

    if os.path.isfile(caminho):  # Verifica se o arquivo realmente existe
        nome_arquivo = os.path.basename(caminho)  # Pega só o nome do arquivo, sem o caminho
        destino = os.path.join(PASTA_DOCUMENTOS, nome_arquivo)  # Define onde o arquivo vai ser salvo
        shutil.copy(caminho, destino)  # Copia o arquivo para a pasta documentos
        print(f"\nArquivo '{nome_arquivo}' adicionado com sucesso!")
    else:
        print("\nArquivo não encontrado. Verifique o caminho informado.")


def renomear_documento():
    # Função que renomeia um arquivo dentro da pasta documentos
    print("\n=== Renomear Documento ===")

    listar_documentos()  # Mostra os arquivos disponíveis para o usuário escolher

    nome_atual = input("\nDigite o nome atual do arquivo: ")  # Usuário informa o nome atual
    caminho_atual = os.path.join(PASTA_DOCUMENTOS, nome_atual)  # Monta o caminho completo do arquivo

    if os.path.isfile(caminho_atual):  # Verifica se o arquivo existe na pasta
        novo_nome = input("Digite o novo nome do arquivo: ")  # Usuário informa o novo nome
        caminho_novo = os.path.join(PASTA_DOCUMENTOS, novo_nome)  # Monta o caminho com o novo nome
        os.rename(caminho_atual, caminho_novo)  # Renomeia o arquivo
        print(f"\nArquivo renomeado para '{novo_nome}' com sucesso!")
    else:
        print("\nArquivo não encontrado. Verifique o nome informado.")


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
        adicionar_documento()  # Chama a função de adicionar
    elif opcao == "3":
        renomear_documento()  # Chama a função de renomear
    elif opcao == "4":
        print("\nFunção remover - em breve")
    elif opcao == "5":
        print("\nEncerrando o sistema. Até logo!")
        break  # break encerra o loop e fecha o programa
    else:
        print("\nOpção inválida. Tente novamente.")  # Caso o usuário digite algo que não existe no menu