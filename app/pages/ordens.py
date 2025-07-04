import customtkinter as ctk
from components.filtro import FiltroFrame

class OrdensPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Título
        ctk.CTkLabel(self, text="Ordens de Serviço", font=("Arial", 22)).pack(pady=10)

        # Frame superior para botões + filtro
        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(top_frame, text="Adicionar", command=self.adicionar_ordem).pack(side="left", padx=5)

        filtro = FiltroFrame(top_frame, on_filtrar_callback=self.filtrar_ordens)
        filtro.pack(side="left", fill="x", expand=True, padx=5)

        # Tabela
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.dados = []
        self.pagina_atual = 1
        self.total_paginas = 3

        self.carregar_dados_fake()
        self.renderizar_tabela()

        # Paginação
        pagination_frame = ctk.CTkFrame(self)
        pagination_frame.pack(pady=10)

        ctk.CTkButton(pagination_frame, text="Anterior", command=self.pagina_anterior).pack(side="left", padx=5)
        self.pagina_label = ctk.CTkLabel(pagination_frame, text=f"Página {self.pagina_atual} de {self.total_paginas}")
        self.pagina_label.pack(side="left", padx=5)
        ctk.CTkButton(pagination_frame, text="Próxima", command=self.pagina_proxima).pack(side="left", padx=5)

    def carregar_dados_fake(self):
        self.dados = [
            {"id": i, "descricao": f"Ordem de serviço {i}"}
            for i in range((self.pagina_atual - 1) * 5 + 1, self.pagina_atual * 5 + 1)
        ]

    def renderizar_tabela(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Cabeçalho
        header = ctk.CTkFrame(self.table_frame)
        header.pack(fill="x")
        ctk.CTkLabel(header, text="ID", width=50, anchor="w").pack(side="left", padx=5)
        ctk.CTkLabel(header, text="Descrição", anchor="w").pack(side="left", padx=5)

        # Dados como botões clicáveis
        for item in self.dados:
            button_row = ctk.CTkButton(
                self.table_frame,
                text=f"{item['id']} - {item['descricao']}",
                anchor="w",
                fg_color="transparent",  # sem cor de fundo
                hover_color="#3a3a3a",   # cor ao passar mouse
                text_color="white",
                corner_radius=0,
                command=lambda i=item: self.mostrar_detalhes(i)
            )
            button_row.pack(fill="x", pady=1)

    def mostrar_detalhes(self, item):
        detalhes = ctk.CTkToplevel(self)
        detalhes.title(f"Detalhes Ordem {item['id']}")
        detalhes.geometry("400x200")
        detalhes.grab_set()

        ctk.CTkLabel(detalhes, text=f"ID: {item['id']}", font=("Arial", 18)).pack(pady=10)
        ctk.CTkLabel(detalhes, text=f"Descrição: {item['descricao']}", font=("Arial", 16)).pack(pady=10)
        ctk.CTkButton(detalhes, text="Fechar", command=detalhes.destroy).pack(pady=20)

    def adicionar_ordem(self):
        toplevel = ctk.CTkToplevel(self)
        toplevel.title("Nova Ordem")
        toplevel.geometry("400x300")
        toplevel.grab_set()

        ctk.CTkLabel(toplevel, text="Cliente:").pack(pady=5)
        entry_cliente = ctk.CTkEntry(toplevel)
        entry_cliente.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(toplevel, text="Descrição:").pack(pady=5)
        entry_desc = ctk.CTkEntry(toplevel)
        entry_desc.pack(pady=5, fill="x", padx=10)

        def salvar():
            cliente = entry_cliente.get()
            desc = entry_desc.get()
            print(f"Ordem adicionada: Cliente={cliente}, Descrição={desc}")
            toplevel.destroy()

        frame_botoes = ctk.CTkFrame(toplevel)
        frame_botoes.pack(pady=20)

        ctk.CTkButton(frame_botoes, text="Salvar", command=salvar).pack(side="left", padx=10)
        ctk.CTkButton(frame_botoes, text="Cancelar", command=toplevel.destroy).pack(side="left", padx=10)

    def filtrar_ordens(self, termo):
        print(f"Filtrando ordens com o termo: {termo}")
        filtro = termo.lower()
        dados_filtrados = [d for d in self.dados if filtro in d["descricao"].lower()]
        if dados_filtrados:
            self.dados = dados_filtrados
        else:
            self.carregar_dados_fake()
        self.renderizar_tabela()
        self.pagina_label.configure(text=f"Página {self.pagina_atual} de {self.total_paginas}")

    def pagina_proxima(self):
        if self.pagina_atual < self.total_paginas:
            self.pagina_atual += 1
            self.carregar_dados_fake()
            self.renderizar_tabela()
            self.pagina_label.configure(text=f"Página {self.pagina_atual} de {self.total_paginas}")

    def pagina_anterior(self):
        if self.pagina_atual > 1:
            self.pagina_atual -= 1
            self.carregar_dados_fake()
            self.renderizar_tabela()
            self.pagina_label.configure(text=f"Página {self.pagina_atual} de {self.total_paginas}")
