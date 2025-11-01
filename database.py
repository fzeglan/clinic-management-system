import psycopg2
from contextlib import contextmanager

@contextmanager
def get_cursor():
    conexao = psycopg2.connect(
        host="localhost",
        dbname="clinica_db",
        user="usuario",
        password="senha_do_banco",
        port="5432"
    )
    cursor = conexao.cursor()
    try:
        yield cursor
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print(f" Erro no banco: {e}")
    finally:
        cursor.close()
        conexao.close()

