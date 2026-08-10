from datetime import datetime
import customtkinter as ctk
import getpass

from Front import parametro as p


# ==========================================
# Classe do Cabeçalho
# ==========================================
class Cabecalho:

    def __init__(self, master):
        self.master = master

        # Frames
        self.frame_topo = None
        self.frame_esquerda = None
        self.frame_centro = None
        self.frame_direita = None

        # Labels
        self.label_empresa = None
        self.label_logo = None
        self.label_usuario = None
        self.label_data = None
        self.label_hora = None

        self.criar_frame()
        self.criar_componentes()
        self.atualizar_relogio()

    # ==========================================
    # Criar Estrutura
    # ==========================================
    def criar_frame(self):
        self.frame_topo = ctk.CTkFrame(
            master=self.master,
            height=p.Layout.ALTURA_TOPO,
            corner_radius=p.Layout.RAIO,
            fg_color=p.Cores.TOPO,
            border_width=p.Layout.BORDA,
            border_color=p.Cores.BORDA
        )

        self.frame_topo.pack(
            side="top",
            fill="x"
        )

        self.frame_topo.pack_propagate(False)

        # Esquerda
        self.frame_esquerda = ctk.CTkFrame(
            master=self.frame_topo,
            fg_color="transparent"
        )

        self.frame_esquerda.pack(
            side="left",
            fill="y",
            padx=p.Layout.PADDING_LATERAL
        )

        # Direita
        self.frame_direita = ctk.CTkFrame(
            master=self.frame_topo,
            fg_color="transparent"
        )

        self.frame_direita.pack(
            side="right",
            fill="y",
            padx=p.Layout.PADDING_LATERAL
        )

        # Centro
        self.frame_centro = ctk.CTkFrame(
            master=self.frame_topo,
            fg_color="transparent"
        )

        self.frame_centro.pack(
            side="left",
            fill="both",
            expand=True
        )

    # ==========================================
    # Criar Componentes
    # ==========================================
    
    def criar_componentes(self):
        usuario = getpass.getuser()

        self.label_empresa = ctk.CTkLabel(
            master=self.frame_esquerda,
            text=p.Empresa.NOME,
            font=p.Fontes.TITULO,
            text_color=p.Cores.BRANCO
        )

        self.label_empresa.pack(
            expand=True
        )

        self.label_logo = ctk.CTkLabel(
            master=self.frame_centro,
            text="LOGO",
            font=p.Fontes.SUBTITULO,
            text_color=p.Cores.BRANCO
        )

        self.label_logo.pack(
            expand=True
        )

        self.label_usuario = ctk.CTkLabel(
            master=self.frame_direita,
            text=f"Usuário: {usuario}",
            font=p.Fontes.CABECALHO_INFO,
            text_color=p.Cores.BRANCO
        )

        self.label_usuario.pack(
            side="right",
            padx=p.Layout.PADDING_INFO
        )

        self.label_data = ctk.CTkLabel(
            master=self.frame_direita,
            text="",
            font=p.Fontes.CABECALHO_INFO,
            text_color=p.Cores.BRANCO
        )

        self.label_data.pack(
            side="right",
            padx=p.Layout.PADDING_INFO
        )

        self.label_hora = ctk.CTkLabel(
            master=self.frame_direita,
            text="",
            font=p.Fontes.CABECALHO_INFO,
            text_color=p.Cores.BRANCO
        )

        self.label_hora.pack(
            side="right",
            padx=p.Layout.PADDING_INFO
        )

    # ==========================================
    # Atualizar Relógio
    # ==========================================
    def atualizar_relogio(self):
        agora = datetime.now()

        self.label_data.configure(
            text=agora.strftime("%d/%m/%Y")
        )

        self.label_hora.configure(
            text=agora.strftime("%H:%M:%S")
        )

        self.master.after(
            1000,
            self.atualizar_relogio
        )