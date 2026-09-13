import sqlite3

conexao = sqlite3.connect("database/vitasync.db")
cursor = conexao.cursor()

cursor.execute("""
INSERT INTO USUARIO (nome, email, senha)
VALUES (?, ?, ?)
""", ("Vinícius", "vini@email.com", "senha123"))

conexao.commit()

conexao.close()

print("Usuário inserido com sucesso!")