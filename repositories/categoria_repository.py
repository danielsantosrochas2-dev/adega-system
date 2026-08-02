from database.conexao import conectar

# Cadastrar Categoria

def cadastrar_categoria(nome):

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO categorias (nome)
        VALUES (?)
        """, (nome))
        conexao.commit()
        return True

    except Exception as erro:
        print(erro)
        return False

    finally:
        if conexao:
            conexao.close()

# Busca de categoria por ID

def busca_categoria_id(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *
    FROM categorias
    WHERE id = ?
    """, (id,))

    categoria = cursor.fetchone()
    conexao.close()

    return categoria

# Busca categoria por nome

def busca_categoria_nome(nome):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *
    FROM categorias
    WHERE nome = ?
    """, (nome,))

    categoria = cursor.fetchone()
    conexao.close()

    return categoria

# Listar todas categorias

def listar_todas_categorias():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *
    FROM categorias
    ORDER BY nome
    """)

    categorias = cursor.fetchall()
    conexao.close()

    return categorias

# Atualizar nome da categoria

def atualizar_nome_categoria(nome, id):

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
        UPDATE categorias
        SET nome = ?
        WHERE id = ?
        """,(nome, id))
        conexao.commit()
        return True

    except Exception as erro:
        print(erro)
        return False

    finally:
        if conexao:
            conexao.close()


