import requests

class CreateKit:
    def __init__(self):
        self.base_url = 'https://d431d0f2-c0ad-4275-89d1-30517d34c220.serverhub.praktikum-services.ru/api/v1/kits/'


    def post_create_new_kit(self, body):
        response = requests.post(self.base_url, json=body)
        return response