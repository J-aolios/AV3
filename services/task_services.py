from config.db import criar_conexao

def create_task(user_id, title):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO TASKS (title, user_id) VALUES (%s, %s)"
    cursor.execute(sql, (title, user_id))
    conn.commit()
    print("Task cadastrada!")