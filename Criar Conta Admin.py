import getpass

from config.db import criar_conexao
from services.admin_services import insert_admin
from services.admin_services import delete_admin

print("1 - Criar Novo Admin \n2 - Deletar Admin")
opcao = int(input("Digite a opção: "))
if opcao == 1:
    admin_nome = input("Insira seu nome: ")
    admin_email = input("Insira seu e-mail: ")
    admin_password = input("Insira sua senha: ")
    insert_admin(admin_nome, admin_email, admin_password)
elif opcao == 2:
    admin_email = input("Digite o e-mail do usuário a ser deletado: ")
    admin_cpf = input("Insira o CPF do usuário a ser deletado: ")
    admin_password = getpass.getpass("Digite a senha para confirmar: ")
    delete_admin(admin_email, admin_password)
