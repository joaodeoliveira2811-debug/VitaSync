import sqlite3

conexao = sqlite3.connect("database/vitasync.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM USUARIO")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]} | Nivel: {usuario[4]} | XP: {usuario[5]} ")

conexao.close()