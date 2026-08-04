import customtkinter as ctk
import getpass

# Configuração do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("Loguin Adega do Ney")
janela.geometry("500x300")
janela.minsize(100, 100)

# Caixa de usuário
usuario = ctk.CTkEntry(
    janela,
    placeholder_text="Usuário",
    width=250
)
usuario.pack(pady=50)

# Caixa de senha
senha = ctk.CTkEntry(
    janela,
    placeholder_text="Senha",
    show="*",
    width=250
)
senha.pack(pady=5)

# Botão entrar
botao = ctk.CTkButton(
    janela,
    text="Entrar",
    width=200
)
botao.pack(pady=50)


janela.mainloop()
