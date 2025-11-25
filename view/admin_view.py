import getpass

from services.film_services import create_films, list_films, delete_films, update_films
from services.admin_services import insert_admin

def admin_panel(admin_auth):
    print(f"Bem vindo {admin_auth[1]}")
    while True:
        print("1 - Cadastrar Filme \n2 - Listar Filme \n3 - Remover Filme \n4 - Atualizar Filme \n5 - Deslogar")
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            title = input("Digite o título do filme: ")
            create_films(title)
        elif opcao == 2:
            films = list_films()
            for Film in films:
                print(f"{Film[0]} - {Film[1]}")
        elif opcao == 3:
            id_film = int(input("Digite o id do filme para removê-lo: "))
            admin_password = getpass.getpass("Digite sua senha para deletar esse filme: ")
            insert_admin(admin_password)
            delete_films(id_film)
        elif opcao == 4:
            id_film = int(input("Digite o id do filme para atualizá-lo: "))
            title = input("Digite o novo título do filme: ")
            genre = input("Atualize os novos gêneros do filme: ")
            indication = input("Atualize a idade indicativa: ")
            duration = input("Atualize a duração do filme: ")
            admin_password = getpass.getpass("Digite sua senha para atualizar esse filme: ")
            insert_admin(admin_password)
            update_films(id_film, title, genre, indication, duration)
        elif opcao == 5:
            break
        else:
            print("Digite uma opção válida!")
            