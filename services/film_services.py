from config.db import criar_conexao

def create_films(title, genero, indicacao, duracao, id_film):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO films (title, genero, indicacao, duracao, id_film) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (title, genero, indicacao, duracao, id_film))
    conn.commit()
    print("Filme cadastrado!")

def list_films(id_film):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "SELECT * FROM films WHERE id_film = %s"
    cursor.execute(sql, [id_film])
    films = cursor.fetchall()
    return films

def delete_films(id_film):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "DELETE FROM films WHERE id_film=%s AND id=%s"
    cursor.execute(sql, [id_film])
    conn.commit()
    print("Filme Removido!")

def update_films(id_film, title, genre, indication, duration):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "UPDATE films SET title=%s WHERE id_film=%s AND id=%s"
    print("Filme atualizado!")
    cursor.execute(sql, [id_film, title, genre, indication, duration])
    conn.commit()