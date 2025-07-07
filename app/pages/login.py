import customtkinter as ctk
from app.services import user_service


class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Frame centralizado COM BORDA E TAMANHO FIXO
        content_frame = ctk.CTkFrame(
            self,
            fg_color="#2a2a2a",
            border_width=2,
            border_color="#888",
            width=400,
            height=400,
            corner_radius=10
        )
        content_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Impede de encolher para caber os widgets
        content_frame.pack_propagate(False)

        # Frame interno para criar padding interno
        inner_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        inner_frame.pack(fill="both", expand=True, padx=30, pady=30)

        # Título
        ctk.CTkLabel(inner_frame, text="LOGIN", font=("Arial", 26)).pack(pady=20)

        # Campos
        self.user_entry = ctk.CTkEntry(inner_frame, placeholder_text="Usuário")
        self.user_entry.pack(pady=10, padx=20, fill="x")

        self.pass_entry = ctk.CTkEntry(inner_frame, placeholder_text="Senha", show="*")
        self.pass_entry.pack(pady=10, padx=20, fill="x")

        # Mensagem de erro
        self.msg_label = ctk.CTkLabel(inner_frame, text="", text_color="red")
        self.msg_label.pack()

        # Botão login
        self.login_btn = ctk.CTkButton(inner_frame, text="Entrar", command=self.tentar_login)
        self.login_btn.pack(pady=20, fill="x", padx=20)

        # Loading
        self.loading_label = ctk.CTkLabel(inner_frame, text="", font=("Arial", 16))
        self.loading_label.pack(pady=10)
        self.loading_label.pack_forget()

        self.loading_steps = 0

        # Atalhos Enter
        self.bind("<Return>", lambda event: self.tentar_login())
        self.user_entry.bind("<Return>", lambda event: self.tentar_login())
        self.pass_entry.bind("<Return>", lambda event: self.tentar_login())

        # Foco inicial
        self.user_entry.focus()

    def fazer_login(self, user, password):
        login_sucesso = False
        try:
            login_sucesso = user_service.AuthUser.login_user(user, password)
        except Exception as e:
            print("Erro ao fazer login: ", e)

        if login_sucesso:
            self.controller.show_page(self.controller.pages['dashboard'])
        else:
            self.msg_label.configure(text="Usuario ou senha incorretos")
            self.loading_label.pack_forget()
        
        

    def loading_animar(self):
        dots = "." * (self.loading_steps % 4)
        self.loading_label.configure(text=f"Carregando{dots}")
        self.loading_steps += 1

        if self.loading_steps <= 20:  # 20 passos, 200ms cada = ~4 segundos
            self.after(200, self.loading_animar)
        else:
            self.controller.show_page(self.controller.pages['dashboard'])
