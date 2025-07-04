import customtkinter as ctk

class FiltroFrame(ctk.CTkFrame):
    def __init__(self, parent, on_filtrar_callback=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.on_filtrar_callback = on_filtrar_callback

        self.entry = ctk.CTkEntry(self, placeholder_text="Buscar por nome ou código")
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.entry.bind("<Return>", self._on_enter)

        self.btn_filtrar = ctk.CTkButton(self, text="Filtrar", command=self._filtrar)
        self.btn_filtrar.pack(side="left")

    def _filtrar(self):
        termo = self.entry.get()
        if self.on_filtrar_callback:
            self.on_filtrar_callback(termo)

    def _on_enter(self, event):
        self._filtrar()
