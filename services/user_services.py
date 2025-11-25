import getpass
# import bcrypt

from config.db import criar_conexao

def insert_user(user_nome: str, user_email: str, user_cpf: int, user_password: str):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios(user_nome, user_email, user_cpf, user_password) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (user_nome, user_email, user_cpf, user_password))
        conn.commit()
        print("Usuário cadastrado com sucesso!")       
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def login_user(user_email: str, user_password: str):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = "SELECT * FROM usuarios WHERE user_email=%s AND user_password=%s"
        cursor.execute(sql, (user_email, user_password))
        user = cursor.fetchone()
        return user 
    except Exception as e:
        print(e)

def delete_user(user_email, user_cpf, user_password):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = "DELETE FROM usuarios WHERE user_email=%s and user_cpf=%s and user_password=%s"
        cursor.execute(sql, [user_email, user_cpf, user_password])
        conn.commit()
        print("Usuário Removido com Sucesso!")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
