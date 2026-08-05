from database.conexao import conectar

# Criar venda

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

# Adicionar item a venda