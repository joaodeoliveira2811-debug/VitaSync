import sqlite3

conexao = sqlite3.connect("database/vitasync.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS USUARIO (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    nivel INTEGER DEFAULT 1,
    xp INTEGER DEFAULT 0,
    data_cadastro TEXT
)
""")

conexao.commit()

conexao.close()

print("Banco de dados e tabela USUARIO criados com sucesso!")