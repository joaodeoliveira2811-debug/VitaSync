from flask import Flask, render_template
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "vitasync.db")

app = Flask(__name__)

@app.route("/")
def home():
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, nivel, xp FROM USUARIO WHERE id = 1")
    usuario = cursor.fetchone()
    conexao.close()

    if usuario is None:
        return "Nenhum usuário encontrado. Por favor, cadastre-se primeiro."

    sessoes = [
        {"materia": "Python", "duracao": 50},
        {"materia": "Banco de Dados", "duracao": 30},
        {"materia": "Python", "duracao": 45},
    ]

    return render_template("index.html", nome=usuario[0], nivel=usuario[1], xp=usuario[2], sessoes=sessoes)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)