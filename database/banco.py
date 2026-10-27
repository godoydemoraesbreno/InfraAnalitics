import os
import sqlite3

# descobrir onde a pasta está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# junta a pasta com o nome do arquivo
DB_PATH = os.path.join(BASE_DIR, "banco.db")

#criar tabela se ja nao existir
def criar_tabela():
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS historico_redes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        ip TEXT NOT NULL,
        status TEXT NOT NULL,
        horario DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

    conexao.commit()
    conexao.close()

