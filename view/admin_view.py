from services.task_services import create_task, list_tasks, delete_task, update_task

def panel(user_auth):
    while True:
        print(f"Bem vindo {user_auth[1]}")
        print("1 - Cadastrar Task \n2 - Listar Task \n3 - Remover Task \n4 - Atualizar Task \n5 - Deslogar")

        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            title = input("Digite o título da tarefa: ")
            create_task(user_auth[0], title)
        elif opcao == 2:
            tasks = list_tasks(user_auth[0])
            for task in tasks:
                print(f"{task[0]} - {task[1]}")
        elif opcao == 3:
            id_task = int(input("Digite o id da task para removê-la: "))
            delete_task(user_auth[0], id_task)
        elif opcao == 4:
            id_task = int(input("Digite o id da task para atualizá-la: "))
            new_title = input("Digite o novo título da task: ")
            update_task(user_auth[0], id_task, new_title)
        elif opcao == 5:
            break
        else:
            print("Digite uma opção válida!")