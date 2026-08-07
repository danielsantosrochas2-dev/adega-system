from repositories.venda_repository import nova_venda, adicionar_item_na_venda, busca_venda_id, cancelar_venda, finalizar_venda, remover_item_da_venda, atualizar_valor_total_venda, buscar_itens_venda
from repositories.movimentacao_repository import registro_saida_estoque
from repositories.produto_repository import busca_produto_id, atualizar_quantidade_estoque
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
    
    subtotal = (preco * quantidade) - desconto
    motivo = "SAIDA"
    data_hora = datetime.now()
    adicionar_item_na_venda(venda_id, produto_id, quantidade, preco, subtotal, tipo_item, desconto)
    atualizar_quantidade_estoque(produto_id, quantidade)
    registro_saida_estoque(produto_id, usuario_id, quantidade, motivo, data_hora, venda_id)

    total = calcular_total_venda(venda_id)
    desconto_total = calcular_desconto_total_venda(venda_id)

    atualizar_valor_total_venda(
    venda_id,
    total,
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
