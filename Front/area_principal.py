import os

import customtkinter as ctk
from PIL import Image

import parametro as p


# ==========================================
# Classe da Área Principal
# ==========================================
class AreaPrincipal:

    def __init__(self, master):
        self.master = master

        # Frames
        self.frame_principal = None
        self.frame_boas_vindas = None
        self.frame_tutorial = None

        # Imagem
        self.imagem_boas_vindas = None
        self.label_imagem = None

        # Labels
        self.label_titulo = None
        self.label_subtitulo = None

        self.criar_frame()
        self.mostrar_boas_vindas()

    # ==========================================
    # Criar Estrutura Principal
    # ==========================================
    def criar_frame(self):
        self.frame_principal = ctk.CTkFrame(
            master=self.master,
            corner_radius=p.Layout.RAIO,
            fg_color=p.Cores.PRINCIPAL,
            border_width=p.Layout.BORDA,
            border_color=p.Cores.BORDA
        )

        self.frame_principal.pack(
            side="left",
            fill="both",
            expand=True
        )

    # ==========================================
    # Limpar Área Principal
    # ==========================================
    def limpar_area(self):
        for componente in self.frame_principal.winfo_children():
            componente.destroy()

    # ==========================================
    # Mostrar Tela de Boas-vindas
    # ==========================================
    def mostrar_boas_vindas(self):
        self.limpar_area()

        self.frame_boas_vindas = ctk.CTkFrame(
            master=self.frame_principal,
            fg_color="transparent"
        )

        self.frame_boas_vindas.pack(
            fill="both",
            expand=True,
            padx=p.Layout.PADDING_BOAS_VINDAS,
            pady=p.Layout.PADDING_BOAS_VINDAS
        )

        # Título
        self.label_titulo = ctk.CTkLabel(
            master=self.frame_boas_vindas,
            text=f"Bem-vindo ao {p.Empresa.NOME}",
            font=p.Fontes.TITULO_BOAS_VINDAS,
            text_color=p.Cores.PRETO
        )

        self.label_titulo.pack(
            pady=(10, 5)
        )

        # Subtítulo
        self.label_subtitulo = ctk.CTkLabel(
            master=self.frame_boas_vindas,
            text="Selecione uma opção no menu lateral para começar.",
            font=p.Fontes.SUBTITULO_BOAS_VINDAS,
            text_color=p.Cores.PRETO
        )

        self.label_subtitulo.pack(
            pady=(0, 15)
        )

        self.carregar_imagem()

        self.criar_tutorial()

    # ==========================================
    # Carregar Imagem
    # ==========================================
    def carregar_imagem(self):
        caminho_imagem = p.Imagens.BOAS_VINDAS

        if os.path.exists(caminho_imagem):
            imagem_original = Image.open(caminho_imagem)

            self.imagem_boas_vindas = ctk.CTkImage(
                light_image=imagem_original,
                dark_image=imagem_original,
                size=(
                    p.Imagens.LARGURA_BOAS_VINDAS,
                    p.Imagens.ALTURA_BOAS_VINDAS
                )
            )

            self.label_imagem = ctk.CTkLabel(
                master=self.frame_boas_vindas,
                text="",
                image=self.imagem_boas_vindas
            )

        else:
            self.label_imagem = ctk.CTkLabel(
                master=self.frame_boas_vindas,
                text="Imagem de boas-vindas",
                width=p.Imagens.LARGURA_BOAS_VINDAS,
                height=p.Imagens.ALTURA_BOAS_VINDAS,
                corner_radius=10,
                fg_color=p.Cores.FUNDO,
                text_color=p.Cores.BRANCO,
                font=p.Fontes.SUBTITULO
            )

        self.label_imagem.pack(
            pady=(5, 20)
        )

    # ==========================================
    # Criar Tutorial
    # ==========================================
    def criar_tutorial(self):
        self.frame_tutorial = ctk.CTkFrame(
            master=self.frame_boas_vindas,
            fg_color="#F2F2F2",
            corner_radius=10,
            border_width=1,
            border_color=p.Cores.BORDA
        )

        self.frame_tutorial.pack(
            fill="x",
            padx=40,
            pady=(0, 15)
        )

        titulo_tutorial = ctk.CTkLabel(
            master=self.frame_tutorial,
            text="Guia rápido",
            font=p.Fontes.SUBTITULO,
            text_color=p.Cores.PRETO
        )

        titulo_tutorial.pack(
            pady=(15, 10)
        )

        itens = [
            "🛒 Caixa — inicia e acompanha as vendas.",
            "📦 Produtos — cadastra e consulta produtos.",
            "👥 Clientes — cadastra e consulta clientes.",
            "📊 Estoque — consulta quantidades e movimentações."
        ]

        for texto in itens:
            label_item = ctk.CTkLabel(
                master=self.frame_tutorial,
                text=texto,
                font=p.Fontes.ITEM_TUTORIAL,
                text_color=p.Cores.PRETO,
                anchor="w"
            )

            label_item.pack(
                fill="x",
                padx=25,
                pady=p.Layout.ESPACO_TUTORIAL
            )