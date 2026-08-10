import customtkinter as ctk

from Front import parametro as p

from Front.cabecalho import Cabecalho
from Front.conteudo import Conteudo
from Front.menu_lateral import MenuLateral
from Front.area_principal import AreaPrincipal
from Front.rodape import Rodape


# ==========================================
# Configuração do CustomTkinter
# ==========================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ==========================================
# Classe Principal da Aplicação
# ==========================================
class SistemaMercado(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.title(p.Janela.TITULO)

        self.geometry(
            f"{p.Janela.LARGURA}x{p.Janela.ALTURA}"
        )

        self.minsize(
            p.Janela.LARGURA_MIN,
            p.Janela.ALTURA_MIN
        )

        self.configure(
            fg_color=p.Cores.FUNDO
        )

        # Componentes da interface
        self.cabecalho = Cabecalho(self)

        self.rodape = Rodape(self)

        self.conteudo = Conteudo(self)

        self.menu_lateral = MenuLateral(
            self.conteudo.frame
        )

        self.area_principal = AreaPrincipal(
            self.conteudo.frame
        )


# ==========================================
# Inicialização
# ==========================================
app = SistemaMercado()

if __name__ == "__main__":
    app.mainloop()