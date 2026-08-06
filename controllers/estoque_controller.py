from repositories.movimentacao_repository import busca_movimentacao_periodo
from repositories.movimentacao_repository import busca_movimentacao_produto
from repositories.movimentacao_repository import listar_movimentacoes_gerais
from repositories.movimentacao_repository import registro_ajuste_estoque
from repositories.movimentacao_repository import registro_entrada_estoque
from repositories.movimentacao_repository import registro_saida_estoque
from repositories.produto_repository import busca_produto_id
from repositories.usuario_repository import busca_usuario_id
from repositories.produto_repository import atualizar_estoque
from repositories.produto_repository import consulta_estoque_pra_atualizacao
from repositories.produto_repository import atualizar_quantidade_estoque
from repositories.produto_repository import busca_produtos_baixo
from repositories.produto_repository import busca_produtos_proximo_vencidos

# Validar entrada de estoque

def validar_entrada_estoque(produto_id, usuario_id, quantidade, motivo):

    produto = busca_produto_id(produto_id)
    usuario = busca_usuario_id(usuario_id)

    if produto is None:
        return "Produto não localizado"

    if usuario is None:
        return "Usuario não localizado"

    if quantidade <= 0:
        return "Quantidade tem que ser maior que zero"

    if not motivo:
        return "Motivo obrigatório"

    resultado_atualizacao = atualizar_quantidade_produto(produto_id, quantidade, "entrada")

    if not resultado_atualizacao:
        return "Erro ao atualizar estoque"
    
    resultado_movimentacao = registro_entrada_estoque(produto_id, usuario_id, quantidade, motivo)

    if not resultado_movimentacao:
        return "Erro ao registrar entrada no estoque"

    return "Entrada no estoque realizada com sucesso!"

# Validar saida do estoque

def validar_saida_estoque(produto_id, usuario_id, quantidade, motivo, data_hora, venda_id):

    produto = busca_produto_id(produto_id)
    usuario = busca_usuario_id(usuario_id)

    if produto is None:
        return "Produto não localizado"

    if usuario is None:
        return "Usuario não localizado"    

    quantidade_produto = produto[7]

    if quantidade <= 0:
        return "Quantidade deve ser maior que zero"
    
    if quantidade > quantidade_produto:
        return "Estoque insuficiente"

    if not motivo:
        return "Motivo obrigatório"

    resultado_atualizacao = atualizar_quantidade_produto(produto_id,quantidade, "saida")

    if not resultado_atualizacao:
        return "Erro ao atualizar estoque"

    resultado_movimentacao = registro_saida_estoque(produto_id, usuario_id, quantidade, motivo, data_hora, venda_id)

    if not resultado_movimentacao:
        return "Erro ao registrar saida no estoque"

    return "Saida no estoque realizada com sucesso!"

#  Validar ajuste de estoque

def validar_ajuste_estoque(produto_id, usuario_id, quantidade, motivo):

    produto = busca_produto_id(produto_id)
    usuario = busca_usuario_id(usuario_id)
    

    if produto is None:
        return "Produto não localizado"

    if usuario is None:
        return "Usuario não localizado"

    quantidade_produto = produto[7]

    if quantidade is None:
            return "Digite um valor inteiro"
    
    if quantidade == 0:
        return "Quantidade deve ser diferente que zero"

    if not motivo:
        return "Motivo, obrigatorio"

    resultado_atualizacao = atualizar_quantidade_produto(produto_id, quantidade, "ajuste")

    if not resultado_atualizacao:
        return "Erro ao atualizar estoque"
    
    resultado_movimentacao = registro_ajuste_estoque(produto_id, usuario_id, quantidade, motivo)
    
    if not resultado_movimentacao:
        return "Erro ao ajustar o estoque"

    return "Ajuste no estoque realizado com sucesso!!"

# Atualizar quantidade produto

def atualizar_quantidade_produto(produto_id,quantidade, operacao):

    produto = busca_produto_id(produto_id)

    if produto is None:
        return False
    
    estoque_atual = produto[7]

    if operacao == "entrada":
        novo_estoque = estoque_atual + quantidade

    elif operacao == "saida":
        novo_estoque = estoque_atual - quantidade

    elif operacao == "ajuste":
        novo_estoque = estoque_atual + quantidade

    else:
        return False

    return atualizar_quantidade_estoque(produto_id, novo_estoque)

# Verificar estoque minimo

def verificar_estoque_minimo():

    produtos = busca_produtos_baixo()

    if not produtos:
        return "Nenhum produto com estoque baixo"

    return produtos

# Verificar validade de produtos

def verificar_validade_produtos():

    produtos = busca_produtos_proximo_vencidos()

    if not produtos:
        return "Nenhum produto próximo do vencimento"

    return produtos
    