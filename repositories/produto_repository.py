from database.conexao import conectar

# Cadastrar Produto no banco de dados

def cadastrar_produto(nome, categoria_id, codigo_interno, codigo_barras, preco_compra, preco_venda, estoque, estoque_minimo, controla_dose, doses_por_unidade, controla_validade, data_validade):

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO produtos (nome, categoria_id, codigo_interno, codigo_barras, preco_compra, preco_venda, estoque, estoque_minimo, controla_dose, doses_por_unidade, controla_validade, data_validade, ativo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
        """, (nome, categoria_id, codigo_interno, codigo_barras, preco_compra, preco_venda, estoque, estoque_minimo, controla_dose, doses_por_unidade, controla_validade, data_validade))
        conexao.commit()
        return True

    except Exception as erro:
        print(erro)
        return False

    finally:
        if conexao:
            conexao.close()

# Buscar produto por id

def busca_produto_id(id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM produtos
    WHERE id = ?
    """, (id,))

    produto = cursor.fetchone()
    conexao.close()

    return produto

# Buscar produto por nome

def busca_produto_nome(nome):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM produtos
    WHERE nome LIKE ?
    AND ativo = 1
    """, (f"%{nome}%",))

    produtos = cursor.fetchall()
    conexao.close()

    return produtos

# Listar Produtos Ativos

def listar_produtos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT id, nome, codigo_interno, preco_venda, estoque FROM produtos
    WHERE ativo = 1
    ORDER BY nome
    """)

    lista_produtos = cursor.fetchall()
    conexao.close()

    return lista_produtos

# Atualizar produto

def atualizar_produto(id, nome, categoria_id, codigo_interno, codigo_barras, preco_compra, preco_venda, controla_dose, doses_por_unidade, controla_validade, data_validade):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE produtos
    SET nome = ?, categoria_id = ?, codigo_interno = ?, codigo_barras = ?, preco_compra = ?, preco_venda = ?, controla_dose = ?, doses_por_unidade = ?, controla_validade = ?, data_validade = ?
    WHERE id = ?
    """,(nome, categoria_id, codigo_interno, codigo_barras, preco_compra, preco_venda, controla_dose, doses_por_unidade, controla_validade, data_validade, id))

    conexao.commit()
    conexao.close()

    return True

# Desativar produto

def alterar_status_produto(id, ativo):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE produtos
    SET ativo = ?
    WHERE ID = ?
    """, (ativo, id))

    conexao.commit()
    conexao.close()

    return True

# Atualizar estoque quantidade e quantida de minima

def atualizar_estoque(id, estoque, estoque_minimo):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE produtos
    SET estoque = ?, estoque_minimo = ?
    WHERE id = ? AND ativo = 1
    """, (estoque, estoque_minimo, id))

    conexao.commit()
    conexao.close()

    return True

# Buscar produtos com estoque baixo

def busca_produtos_baixo():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT nome, categoria_id, estoque, estoque_minimo
    FROM produtos
    WHERE estoque <= estoque_minimo
    """)

    quantidade_produto_baixo = cursor.fetchall()

    conexao.close()

    return quantidade_produto_baixo

# Buscar Produtos proximos e Vencidos

def busca_produtos_proximo_vencidos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT nome, categoria_id, estoque, data_validade
    FROM produtos
    WHERE data_validade <= date('now', '+30 days')
    AND data_validade >= date('now')
    """)

    produtos = cursor.fetchall()
    conexao.close()

    return produtos






