from database.conexao import conectar
from datetime import datetime
data_hora = datetime.now()
# Registrar entrada no estoque

def registro_entrada_estoque(produto_id, usuario_id, quantidade, motivo, data_hora):

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO movimentacoes_estoque (produto_id, usuario_id, tipo_movimentacao, quantidade, motivo, data_hora, venda_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (produto_id, usuario_id, "Entrada", quantidade, motivo, data_hora, None))
        conexao.commit()
        return True

    except Exception as erro:
        print(erro)
        return False

    finally:
        if conexao:
            conexao.close()

# Registrar Saida do estoque 

def registro_saida_estoque(produto_id, usuario_id, quantidade, motivo, data_hora, venda_id):

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO movimentacoes_estoque(produto_id, usuario_id, tipo_movimentacao, quantidade, motivo, data_hora, venda_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,(produto_id, usuario_id, "Saida", quantidade, motivo, data_hora, venda_id))
        conexao.commit()
        return True

    except Exception as erro:
        print(erro)
        return False

    finally:
        if conexao:
            conexao.close()

# Registrar Ajuste em estoque

def registro_ajuste_estoque(produto_id, usuario_id, quantidade, motivo, data_hora):

    conexao = None
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()
    
        cursor.execute("""
        INSERT INTO movimentacoes_estoque(produto_id, usuario_id, tipo_movimentacao, quantidade, motivo, data_hora, venda_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,(produto_id, usuario_id, "Ajuste", quantidade, motivo, data_hora, None))
        conexao.commit()
        return True
    
    except Exception as erro:
        print(erro)
        return False
    
    finally:
        if conexao:
            conexao.close()

# Buscar movimentação por produto

def busca_movimentacao_produto(produto_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM movimentacoes_estoque
    WHERE produto_id = ?
    ORDER BY data_hora DESC
    """, (produto_id,))

    movimentacao_produto = cursor.fetchall()
    conexao.close()

    return movimentacao_produto

# Busca movimentacao por periodo

def busca_movimentacao_periodo(data_inicial, data_final):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM movimentacoes_estoque
    WHERE data_hora BETWEEN ? AND ?
    ORDER BY data_hora DESC
    """, (data_inicial, data_final,))

    movimentacao_produto = cursor.fetchall()
    conexao.close()

    return movimentacao_produto

# Listar todas as movimentacoes

def listar_movimentacoes_gerais():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM movimentacoes_estoque
    ORDER BY data_hora DESC
    """)

    movimentacoes = cursor.fetchall()
    conexao.close()

    return movimentacoes