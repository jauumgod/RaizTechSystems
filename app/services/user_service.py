import requests
from urls import APIURL

class AuthUser:
    access_token = None
    refresh_token = None

    @staticmethod
    def login_user(user, password):
        data = {
            "username": user,
            "password": password
        }
        try:
            response = requests.post(f"{APIURL}/login/", json=data)
            if response.status_code == 200:
                resp_json = response.json()
                AuthUser.access_token = resp_json.get("access")
                AuthUser.refresh_token = resp_json.get("refresh")
                print("Access:", AuthUser.access_token)
                print("Refresh:", AuthUser.refresh_token)
                return True
            else:
                print("Erro:", response.status_code, response.text)
                return False
        except requests.RequestException as e:
            print("Erro na conexão:", e)
            return False

    @staticmethod
    def logout_user():
        AuthUser.access_token = None
        AuthUser.refresh_token = None

    @staticmethod
    def get_headers():
        if AuthUser.access_token:
            return {"Authorization": f"Bearer {AuthUser.access_token}"}
        return {}

    @staticmethod
    def request_metodo_seguro(method, url, **kwargs):
        """
        Método que tenta a requisição com o access token,
        e caso dê 401, tenta renovar o token com refresh_token e refaz a requisição
        """
        headers = AuthUser.get_headers()
        if "headers" in kwargs:
            headers.update(kwargs["headers"])
        kwargs["headers"] = headers

        try:
            response = requests.request(method, url, **kwargs)
            if response.status_code == 401:
                print("Access token expirado, tentando refresh...")
                if AuthUser.tentar_refresh():
                    # Atualiza headers com novo access token
                    headers = AuthUser.get_headers()
                    kwargs["headers"] = headers
                    response = requests.request(method, url, **kwargs)
            return response
        except requests.RequestException as e:
            print("Erro na conexão:", e)
            return None

    @staticmethod
    def tentar_refresh():
        """
        Usa o refresh_token para obter um novo access_token
        """
        if not AuthUser.refresh_token:
            print("Sem refresh token")
            return False

        try:
            response = requests.post(f"{APIURL}/token/refresh/", json={
                "refresh": AuthUser.refresh_token
            })
            if response.status_code == 200:
                AuthUser.access_token = response.json().get("access")
                print("Novo access_token obtido:", AuthUser.access_token)
                return True
            else:
                print("Falha ao renovar token:", response.status_code, response.text)
                AuthUser.logout_user()
                return False
        except requests.RequestException as e:
            print("Erro ao tentar refresh:", e)
            return False
