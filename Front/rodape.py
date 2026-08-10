import customtkinter as ctk

from Front import parametro as p


# ==========================================
# Classe do Rodapé
# ==========================================
class Rodape:

    def __init__(self, master):

        self.master = master

        # Frame
        self.frame_rodape = None

        # Labels
        self.label_versao = None
        self.label_status = None
        self.label_conexao = None

        self.criar_frame()
        self.criar_componentes()

    # ==========================================
    # Criar Estrutura
    # ==========================================
    def criar_frame(self):

        self.frame_rodape = ctk.CTkFrame(
            master=self.master,
            height=p.Layout.ALTURA_RODAPE,
            corner_radius=p.Layout.RAIO,
            fg_color=p.Cores.RODAPE,
            border_width=p.Layout.BORDA,
            border_color=p.Cores.BORDA
        )

        self.frame_rodape.pack(
            side="bottom",
            fill="x"
        )

        self.frame_rodape.pack_propagate(False)

    # ==========================================
    # Criar Componentes
    # ==========================================
    def criar_componentes(self):

        self.frame_rodape.grid_columnconfigure(0, weight=1)
        self.frame_rodape.grid_columnconfigure(1, weight=1)
        self.frame_rodape.grid_columnconfigure(2, weight=1)

        # Versão
        self.label_versao = ctk.CTkLabel(
            master=self.frame_rodape,
            text="Versão 0.0.1",
            font=p.Fontes.PEQUENA,
            text_color=p.Cores.BRANCO
        )

        self.label_versao.grid(
            row=0,
            column=0,
            padx=15,
            sticky="w"
        )

        # Conexão
        self.label_conexao = ctk.CTkLabel(
            master=self.frame_rodape,
            text="Conectado",
            font=p.Fontes.PEQUENA,
            text_color=p.Cores.BRANCO
        )

        self.label_conexao.grid(
            row=0,
            column=1
        )

        # Status
        self.label_status = ctk.CTkLabel(
            master=self.frame_rodape,
            text="🟢 Sistema Online",
            font=p.Fontes.PEQUENA,
            text_color=p.Cores.BRANCO
        )

        self.label_status.grid(
            row=0,
            column=2,
            padx=15,
            sticky="e"
        )