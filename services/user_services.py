from config.db import criar_conexao

def insert_user(email: str, password: str):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()

        sql = "INSERT INTO usuarios(email, password) VALUES (%s, %s)"
        cursor.execute(sql, (email, password))
        conn.commit()
        print("Usuário cadastrado com sucesso!")
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def login(email: str, password: str):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        sql = "SELECT * FROM usuarios WHERE email=%s and password=%s"
        cursor.execute(sql, (email, password))
        user = cursor.fetchone()
        return user 
    except Exception as e:
        print(e)