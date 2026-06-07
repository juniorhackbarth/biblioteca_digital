import os  # Importa a biblioteca do Python que permite trabalhar com arquivos e pastas

# Define o nome da pasta onde ficam os documentos da biblioteca
PASTA_DOCUMENTOS = "documentos"


def menu():
    
    print("\n=== Biblioteca Digital ===")  # \n pula uma linha antes de exibir
    print("1 - Listar documentos")
    print("2 - Adicionar documento")
    print("3 - Renomear documento")
    print("4 - Remover documento")
    print("5 - Sair")


while True:
    menu()  
    opcao = input("\nDigite uma opção: ")  

    if opcao == "1":
        print("\nFunção listar - em breve")  
    elif opcao == "2":
        print("\nFunção adicionar - em breve") 
    elif opcao == "3":
        print("\nFunção renomear - em breve")       
    elif opcao == "4":
        print("\nFunção remover - em breve")  
    elif opcao == "5":
        print("\nEncerrando o sistema. Até logo!")
        break  
    else:
        print("\nOpção inválida. Tente novamente.")  