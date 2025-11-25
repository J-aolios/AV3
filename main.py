import getpass

from services.user_services import insert_user, login_user
from services.admin_services import login_admin
from view.admin_view import admin_panel
from view.user_view import user_panel
painel = 0

while painel == 0:
   print("1 - Entrar como Administrador \n2 - Entrar como Usuário \n3 - Sair")
   entrar = int(input("Digite a opção: "))

   if entrar == 1:     
      admin_nome = input("Insira seu nome: ")
      admin_password = getpass.getpass("Insira sua senha: ")
      admin_auth = login_admin(admin_nome, admin_password)
      if admin_auth:
         admin_panel(admin_auth)
      else: print("Nome ou senha inválidos!")
   elif entrar == 2:
      conta = input("Você possui uma conta? Sim ou Não?\n").capitalize()     
      if conta == "Sim":
        user_nome = insert_user(user_nome)
        user_cpf = insert_user(user_cpf)       
        user_email = input("Digite seu e-mail: ")
        user_password = getpass.getpass("Digite sua senha: ")
        user_auth = login_user(user_email, user_password)
        if user_auth:
            user_panel(user_auth)
        else:
            print("Email ou senha inválidos!")
      elif conta == "Não":
        insert_user(user_nome, user_email, user_cpf, user_password)  
   elif entrar == 3:
        painel += 1
        break 
   else:
        print("Digite uma opção válida")
