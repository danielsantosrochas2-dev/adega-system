from database.conexao import conectar

def buscar_usuario(usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    conexao.close()

    return usuarios

def validar_login(usuario, senha):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * 
         FROM usuarios
         WHERE usuario = ?
         AND senha = ?
         AND ativo = 1
         """,
        (usuario, senha)
        )

    usuario_encontrado = cursor.fetchone()
    
    conexao.close()

    return usuario_encontrado

# Retorna o login de todos os usuários ativos do sistema.

def listar_usuarios():

    conexao =  conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT usuario
    FROM usuarios
    WHERE ativo = 1
    ORDER BY usuario""")

    lista_de_usuarios = cursor.fetchall()

    conexao.close()

    return lista_de_usuarios

# Cadastro de usuario no banco 

def cadastro_usuario(usuario, nome, senha, perfil):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO usuarios (usuario, nome, senha, perfil)
    VALUES (?, ?, ?, ?)
    """, (usuario, nome, senha, perfil))

    conexao.commit()
    conexao.close()

    return True

# Atualizar dados do usuario

def editar_usuario(id, usuario, nome, senha, perfil):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE usuarios 
    SET usuario = ?, nome = ?, senha = ?, perfil = ?
    WHERE id = ?""", (usuario, nome, senha, perfil, id))

    conexao.commit()
    conexao.close()

    return True

# Desativar usuario

def alterar_status_usuario(id, ativo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(""" UPDATE USUARIOS
     SET ativo = ?
     WHERE id =? """, (ativo, id))

    conexao.commit()
    conexao.close()

    return True

# Busca de usuario por id

def busca_usuario_id(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE id = ?
    """, (id))

    usuario = cursor.fetchone()
    cursor.close()

    return usuario
