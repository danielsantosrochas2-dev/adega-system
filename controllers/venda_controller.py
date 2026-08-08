from repositories.venda_repository import nova_venda, adicionar_item_na_venda, busca_venda_id, cancelar_venda, finalizar_venda, remover_item_da_venda, atualizar_valor_total_venda, buscar_itens_venda, busca_produto_unico, busca_quantidade_produto
from repositories.movimentacao_repository import registro_saida_estoque, registro_entrada_estoque
from repositories.produto_repository import busca_produto_id, atualizar_quantidade_estoque, consulta_estoque_pra_atualizacao
from datetime import datetime

# Abrir a venda - Iniciar o processo

def abrir_venda(usuario_id):

    data_hora = datetime.now()
    valor_total = 0
    forma_pagamento = "PENDENTE"
    status = "ABERTA"
    valor_desconto = 0

    venda_id = nova_venda(usuario_id, data_hora, valor_total, forma_pagamento, status, valor_desconto)

    return venda_id

# Adicionar produto na venda - validação

def adicionar_produto_na_venda(usuario_id, venda_id, produto_id, quantidade, tipo_item, desconto):


    produto = busca_produto_id(produto_id)

    if not produto:
        return "Produto não encontrado"

    if produto[14] == 0:
        return "Produto desativado"

    if produto[7] < quantidade:
        return "Quantidade maior que o estoque do produto"

    if desconto < 0:
        return "Desconto inválido"

    preco = produto[6]

    if desconto > (preco * quantidade):
        return"Desconto maior que o valor do produto"
    
    subtotal = (preco * quantidade)
    motivo = "SAIDA"
    data_hora = datetime.now()
    adicionar_item_na_venda(venda_id, produto_id, quantidade, preco, subtotal, tipo_item, desconto)
    estoque_atual = consulta_estoque_pra_atualizacao(produto_id)[0]
    estoque_novo = estoque_atual - quantidade
    atualizar_quantidade_estoque(produto_id, estoque_novo)
    registro_saida_estoque(produto_id, usuario_id, quantidade, motivo, data_hora, venda_id)

    total = calcular_total_venda(venda_id)
    desconto_total = calcular_desconto_total_venda(venda_id)
    valor_final = total - desconto_total

    atualizar_valor_total_venda(
    venda_id,
    valor_final,
    desconto_total
    )

    return "Produto adicionado na venda"

# Calcular total_venda

def calcular_total_venda(venda_id):

    itens = buscar_itens_venda(venda_id)

    total = 0

    for item in itens:
        total += item[5]

    return total

# calcular desconto total venda

def calcular_desconto_total_venda(venda_id):

    itens = buscar_itens_venda(venda_id)

    desconto = 0

    for item in itens:
        desconto += item[7]

    return desconto

# Remover produto

def remover_produto(venda_id, usuario_id):

    item_venda_id = buscar_itens_venda(venda_id)

    if not item_venda_id:
        return "Produto não localizado"

    data_hora = datetime.now()
    item = busca_produto_unico(venda_id)[0]
    estoque = busca_quantidade_produto(venda_id)[0]
    estoque_atual = consulta_estoque_pra_atualizacao(item)[0]
    estoque_atualizado = estoque + estoque_atual

    remover_item_da_venda(item, venda_id)
    atualizar_quantidade_estoque(item, estoque_atualizado)
    registro_entrada_estoque(item, usuario_id, estoque, "Entrada - Cancelamento Item", data_hora)
    total = calcular_total_venda(venda_id)
    desconto = calcular_desconto_total_venda(venda_id)
    atualizar_valor_total_venda(
        venda_id,
        total,
        desconto
    )

    return "Produto cancelado!"

# Finalizar venda

def finalizar_venda_control(venda_id, forma_pagamento):

    venda_fim = busca_venda_id(venda_id)
    status_venda = venda_fim[5]

    if venda_fim is None:
        return "Venda não localizada"

    status_venda = venda_fim[5]

    if status_venda == "CANCELADA":
        return "Não pode finalizar venda Cancelada"

    status = "FECHADA"

    finalizar_venda(venda_id, status, forma_pagamento)

    return "Venda Finalizada!"

# Cancelar venda 

def cancelar_venda_control(venda_id, usuario_id):

    venda_cancelar = busca_venda_id(venda_id)

    if venda_cancelar is None:
        return "Venda não localizada"

    verificar_status = venda_cancelar[5]

    if verificar_status == "CANCELADA":
        return "Venda já se encontra Cancelada"


    produto = buscar_itens_venda(venda_cancelar[0])
    data_hora = datetime.now()

    for produtos in produto:
        produto_atualizar = produtos[2]
        estoque_atual = consulta_estoque_pra_atualizacao(produto_atualizar)[0]
        estoque = produtos[3] + estoque_atual
        atualizar_quantidade_estoque(produto_atualizar, estoque)
        registro_entrada_estoque(produto_atualizar, usuario_id, produtos[3], "Entrada - Cancelamento", data_hora, venda_cancelar[0])

    cancelar_venda(venda_cancelar[0])
    return True



