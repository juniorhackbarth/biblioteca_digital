import os  # Importa a biblioteca 
import shutil  # Biblioteca para copiar arquivos de uma pasta para outra

PASTA_DOCUMENTOS = "documentos"


def listar_documentos():
    # Função que lista todos os arquivos da pasta documentos
    print("\n=== Documentos da Biblioteca ===")

    arquivos = os.listdir(PASTA_DOCUMENTOS) 

    if len(arquivos) == 0:  
        print("Nenhum documento encontrado.")
    else:
        for i, arquivo in enumerate(arquivos, start=1):  
            print(f"{i} - {arquivo}")  # Exibe o número e o nome do arquivo


def adicionar_documento():
    # Função que copia um arquivo de qualquer lugar do computador para a pasta documentos
    print("\n=== Adicionar Documento ===")

    caminho = input("Digite o caminho completo do arquivo: ")  # Usuário informa onde está o arquivo

    if os.path.isfile(caminho):  
        nome_arquivo = os.path.basename(caminho)  # Pega só o nome do arquivo, sem o caminho
        destino = os.path.join(PASTA_DOCUMENTOS, nome_arquivo)  
        shutil.copy(caminho, destino)  
        print(f"\nArquivo '{nome_arquivo}' adicionado com sucesso!")
    else:
        print("\nArquivo não encontrado. Verifique o caminho informado.")


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
        print("\nFunção renomear - em breve")
    elif opcao == "4":
        print("\nFunção remover - em breve")
    elif opcao == "5":
        print("\nEncerrando o sistema. Até logo!")
        break  # break encerra o loop e fecha o programa
    else:
        print("\nOpção inválida. Tente novamente.")  # Caso o usuário digite algo que não existe no menu