import requests
from urls import APIURL
from app.services.user_service import AuthUser  # ajuste para o seu caminho real

class ClientRequests:

    @staticmethod
    def get_clients():
        try:
            response = AuthUser.request_metodo_seguro("GET", f"{APIURL}/clients/")
            if response and response.status_code == 200:
                return response.json()
            else:
                print("Erro ao buscar clientes:", response.status_code, response.text)
                return []
        except Exception as e:
            print("Erro:", e)
            return []

    @staticmethod
    def post_client(data):
        try:
            response = AuthUser.request_metodo_seguro("POST", f"{APIURL}/clients/", json=data)
            if response and response.status_code in [200, 201]:
                return response.json()
            else:
                print("Erro ao criar cliente:", response.status_code, response.text)
                return None
        except Exception as e:
            print("Erro:", e)
            return None

    @staticmethod
    def update_client(id, data):
        try:
            response = AuthUser.request_metodo_seguro("PUT", f"{APIURL}/clients/{id}/", json=data)
            if response and response.status_code in [200, 204]:
                return True
            else:
                print("Erro ao atualizar cliente:", response.status_code, response.text)
                return False
        except Exception as e:
            print("Erro:", e)
            return False

    @staticmethod
    def deactive_client(id):
        try:
            response = AuthUser.request_metodo_seguro("DELETE", f"{APIURL}/clients/{id}/")
            if response and response.status_code in [200, 204]:
                return True
            else:
                print("Erro ao desativar cliente:", response.status_code, response.text)
                return False
        except Exception as e:
            print("Erro:", e)
            return False
