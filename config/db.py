import psycopg2

def criar_conexao():
    try:
        conn = psycopg2.connect(
           dbname='Cinema',
           user='postgres',
           password= 'Postgre_SQL',
           host= 'localhost',
           port= '5432'
        )
        # print("Conexão bem-sucedida ao banco de dados.")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")