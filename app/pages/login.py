import customtkinter as ctk

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Frame centralizado
        content_frame = ctk.CTkFrame(self, fg_color="transparent")
        content_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        ctk.CTkLabel(content_frame, text="Login", font=("Arial", 24)).pack(pady=20)

        # Campos
        self.user_entry = ctk.CTkEntry(content_frame, placeholder_text="Usuário")
        self.user_entry.pack(pady=10, padx=20)

        self.pass_entry = ctk.CTkEntry(content_frame, placeholder_text="Senha", show="*")
        self.pass_entry.pack(pady=10, padx=20)

        # Mensagem de erro
        self.msg_label = ctk.CTkLabel(content_frame, text="", text_color="red")
        self.msg_label.pack()

        # Botão login
        self.login_btn = ctk.CTkButton(content_frame, text="Entrar", command=self.tentar_login)
        self.login_btn.pack(pady=20)

        # Loading
        self.loading_label = ctk.CTkLabel(content_frame, text="", font=("Arial", 16))
        self.loading_label.pack(pady=10)
        self.loading_label.pack_forget()

        self.loading_steps = 0


        self.bind("<Return>", lambda event: self.tentar_login())
        self.user_entry.bind("<Return>", lambda event: self.tentar_login())
        self.pass_entry.bind("<Return>", lambda event: self.tentar_login())

        # Foco inicial
        self.user_entry.focus()

    def tentar_login(self):
        user = self.user_entry.get()
        senha = self.pass_entry.get()

        if user == "joao" and senha == "123":
            self.msg_label.configure(text="")
            self.login_btn.configure(state="disabled")
            self.user_entry.configure(state="disabled")
            self.pass_entry.configure(state="disabled")

            # Mostrar loading
            self.loading_label.pack()
            self.loading_steps = 0
            self.loading_animar()
        else:
            self.msg_label.configure(text="Usuário ou senha incorretos!")

    def loading_animar(self):
        dots = "." * (self.loading_steps % 4)
        self.loading_label.configure(text=f"Carregando{dots}")
        self.loading_steps += 1

        if self.loading_steps <= 20:  # 20 passos, 200ms cada = ~4 segundos
            self.after(200, self.loading_animar)
        else:
            # Após "loading", abre dashboard
            self.controller.show_page(self.controller.pages['dashboard'])
