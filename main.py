import getpass
import os

from services.user_services import insert_user, login
from view.admin_view import panel

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("1 - Criar Novo Usuário \n2 - Entrar \n3 - Sair do Sistema")
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        email = input("Digite seu e-mail: ")
        password = input("Digite sua senha: ")
        insert_user(email, password)
    elif opcao == 2:
        email = input("Digite seu e-mail: ")
        password = getpass.getpass("Digite sua senha: ")
        user_auth = login(email, password)
        if user_auth:
            panel(user_auth)
        else:
            print("Usuário ou senha inválidos!")
    elif opcao == 3:
        break
    else:
        print("Digite uma opção válida")
