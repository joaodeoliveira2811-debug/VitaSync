import sqlite3

conexao = sqlite3.connect("database/vitasync.db")
conexao.execute("PRAGMA foreign_keys = ON")
cursor = conexao.cursor()

cursor.execute("""
INSERT INTO SESSAO_ESTUDO (usuario_id, materia, duracao, xp)
VALUES (?, ?, ?, ?)
""", (1, "Python", 50, 50))

conexao.commit()
conexao.close()

print("Sessão inserida com sucesso!")