import sqlite3

def conectar():
    try:
        conexao = sqlite3.connect("database/adega.db")
        print("✅ Banco conectado com sucesso!")
        return conexao

    except sqlite3.Error as erro:
        print(f"Erro ao conectar ao banco: {erro}")
        return None

    