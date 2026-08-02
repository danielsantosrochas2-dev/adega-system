from repositories.produto_repository import cadastrar_produto
from repositories.produto_repository import atualizar_produto
from repositories.produto_repository import busca_produto_id
from repositories.produto_repository import busca_produto_nome

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

    if estoque < 0:
       return "Estoque não pode ser negativo"

    if estoque_minimo < 0:
       return "Estoque mínimo não deve ser negativo"

    if controla_dose and doses_por_unidade <= 0:
       return "Informe a quantidade de doses"

    if controla_validade and not data_validade:
       return "Informe a data de validade"
    else:
        cadastrar_produto(nome, categoria_id, codigo_interno, preco_compra, preco_venda, estoque, estoque_minimo, controla_dose, doses_por_unidade, controla_validade, data_validade)
        return "Produto cadastrado com sucesso1"

# Validar atualização de produto

def validar_atualizar_produto(id, nome, categoria_id, codigo_interno, preco_compra, preco_venda, controla_dose, doses_por_unidade, controla_validade, data_validade):

   produto_existe = busca_produto_id(id)

   if id is None:
         return "ID é obrigatório"
   
   if produto_existe is None:
      return "Digite um produto existente!"
   
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

   if controla_dose and doses_por_unidade <= 0:
      return "Informe a quantidade de doses"

   if controla_validade and not data_validade:
      return "Informe a data de validade"
   
   atualizar_produto(id, nome, categoria_id, codigo_interno, preco_compra, preco_venda, controla_dose, doses_por_unidade, controla_validade, data_validade)
   return "Produto atualizado com sucesso!"

# Validar consulta unica de nome obrigatorio

def validar_busca_produto_nome(nome):

   if not nome:
      return "Informe o nome do produto"
   
   produto = busca_produto_nome(nome)

   if produto is None:
      return "Produto não localizado"

   return produto







   
   
   



