import customtkinter as ctk
from tkinter import messagebox

class ConfigPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(self, text="Configurações do Sistema", font=("Arial", 22)).pack(pady=10)

        # Tema
        tema_frame = ctk.CTkFrame(self)
        tema_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(tema_frame, text="Tema:").pack(side="left", padx=5)
        self.tema_var = ctk.StringVar(value=ctk.get_appearance_mode())
        tema_menu = ctk.CTkOptionMenu(tema_frame, values=["Light", "Dark", "System"], variable=self.tema_var)
        tema_menu.pack(side="left", padx=5)

        # Nome da empresa
        empresa_frame = ctk.CTkFrame(self)
        empresa_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(empresa_frame, text="Nome da Empresa:").pack(side="left", padx=5)
        self.empresa_entry = ctk.CTkEntry(empresa_frame, placeholder_text="Digite o nome da empresa")
        self.empresa_entry.pack(side="left", fill="x", expand=True, padx=5)

        # Botão salvar
        salvar_btn = ctk.CTkButton(self, text="Salvar Configurações", command=self.salvar_config)
        salvar_btn.pack(pady=20)

    def salvar_config(self):
        tema = self.tema_var.get()
        nome_empresa = self.empresa_entry.get().strip()

        # Aplica o tema selecionado
        if tema.lower() == "light":
            ctk.set_appearance_mode("Light")
        elif tema.lower() == "dark":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("System")

        # Aqui você pode salvar o nome da empresa em arquivo/config/banco, vou só mostrar mensagem
        messagebox.showinfo("Configurações", f"Configurações salvas!\nTema: {tema}\nEmpresa: {nome_empresa}")
