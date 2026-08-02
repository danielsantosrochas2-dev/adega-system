from repositories.produto_repository import cadastrar_produto

# Validar Cadastro de produto

def validar_cdtr_produto(nome, categoria_id, codigo_interno, preco_compra, preco_venda, estoque, estoque_minimo, controla_dose, doses_por_unidade, controla_validade, data_validade):

    if not nome:
     return "Não deixe em branco"

    if categoria_id is None:
       return "Categoria é obrigatória"

    if not codigo_interno:
       return "Código interno é obrigatorio"

    if preco_compra <= 0:
       return "Preço da compra deve ser maior que zero"

    if preco_venda <= 0:
       return "Preço de venda deve ser maior que zero"

    if estoque <= 0:
       return "Estoque não pode ser negativo"

    if estoque_minimo <= 0:
       return "Estoque mínimo não deve ser negativo"

    if controla_dose and doses_por_unidade <= 0:
       return "Informe a quantidade de doses"

    if controla_validade and not data_validade:
       return "Informe a data de validade"
    else:
        cadastrar_produto(nome, categoria_id, codigo_interno, preco_compra, preco_venda, estoque, estoque_minimo, controla_dose, doses_por_unidade, controla_validade, data_validade)
        return "Produto cadastrado com sucesso1"



