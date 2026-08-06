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

def finalizar_venda(venda_id, status):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE vendas
    SET status = ?
    WHERE id = ?
    """, (status, venda_id))

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

