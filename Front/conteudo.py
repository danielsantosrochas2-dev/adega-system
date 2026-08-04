import customtkinter as ctk

import parametro as p


# ==========================================
# Classe da Área de Conteúdo
# ==========================================
class Conteudo:

    def __init__(self, master):
        self.master = master
        self.frame = None

        self.criar_frame()

    # ==========================================
    # Criar Frame de Conteúdo
    # ==========================================
    def criar_frame(self):
        self.frame = ctk.CTkFrame(
            master=self.master,
            fg_color="transparent",
            corner_radius=p.Layout.RAIO
        )

        self.frame.pack(
            fill="both",
            expand=True
        )