# ==========================================
# Configurações da Janela
# ==========================================
class Janela:
    TITULO = "Adega do Ney"

    LARGURA = 1400
    ALTURA = 765

    LARGURA_MIN = 1200
    ALTURA_MIN = 700


# ==========================================
# Layout da Interface
# ==========================================
class Layout:
    # Cabeçalho
    ALTURA_TOPO = 100
    PADDING_LATERAL = 20
    PADDING_INFO = 15

    # Menu lateral
    LARGURA_MENU = 150
    LARGURA_BOTAO_MENU = 130
    ALTURA_BOTAO_MENU = 45
    ESPACO_BOTOES = 8
    PADDING_MENU = 10

    # Rodapé
    ALTURA_RODAPE = 30

    # Aparência
    BORDA = 1
    RAIO = 0
    RAIO_BOTAO = 8

     # outros parâmetros...

    PADDING_BOAS_VINDAS = 25
    ESPACO_TUTORIAL = 8

# ==========================================
# Cores
# ==========================================
class Cores:
    # Cores principais
    FUNDO = "#202020"
    TOPO = "#4A4A4A"
    MENU = "#DF653D"
    MENU_HOVER = "#C2410C"
    RODAPE = "#0F172A"

    PRINCIPAL = "#FFFFFF"


    # Botões
    BOTAO_MENU = "#DF653D"
    MENU_HOVER = "#C2410C"
    BOTAO_ATIVO = "#FFFFFF"

    # Textos
    BRANCO = "#FFFFFF"
    PRETO = "#000000"
    CINZA_CLARO = "#D8D8D8"

    # Área principal
    PRINCIPAL = "#FFFFFF"

    # Bordas
    BORDA = "#2A2A2A"


# ==========================================
# Empresa
# ==========================================
class Empresa:
    NOME = "Adega do Ney"
    SLOGAN = "Sistema de Gestão"
    VERSAO = "0.0.1"


# ==========================================
# Configurações do Caixa
# ==========================================
class Caixa:
    NOME = "Caixa"
    NUMERO = "01"

    TEXTO_COMPLETO = f"{NOME} {NUMERO}"


# ==========================================
# Fontes
# ==========================================
class Fontes:
    TITULO = ("Segoe UI", 40, "bold")
    SUBTITULO = ("Segoe UI", 20, "bold")
    TEXTO = ("Segoe UI", 14)
    PEQUENA = ("Segoe UI", 12)
    CABECALHO_INFO = ("Segoe UI", 13)

    TITULO_MENU = ("Segoe UI", 18, "bold")
    BOTAO_MENU = ("Segoe UI", 14, "bold")

    TITULO_BOAS_VINDAS = ("Segoe UI", 30, "bold")
    SUBTITULO_BOAS_VINDAS = ("Segoe UI", 16)
    ITEM_TUTORIAL = ("Segoe UI", 14)
    # ==========================================
# Caminhos das Imagens
# ==========================================
class Imagens:
    BOAS_VINDAS = "imagens/boas_vindas.png"

    LARGURA_BOAS_VINDAS = 450
    ALTURA_BOAS_VINDAS = 220