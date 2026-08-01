import customtkinter as ctk
from controllers.login_controller import validar_acesso


class LoginView:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.janela = ctk.CTk()
        self.janela.title("Login")
        self.janela.geometry("500x300")
        self.janela.minsize(100, 100)

        self.usuario = ctk.CTkEntry(
            self.janela,
            placeholder_text="Usuário",
            width=250
        )
        self.usuario.pack(pady=40)

        self.senha = ctk.CTkEntry(
            self.janela,
            placeholder_text="Senha",
            show="*",
            width=250
        )
        self.senha.pack(pady=10)

        self.botao = ctk.CTkButton(
            self.janela,
            text="Entrar",
            width=250,
            command=self.realizar_login
        )
        self.botao.pack(pady=20)

    def realizar_login(self):

        usuario = self.usuario.get()
        senha = self.senha.get()

        resultado = validar_acesso(usuario, senha)

        print(resultado)

    def iniciar(self):
        self.janela.mainloop()