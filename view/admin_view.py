from services.task_services import create_task

def panel(user_auth):
    while True:
        print(f"Bem vindo {user_auth[1]}")
        print("1 - Cadastrar Task \n2 - Buscar Task \n3 - Remover Task \n4 - Atualizar Task \n5 - Deslogar")

        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            title = input("Digite o título da tarefa: ")
            create_task(user_auth[0], title)
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            break
        else:
            print("Digite uma opção válida!")