import customtkinter as ctk
from pages.login import LoginPage
from pages.dashboard import DashboardPage
from pages.ordens import OrdensPage
from pages.produtos import ProdutosPage
from pages.veiculos import VeiculosPage
from pages.clientes import ClientesPage
from pages.config import ConfigPage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("RaizTech Systems")
        self.geometry("1000x600")

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        # Mapear páginas
        self.pages = {
            'dashboard': lambda: DashboardPage(self.container, self),
            'ordens': lambda: OrdensPage(self.container, self),
            'produtos': lambda: ProdutosPage(self.container, self),
            'veiculos': lambda: VeiculosPage(self.container, self),
            'clientes': lambda: ClientesPage(self.container, self),
            'config': lambda: ConfigPage(self.container, self),
        }

        self.show_page(LoginPage)

    def show_page(self, page_class):
        for widget in self.container.winfo_children():
            widget.destroy()
        # Se for classe direta, instancia
        if isinstance(page_class, type):
            page = page_class(self.container, self)
        else:
            page = page_class()
        page.pack(fill="both", expand=True)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
