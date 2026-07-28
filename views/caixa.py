import customtkinter as ctk
import getpass

# Configuração do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("Sistema de Mercado")
janela.geometry("1400x800")
janela.minsize(1200, 700)

# Cor do fundo da janela
janela.configure(fg_color="#202020")

# =========================
# CABEÇALHO
# =========================

frame_topo = ctk.CTkFrame(
    master=janela,
    height=100,
    corner_radius=0,
    fg_color="#4A4A4A",
    border_width=1,
    border_color="#2A2A2A"
)

frame_topo.pack(fill="x", padx=5, pady=(5, 2))
frame_topo.pack_propagate(False)

# Configuração das colunas
frame_topo.grid_columnconfigure(0, weight=1)
frame_topo.grid_columnconfigure(1, weight=2)
frame_topo.grid_columnconfigure(2, weight=1)

usuario = getpass.getuser()

# Nome da empresa
titulo = ctk.CTkLabel(
    frame_topo,
    text="🛒 Adega do Ney",
    font=("Segoe UI", 28, "bold"),
    text_color="white"
)
titulo.grid(row=0, column=0, padx=15, sticky="w")

# Subtítulo
subtitulo = ctk.CTkLabel(
    frame_topo,
    text="Sistema de Gerenciamento de Vendas",
    font=("Segoe UI", 16),
    text_color="#D8D8D8"
)
subtitulo.grid(row=1, column=1)

# Operador
operador = ctk.CTkLabel(
    frame_topo,
    text=f"👤 Operador: {usuario}",
    font=("Segoe UI", 16),
    text_color="white"
)
operador.grid(row=0, column=1, padx=10, sticky="e")

# Caixa
caixa = ctk.CTkLabel(
    frame_topo,
    text="🖥 Caixa 01",
    font=("Segoe UI", 16),
    text_color="white"
)
caixa.grid(row=1, column=2, padx=20, sticky="e")
# =========================
# TÍTULO DO SISTEMA
# =========================
titulo = ctk.CTkLabel(
    master=frame_topo,
    text="Adega do Ney",
    font=("Segoe UI", 40, "bold"),
    text_color="white"
)

titulo.grid(row=0, column=1)


# =========================
# USUÁRIO
# =========================
usuario = getpass.getuser()

label_usuario = ctk.CTkLabel(
    master=frame_topo,
    text=f"👤 {usuario}",
    font=("Segoe UI", 18),
    text_color="white"
)

label_usuario.grid(row=0, column=2, padx=46, sticky="e")

# =========================
# ÁREA CENTRAL
# =========================
frame_central = ctk.CTkFrame(
    master=janela,
    fg_color="#202020",
    corner_radius=0
)

frame_central.pack(fill="both", expand=True)

# =========================
# MENU LATERAL
# =========================
frame_menu = ctk.CTkFrame(
    master=frame_central,
    width=500,
    corner_radius=0,
    fg_color="#7C2D12",
    border_width=1,
    border_color="#2A2A2A"
)

frame_menu.pack(
    side="left",
    fill="y",
    padx=(5, 2),
    pady=5
)

frame_menu.pack_propagate(False)

# =========================
# ÁREA PRINCIPAL
# =========================
frame_principal = ctk.CTkFrame(
    master=frame_central,
    fg_color="white",
    border_width=1,
    border_color="#2A2A2A"
)

frame_principal.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(2, 5),
    pady=5
)

# =========================
# RODAPÉ
# =========================
frame_rodape = ctk.CTkFrame(
    master=janela,
    height=200,
    corner_radius=0,
    fg_color="#0F172A",
    border_width=1,
    border_color="#2A2A2A"
)

frame_rodape.pack(fill="x", padx=5, pady=(2, 5))
frame_rodape.pack_propagate(False)

# Inicia o programa
janela.mainloop()