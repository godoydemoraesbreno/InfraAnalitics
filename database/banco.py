import sqlite3

# funcao que cria tabela (exportada para o script.py)
def criar_tabela():
    conexao = sqlite3.connect("database/banco.db")
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS historico_redes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        ip TEXT NOT NULL,
        status TEXT NOT NULL,
        horario DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

    conexao.commit()
    conexao.close()

