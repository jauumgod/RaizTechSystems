import customtkinter as ctk

class OrdensPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Título
        ctk.CTkLabel(self, text="Ordens de Serviço", font=("Arial", 22)).pack(pady=10)

        # Botões superior
        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(top_frame, text="Adicionar", command=self.adicionar_ordem).pack(side="left", padx=5)
        ctk.CTkButton(top_frame, text="Filtrar", command=self.filtrar_ordens).pack(side="left", padx=5)

        # Tabela fake
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.dados = []  # lista de dados
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

        # Dados
        for item in self.dados:
            row = ctk.CTkFrame(self.table_frame)
            row.pack(fill="x", pady=2)
            ctk.CTkLabel(row, text=str(item["id"]), width=50, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=item["descricao"], anchor="w").pack(side="left", padx=5)

    def adicionar_ordem(self):
        ctk.CTkMessagebox(title="Adicionar", message="Aqui abriria o formulário para adicionar ordem.", icon="info")

    def filtrar_ordens(self):
        ctk.CTkMessagebox(title="Filtrar", message="Aqui abriria o filtro.", icon="info")

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
