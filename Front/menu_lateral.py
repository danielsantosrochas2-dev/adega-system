import customtkinter as ctk

from Front import parametro as p


# ==========================================
# Classe do Menu Lateral
# ==========================================
class MenuLateral:

    def __init__(self, master):
        self.master = master

        self.frame_menu = None
        self.label_titulo = None

        self.botao_caixa = None
        self.botao_produtos = None
        self.botao_clientes = None
        self.botao_estoque = None

        self.criar_frame()
        self.criar_componentes()

    # ==========================================
    # Criar Estrutura do Menu
    # ==========================================
    def criar_frame(self):
        self.frame_menu = ctk.CTkFrame(
            master=self.master,
            width=p.Layout.LARGURA_MENU,
            corner_radius=p.Layout.RAIO,
            fg_color=p.Cores.MENU,
            border_width=p.Layout.BORDA,
            border_color=p.Cores.BORDA
        )

        self.frame_menu.pack(
            side="left",
            fill="y"
        )

        self.frame_menu.pack_propagate(False)

    # ==========================================
    # Criar Componentes do Menu
    # ==========================================
    def criar_componentes(self):
        self.label_titulo = ctk.CTkLabel(
            master=self.frame_menu,
            text="MENU",
            font=p.Fontes.TITULO_MENU,
            text_color=p.Cores.BRANCO
        )

        self.label_titulo.pack(
            pady=(20, 25)
        )

        self.botao_caixa = self.criar_botao(
            texto="🛒  Caixa"
        )

        self.botao_produtos = self.criar_botao(
            texto="📦  Produtos"
        )

        self.botao_clientes = self.criar_botao(
            texto="👥  Clientes"
        )

        self.botao_estoque = self.criar_botao(
            texto="📊  Estoque"
        )

    # ==========================================
    # Fabricar Botões do Menu
    # ==========================================
    def criar_botao(self, texto):
        botao = ctk.CTkButton(
            master=self.frame_menu,
            text=texto,
            width=p.Layout.LARGURA_BOTAO_MENU,
            height=p.Layout.ALTURA_BOTAO_MENU,
            corner_radius=p.Layout.RAIO_BOTAO,
            fg_color=p.Cores.BOTAO_MENU,
            hover_color=p.Cores.MENU_HOVER,
            text_color=p.Cores.BRANCO,
            font=p.Fontes.BOTAO_MENU,
            anchor="w"
        )

        botao.pack(
            padx=p.Layout.PADDING_MENU,
            pady=p.Layout.ESPACO_BOTOES
        )

        return botao