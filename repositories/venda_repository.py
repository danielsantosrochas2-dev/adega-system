from database.conexao import conectar

# Criar venda, chama a tabela vendas

def nova_venda(usuario_id, data_hora, valor_total, forma_pagamento, status, valor_desconto):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO vendas (usuario_id, data_hora, valor_total, forma_pagamento, status, valor_desconto)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (usuario_id, data_hora, valor_total, forma_pagamento, status, valor_desconto,))

    conexao.commit()

    venda_id = cursor.lastrowid

    conexao.close()

    return venda_id

# Adicionar item na venda chama a tabela iten_venda

def adicionar_item_na_venda(venda_id, produto_id, quantidade, preco_unitario, subtotal, tipo_item, desconto):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario, subtotal, tipo_item, desconto)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (venda_id, produto_id, quantidade, preco_unitario, subtotal, tipo_item, desconto))

    conexao.commit()

    item_venda_id = cursor.lastrowid

    conexao.close()

    return item_venda_id

# Remover item da venda 

def remover_item_da_venda(item_venda_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM itens_venda
    WHERE id = ?
    """, (item_venda_id,))


    conexao.commit()

    apagou = cursor.rowcount > 0

    conexao.close()

    return apagou

# Finalizar a venda

def finalizar_venda(venda_id, status, forma_pagamento):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE vendas
    SET status = ?,
     forma_pagamento = ?
    WHERE id = ?
    """, (status, forma_pagamento, venda_id))

    conexao.commit()
    conexao.close ()

    return True

# Cancelar Venda

def cancelar_venda(venda_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE vendas
    SET status = ?
    WHERE id = ?
    """, ("Cancelada", venda_id))

    conexao.commit()
    conexao.close ()

    return True

# Buscar venda por ID

def busca_venda_id(venda_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM vendas
    WHERE id = ?
    """, (venda_id,))

    venda = cursor.fetchone()
    conexao.close()

    return venda

# Listar Vendas

def listar_vendas():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM vendas
    ORDER BY data_hora 
    """)

    lista_vendas = cursor.fetchall()
    conexao.close()

    return lista_vendas

# Busca de vendas por usuario

def busca_vendas_por_usuario(usuario_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM  vendas
    WHERE usuario_id = ?
    ORDER BY data_hora
    """, (usuario_id,))

    vendas = cursor.fetchall()
    conexao.close()

    return vendas

# Busca de vendas por periodo

def busca_vendas_periodo(data_inicial, data_final):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM vendas
    WHERE data_hora BETWEEN ? AND ?
    ORDER BY data_hora DESC
    """, (data_inicial, data_final,))

    vendas_periodo = cursor.fetchall()
    conexao.close()

    return vendas_periodo

# Atualizar valor total da venda

def atualizar_valor_total_venda(venda_id, valor_total, valor_desconto):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE vendas
    SET valor_total = ?,
    valor_desconto = ?
    WHERE id = ?
    """, (valor_total, valor_desconto, venda_id))

    conexao.commit()
    conexao.close()

    return True

# Buscar itens venda na tabela - Itens_venda

def buscar_itens_venda(venda_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM itens_venda
    WHERE venda_id = ?
    """, (venda_id,))

    itens = cursor.fetchall()
    conexao.close()

    return itens