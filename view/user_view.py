import getpass

from services.film_services import list_films
from services.ticket_services import create_ticket
def user_panel(user_auth):
    print(f"Bem vindo {user_auth[1]}")
    while True:
        selecao = int(input("1 - Filmes \n2 - Data \n3 - Assento \n4 - Ingresso \n5 - Sair"))
        if selecao == 1:
            films = list_films()
            for Film in films:
                print(f"{Film[0]} - {Film[1]}")
            Ticket_ingressos = input("Qual o id do filme? ")
            continue
        elif selecao == 2:

            continue
        elif selecao == 3:
            assento = 50
            print(f"Quantidade de assentos disponíveis {assento}")
            qnt_ass = int(input("Quantos assentos gostaria de alugar?"))
            assento -= qnt_ass
            continue
        elif selecao == 4:
            ingressos = create_ticket()
            print(ingressos)
            continue
        elif selecao == 5:
            break
        else:
            print("Digite uma opção válida!")























# import getpass

# from services.user_services import insert_user, login, delete_usuario
# from view.admin_view import panel

# while True:
#     print("1 - Criar Novo Usuário \n2 - Entrar \n3 - Deletar Usuário \n4 - Sair do Sistema")
#     opcao = int(input("Digite a opção: "))

#     if opcao == 1:
#         nome = input("Insira seu nome: ")
#         email = input("Insira seu e-mail: ")
#         cpf = input("Insira seu CPF: ")
#         password = input("Insira sua senha: ")
#         telefone = input("Insira seu telefone: ")
#         insert_user(nome, email, cpf, password, telefone)
#     elif opcao == 2:
#         email = input("Digite seu e-mail: ")
#         password = getpass.getpass("Digite sua senha: ")
#         user_auth = login(email, password)
#         if user_auth:
#             panel(user_auth)
#         else:
#             print("Usuário ou senha inválidos!")
#     elif opcao == 3:
#             email = input("Digite o e-mail do usuário a ser deletado: ")
#             cpf = input("Insira o CPF do usuário a ser deletado: ")
#             password = getpass.getpass("Digite a senha para confirmar: ")
#             user_auth = delete_usuario(email, cpf, password)
#     elif opcao == 4:
#         break
#     else:
#         print("Digite uma opção válida")