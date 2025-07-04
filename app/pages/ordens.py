import customtkinter as ctk
from components.filtro import FiltroFrame

class OrdensPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(self, text="Ordens de Serviço", font=("Arial", 22)).pack(pady=10)

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
                "cliente": f"Cliente {i}",
                "veiculo": f"Carro {i}",
                "data_entrada": "01/07/2025",
                "status": "Aberta" if i % 2 == 0 else "Fechada"
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
        ctk.CTkLabel(header, text="Cliente", width=150, anchor="w").pack(side="left", padx=5)
        ctk.CTkLabel(header, text="Veículo", width=150, anchor="w").pack(side="left", padx=5)
        ctk.CTkLabel(header, text="Data Entrada", width=100, anchor="w").pack(side="left", padx=5)
        ctk.CTkLabel(header, text="Status", width=100, anchor="w").pack(side="left", padx=5)

        # Dados como linhas organizadas
        for item in self.dados:
            row = ctk.CTkFrame(self.table_frame, fg_color="transparent")
            row.pack(fill="x", pady=1)

            ctk.CTkLabel(row, text=f"{item['id']}", width=50, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=item['cliente'], width=150, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=item['veiculo'], width=150, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=item['data_entrada'], width=100, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=item['status'], width=100, anchor="w").pack(side="left", padx=5)

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
        detalhes.title(f"Detalhes Ordem {item['id']}")
        detalhes.geometry("400x300")
        detalhes.grab_set()

        ctk.CTkLabel(detalhes, text=f"Num.OS: {item['id']}", font=("Arial", 18)).pack(pady=5)
        ctk.CTkLabel(detalhes, text=f"Cliente: {item['cliente']}", font=("Arial", 16)).pack(pady=5)
        ctk.CTkLabel(detalhes, text=f"Veículo: {item['veiculo']}", font=("Arial", 16)).pack(pady=5)
        ctk.CTkLabel(detalhes, text=f"Data Entrada: {item['data_entrada']}", font=("Arial", 16)).pack(pady=5)
        ctk.CTkLabel(detalhes, text=f"Status: {item['status']}", font=("Arial", 16)).pack(pady=5)
        ctk.CTkButton(detalhes, text="Fechar", command=detalhes.destroy).pack(pady=15)

    def adicionar_ordem(self):
        toplevel = ctk.CTkToplevel(self)
        toplevel.title("Nova Ordem")
        toplevel.geometry("400x300")
        toplevel.grab_set()

        ctk.CTkLabel(toplevel, text="Cliente:").pack(pady=5)
        entry_cliente = ctk.CTkEntry(toplevel)
        entry_cliente.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(toplevel, text="Veículo:").pack(pady=5)
        entry_veiculo = ctk.CTkEntry(toplevel)
        entry_veiculo.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(toplevel, text="Data Entrada:").pack(pady=5)
        entry_data = ctk.CTkEntry(toplevel)
        entry_data.pack(pady=5, fill="x", padx=10)

        ctk.CTkLabel(toplevel, text="Status:").pack(pady=5)
        entry_status = ctk.CTkEntry(toplevel)
        entry_status.pack(pady=5, fill="x", padx=10)

        def salvar():
            cliente = entry_cliente.get()
            veiculo = entry_veiculo.get()
            data_entrada = entry_data.get()
            status = entry_status.get()
            print(f"Nova Ordem -> Cliente: {cliente}, Veículo: {veiculo}, Data Entrada: {data_entrada}, Status: {status}")
            toplevel.destroy()

        frame_botoes = ctk.CTkFrame(toplevel)
        frame_botoes.pack(pady=20)
        ctk.CTkButton(frame_botoes, text="Salvar", command=salvar).pack(side="left", padx=10)
        ctk.CTkButton(frame_botoes, text="Cancelar", command=toplevel.destroy).pack(side="left", padx=10)

    def filtrar_ordens(self, termo):
        filtro = termo.lower()
        dados_filtrados = [d for d in self.dados if filtro in d["cliente"].lower() or filtro in d["veiculo"].lower()]
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
