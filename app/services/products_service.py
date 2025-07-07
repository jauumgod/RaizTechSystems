from urls import APIURL
from app.services.user_service import AuthUser  # ajuste o caminho conforme sua estrutura

class ProductsRequests:

    @staticmethod
    def get_products():
        try:
            response = AuthUser.request_metodo_seguro("GET", f"{APIURL}/products/")
            if response and response.status_code == 200:
                return response.json()
            else:
                print("Erro ao buscar produtos:", response.status_code, response.text)
                return []
        except Exception as e:
            print("Erro:", e)
            return []

    @staticmethod
    def post_products(data):
        try:
            response = AuthUser.request_metodo_seguro("POST", f"{APIURL}/products/", json=data)
            if response and response.status_code in [200, 201]:
                return response.json()
            else:
                print("Erro ao criar produto:", response.status_code, response.text)
                return None
        except Exception as e:
            print("Erro:", e)
            return None

    @staticmethod
    def update_products(id, data):
        try:
            response = AuthUser.request_metodo_seguro("PUT", f"{APIURL}/products/{id}/", json=data)
            if response and response.status_code in [200, 204]:
                return True
            else:
                print("Erro ao atualizar produto:", response.status_code, response.text)
                return False
        except Exception as e:
            print("Erro:", e)
            return False

    @staticmethod
    def deactive_products(id):
        try:
            response = AuthUser.request_metodo_seguro("DELETE", f"{APIURL}/products/{id}/")
            if response and response.status_code in [200, 204]:
                return True
            else:
                print("Erro ao desativar produto:", response.status_code, response.text)
                return False
        except Exception as e:
            print("Erro:", e)
            return False
