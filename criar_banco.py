import sqlite3

conexao = sqlite3.connect("database/vitasync.db")
conexao.execute("PRAGMA foreign_keys = ON")
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
cursor.execute("""
CREATE TABLE IF NOT EXISTS SESSAO_ESTUDO (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    materia TEXT NOT NULL,
    duracao INTEGER NOT NULL,
    xp INTEGER NOT NULL,
    data_registro TEXT,
    FOREIGN KEY (usuario_id) REFERENCES USUARIO (id)
)
""")


conexao.commit()

conexao.close()

print("Banco de dados e tabela USUARIO criados com sucesso!")