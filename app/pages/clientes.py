import customtkinter as ctk
from components.filtro import FiltroFrame

class ClientesPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(self, text="Clientes Cadastrados", font=("Arial", 22)).pack(pady=10)

        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(top_frame, text="Adicionar", command=self.adicionar_ordem).pack(side="left", padx=5)
        filtro = FiltroFrame(top_frame, on_filtrar_callback=self.filtrar_ordens)
        filtro.pack(side="left", fill="x", expand=True, padx=5)

        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.dados = []
        self.pagina_atual = 1
        self.total_paginas = 3

        self.carregar_dados_fake()
        self.renderizar_tabela()

        pagination_frame = ctk.CTkFrame(self)
        pagination_frame.pack(pady=10)

        ctk.CTkButton(pagination_frame, text="Anterior", command=self.pagina_anterior).pack(side="left", padx=5)
        self.pagina_label = ctk.CTkLabel(pagination_frame, text=f"Página {self.pagina_atual} de {self.total_paginas}")
        self.pagina_label.pack(side="left", padx=5)
        ctk.CTkButton(pagination_frame, text="Próxima", command=self.pagina_proxima).pack(side="left", padx=5)

    def carregar_dados_fake(self):
        self.dados = [
            {
                "id": i,
                "nome": f"João {i}",
                "telefone": f"4002892 {i}",
                "qtd_veiculos": "1",
            }
            for i in range((self.pagina_atual - 1) * 5 + 1, self.pagina_atual * 5 + 1)
        ]

    def renderizar_tabela(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Cabeçalho tipo planilha
        header = ctk.CTkFrame(self.table_frame)
        header.pack(fill="x")
        ctk.CTkLabel(header, text="ID", width=50, anchor="w").pack(side="left", padx=5)
        ctk.CTkLabel(header, text="Nome", width=150, anchor="w").pack(side="left", padx=5)
        ctk.CTkLabel(header, text="Telefone", width=150, anchor="w").pack(side="left", padx=5)
        ctk.CTkLabel(header, text="Qtd. Veiculos", width=100, anchor="w").pack(side="left", padx=5)
        # ctk.CTkLabel(header, text="", width=100, anchor="w").pack(side="left", padx=5)

        # Dados como linhas organizadas
        for item in self.dados:
            row = ctk.CTkFrame(self.table_frame, fg_color="transparent")
            row.pack(fill="x", pady=1)

            ctk.CTkLabel(row, text=f"{item['id']}", width=50, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=item['nome'], width=150, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=item['telefone'], width=150, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=item['qtd_veiculos'], width=100, anchor="w").pack(side="left", padx=5)
            # ctk.CTkLabel(row, text=item['status'], width=100, anchor="w").pack(side="left", padx=5)

            # Hover manual
            row.bind("<Enter>", lambda e, fr=row: fr.configure(fg_color="#3a3a3a"))
            row.bind("<Leave>", lambda e, fr=row: fr.configure(fg_color="transparent"))

            # Clique para abrir detalhes
            row.bind("<Button-1>", lambda e, i=item: self.mostrar_detalhes(i))
            for child in row.winfo_children():
                child.bind("<Enter>", lambda e, fr=row: fr.configure(fg_color="#3a3a3a"))
                child.bind("<Leave>", lambda e, fr=row: fr.configure(fg_color="transparent"))
                child.bind("<Button-1>", lambda e, i=item: self.mostrar_detalhes(i))


    def mostrar_detalhes(self, item):
        detalhes = ctk.CTkToplevel(self)
        detalhes.title(f"Detalhes Cliente {item['id']}")
        detalhes.geometry("400x300")
        detalhes.grab_set()

        ctk.CTkLabel(detalhes, text=f"Id: {item['id']}", font=("Arial", 18)).pack(pady=5)
        ctk.CTkLabel(detalhes, text=f"Nome: {item['nome']}", font=("Arial", 16)).pack(pady=5)
        ctk.CTkLabel(detalhes, text=f"Telefone: {item['telefone']}", font=("Arial", 16)).pack(pady=5)
        ctk.CTkLabel(detalhes, text=f"Veiculos: {item['qtd_veiculos']}", font=("Arial", 16)).pack(pady=5)
        ctk.CTkButton(detalhes, text="Fechar", command=detalhes.destroy).pack(pady=15)

    def adicionar_ordem(self):
        toplevel = ctk.CTkToplevel(self)
        toplevel.title("Novo Cliente")
        toplevel.geometry("400x300")
        toplevel.grab_set()

        ctk.CTkLabel(toplevel, text="Nome:").pack(pady=5)
        entry_cliente = ctk.CTkEntry(toplevel)
        entry_cliente.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(toplevel, text="Telefone:").pack(pady=5)
        entry_telefone = ctk.CTkEntry(toplevel)
        entry_telefone.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(toplevel, text="Veiculos:").pack(pady=5)
        entry_data = ctk.CTkEntry(toplevel)
        entry_data.pack(pady=5, fill="x", padx=10)

        # ctk.CTkLabel(toplevel, text="Status:").pack(pady=5)
        # entry_status = ctk.CTkEntry(toplevel)
        # entry_status.pack(pady=5, fill="x", padx=10)

        def salvar():
            nome = entry_cliente.get()
            telefone = entry_telefone.get()
            veiculos = entry_data.get()

            toplevel.destroy()

        frame_botoes = ctk.CTkFrame(toplevel)
        frame_botoes.pack(pady=20)
        ctk.CTkButton(frame_botoes, text="Salvar", command=salvar).pack(side="left", padx=10)
        ctk.CTkButton(frame_botoes, text="Cancelar", command=toplevel.destroy).pack(side="left", padx=10)

    def filtrar_ordens(self, termo):
        filtro = termo.lower()
        dados_filtrados = [d for d in self.dados if filtro in d["nome"].lower()]
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
