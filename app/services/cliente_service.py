import requests
from urls import APIURL

req = requests(APIURL)


class ClientRequests:

    def get_clients():
        req.get("/clients")
        clientes = []
        return clientes
    
    def post_client(data):
        return
    
    def update_client(id, data):
        return 
    
    def deactive_client(id):
        return