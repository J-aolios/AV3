from config.db import criar_conexao

def create_ticket():
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "SELECT i.*, f.* FILM Ingressos i JOIN filme f on i.id_filme = f.id"
    cursor.execute(sql)
    ingressos = cursor.fetchall()
    return ingressos
