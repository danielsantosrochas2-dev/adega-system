from repositories.movimentacao_repository import busca_movimentacao_periodo
from repositories.movimentacao_repository import busca_movimentacao_produto
from repositories.movimentacao_repository import listar_movimentacoes_gerais
from repositories.movimentacao_repository import registro_ajuste_estoque
from repositories.movimentacao_repository import registro_entrada_estoque
from repositories.movimentacao_repository import registro_saida_estoque
from repositories.produto_repository import busca_produto_id
from repositories.usuario_repository import busca_usuario_id

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

    resultado = registro_entrada_estoque(produto_id, usuario_id, quantidade, motivo)

    if not resultado:
        return "Erro ao registrar entrada no estoque"

    return "Entrada no estoque realizada com sucesso!"

# Validar saida do estoque

def validar_saida_estoque(produto_id, usuario_id, quantidade, motivo, venda_id):

    produto = busca_produto_id(produto_id)
    usuario = busca_usuario_id(usuario_id)

    if produto is None:
        return "Produto não localizado"

    if usuario is None:
        return "Usuario não localizado"    

    quantidade_produto = produto[7]

    if quantidade <= 0:
        return "Quantidade dever ser maior que zero"
    
    if quantidade > quantidade_produto:
        return "Estoque insuficiente"

    if not motivo:
        return "Motivo obrigatório"

    resultado = registro_saida_estoque(produto_id, usuario_id, quantidade, motivo, venda_id)

    if not resultado:
        return "Erro ao registrar saida no estoque"

    return "Saida no estoque realizada com sucesso!!"

#  Validar ajuste de estoque

def validar_ajuste_estoque(produto_id, usuario_id, quantidade, motivo):

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
        return "Estoque Insuficiente"

    if not motivo:
        return "Motivo, obrigatorio"

    resultado = registro_ajuste_estoque(produto_id, usuario_id, quantidade, motivo)

    if not resultado:
        return "Erro ao ajustar o estoque"

    return "Ajuste no estoque realizado com sucesso!!"