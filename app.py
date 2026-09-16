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

menu_lateral = [
    {
        "id": 1,
        "nome": "Agenda",
        "rota": "/agenda",
        "ativo": False
    },
    {
        "id": 2,
        "nome": "Sessões de Estudos",
        "rota": "/sessoes",
        "ativo": True
    }
]

# ==========================================
# 2. A LÓGICA DE NEGÓCIO (Seu algoritmo)
# ==========================================
def obter_rota_ativa(menu):
    for item in menu:
        pass # Remova este 'pass' e coloque a SUA TAREFA AQUI: 
        # Escreva o 'if' para verificar se item["ativo"] == True.
        # Se for, dê um return em item["rota"].
            
    return None # Retorna vazio se nada for encontrado

# ==========================================
# 3. AS ROTAS (Conectando Python ao HTML)
# ==========================================
@app.route('/')
def index():
    # Usamos a sua função para descobrir a rota ativa:
    rota_atual = obter_rota_ativa(menu_lateral)
    
    # Imprime no terminal só para você confirmar que sua lógica funcionou!
    print(f"Log de Dados: A rota ativa é {rota_atual}") 
    
    # Aqui a mágica acontece: mandamos a variável 'menu_lateral' lá pro index.html
    return render_template('index.html', menu=menu_lateral)

if __name__ == '__main__':
    app.run(debug=True)
