import os
from PIL import Image
import customtkinter as ctk
from pages.ordens import OrdensPage
from pages.produtos import ProdutosPage
from pages.veiculos import VeiculosPage
from pages.clientes import ClientesPage
from pages.config import ConfigPage

class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        ICON_ORDENS = os.path.normpath(os.path.join(BASE_DIR, "..", "assets", "icons", "ordens.png"))
        ICON_PRODUTOS = os.path.normpath(os.path.join(BASE_DIR, "..", "assets", "icons", "produtos.png"))
        ICON_VEICULOS = os.path.normpath(os.path.join(BASE_DIR, "..", "assets", "icons", "veiculos.png"))
        ICON_CLIENTES = os.path.normpath(os.path.join(BASE_DIR, "..", "assets", "icons", "clientes.png"))
        ICON_CONFIG = os.path.normpath(os.path.join(BASE_DIR, "..", "assets", "icons", "config.png"))

        img_ordens = ctk.CTkImage(light_image=Image.open(ICON_ORDENS), size=(24,24))
        img_produtos = ctk.CTkImage(light_image=Image.open(ICON_PRODUTOS), size=(24,24))
        img_veiculos = ctk.CTkImage(light_image=Image.open(ICON_VEICULOS), size=(24,24))
        img_clientes = ctk.CTkImage(light_image=Image.open(ICON_CLIENTES), size=(24,24))
        img_config = ctk.CTkImage(light_image=Image.open(ICON_CONFIG), size=(24,24))

        menu_frame = ctk.CTkFrame(self)
        menu_frame.pack(fill="x", pady=10)

        ctk.CTkButton(menu_frame, text="Ordens", image=img_ordens, compound="left",
                      command=self.abrir_ordens).pack(side="left", padx=5)
        ctk.CTkButton(menu_frame, text="Produtos", image=img_produtos, compound="left",
                      command=self.abrir_produtos).pack(side="left", padx=5)
        ctk.CTkButton(menu_frame, text="Veículos", image=img_veiculos, compound="left",
                      command=self.abrir_veiculos).pack(side="left", padx=5)
        ctk.CTkButton(menu_frame, text="Clientes", image=img_clientes, compound="left",
                      command=self.abrir_clientes).pack(side="left", padx=5)
        ctk.CTkButton(menu_frame, text="Configurações", image=img_config, compound="left",
                      command=self.abrir_config).pack(side="left", padx=5)

        ctk.CTkLabel(self, text="Bem-vindo ao Dashboard!", font=("Arial", 24)).pack(pady=50)

    def abrir_ordens(self):
        janela = ctk.CTkToplevel(self)
        janela.title("Ordens")
        janela.geometry("800x600")
        OrdensPage(janela, self.controller).pack(fill="both", expand=True)
        janela.lift()
        janela.focus_force()
        janela.grab_set()

    def abrir_produtos(self):
        janela = ctk.CTkToplevel(self)
        janela.title("Produtos")
        janela.geometry("800x600")
        ProdutosPage(janela, self.controller).pack(fill="both", expand=True)
        janela.lift()
        janela.focus_force()
        janela.grab_set()

    def abrir_veiculos(self):
        janela = ctk.CTkToplevel(self)
        janela.title("Veículos")
        janela.geometry("800x600")
        VeiculosPage(janela, self.controller).pack(fill="both", expand=True)
        janela.lift()
        janela.focus_force()
        janela.grab_set()

    def abrir_clientes(self):
        janela = ctk.CTkToplevel(self)
        janela.title("Clientes")
        janela.geometry("800x600")
        ClientesPage(janela, self.controller).pack(fill="both", expand=True)
        janela.lift()
        janela.focus_force()
        janela.grab_set()


    def abrir_config(self):
        janela = ctk.CTkToplevel(self)
        janela.title("Configurações")
        janela.geometry("800x600")
        ConfigPage(janela, self.controller).pack(fill="both", expand=True)
        janela.lift()
        janela.focus_force()
        janela.grab_set()