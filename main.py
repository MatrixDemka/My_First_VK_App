import requests
from pprint import pprint
import json


#token_vk =
#token_ya =


class VK_API_Client:
    def __init__(self, token, version="5.131"):
        self.base_url = "https://api.vk.com/method/"
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }

    def user_info(self, user_id):
        url_user = f"{self.base_url}users.get"
        params = {
            "user_ids": user_id
        }
        response = requests.get(url_user, params={**self.params, **params})
        return response.json()

    def get_photos(self, user_id):
        url_get = f"{self.base_url}photos.get"
        params = {
            "owner_id": user_id,
            "album_id": "profile",
            "extended": 1,
            "photo_size": 1
        }
        response = requests.get(url_get, params={**self.params, **params})
        return response.json()


class YA_API_Client:
    def __init__(self, token):
        self.base_url = "https://cloud-api.yandex.net/v1/disk/"
        self.token = token

    def create_folder(self):
        url_create_folder = f"{self.base_url}resources"
        params = {
            "path": "/Photos_VK"
        }
        headers = {
            "Authorization": f"OAuth {self.token}"
        }
        response = requests.put(url_create_folder, params=params, headers=headers)

    def upload(self):
        url_upload = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {
            "path": "Photos_VK/"
        }
        headers = {
            "Authorization": f"OAuth {self.token}"
        }
        response = requests.get(url_upload, params=params, headers=headers)
        upload_link = response.json()["href"]


vk_client = VK_API_Client(token_vk)
ya_client = YA_API_Client(token_ya)

get_photos = vk_client.get_photos(140088998)
pprint(get_photos)




