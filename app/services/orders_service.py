from urls import APIURL
from app.services.user_service import AuthUser  # ajuste o import para o seu projeto

class OrdensRequests:

    @staticmethod
    def get_ordens():
        try:
            response = AuthUser.request_metodo_seguro("GET", f"{APIURL}/ordens/")
            if response and response.status_code == 200:
                return response.json()
            else:
                print("Erro ao buscar ordens:", response.status_code, response.text)
                return []
        except Exception as e:
            print("Erro:", e)
            return []

    @staticmethod
    def post_ordens(data):
        try:
            response = AuthUser.request_metodo_seguro("POST", f"{APIURL}/ordens/", json=data)
            if response and response.status_code in [200, 201]:
                return response.json()
            else:
                print("Erro ao criar ordem:", response.status_code, response.text)
                return None
        except Exception as e:
            print("Erro:", e)
            return None

    @staticmethod
    def update_ordens(id, data):
        try:
            response = AuthUser.request_metodo_seguro("PUT", f"{APIURL}/ordens/{id}/", json=data)
            if response and response.status_code in [200, 204]:
                return True
            else:
                print("Erro ao atualizar ordem:", response.status_code, response.text)
                return False
        except Exception as e:
            print("Erro:", e)
            return False

    @staticmethod
    def deactive_ordens(id):
        try:
            response = AuthUser.request_metodo_seguro("DELETE", f"{APIURL}/ordens/{id}/")
            if response and response.status_code in [200, 204]:
                return True
            else:
                print("Erro ao desativar ordem:", response.status_code, response.text)
                return False
        except Exception as e:
            print("Erro:", e)
            return False
