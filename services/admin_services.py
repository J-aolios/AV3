# import bcrypt

from config.db import criar_conexao

def insert_admin(admin_nome: str, admin_email: str, admin_password: str):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios(admin_nome, admin_email, admin_password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (admin_nome, admin_email, admin_password))
        conn.commit()
        print("Admin cadastrado com sucesso!")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def login_admin(admin_email: str, admin_password: str):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = "SELECT * FROM admin WHERE admin_email=%s AND admin_password=%s"
        cursor.execute(sql, (admin_email, admin_password))
        user = cursor.fetchone()
        return user 
    except Exception as e:
        print(e)

def delete_admin(admin_nome, admin_email, admin_password):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = "DELETE FROM admin WHERE admin_nome=%s and admin_email=%s and admin_password=%s"
        cursor.execute(sql, [admin_nome, admin_email, admin_password])
        conn.commit()
        print("Admin Removido com Sucesso!")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
