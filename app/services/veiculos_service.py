import requests
from urls import APIURL
from app.services.user_service import AuthUser  # ajuste para seu import real

class VeiculosRequests:

    @staticmethod
    def get_veiculos():
        try:
            response = AuthUser.request_metodo_seguro("GET", f"{APIURL}/veiculos/")
            if response and response.status_code == 200:
                return response.json()
            else:
                print("Erro ao buscar veículos:", response.status_code, response.text)
                return []
        except Exception as e:
            print("Erro:", e)
            return []

    @staticmethod
    def post_veiculos(data):
        try:
            response = AuthUser.request_metodo_seguro("POST", f"{APIURL}/veiculos/", json=data)
            if response and response.status_code in [200, 201]:
                return response.json()
            else:
                print("Erro ao criar veículo:", response.status_code, response.text)
                return None
        except Exception as e:
            print("Erro:", e)
            return None

    @staticmethod
    def update_veiculos(id, data):
        try:
            response = AuthUser.request_metodo_seguro("PUT", f"{APIURL}/veiculos/{id}/", json=data)
            if response and response.status_code in [200, 204]:
                return True
            else:
                print("Erro ao atualizar veículo:", response.status_code, response.text)
                return False
        except Exception as e:
            print("Erro:", e)
            return False

    @staticmethod
    def deactive_veiculos(id):
        try:
            response = AuthUser.request_metodo_seguro("DELETE", f"{APIURL}/veiculos/{id}/")
            if response and response.status_code in [200, 204]:
                return True
            else:
                print("Erro ao desativar veículo:", response.status_code, response.text)
                return False
        except Exception as e:
            print("Erro:", e)
            return False
