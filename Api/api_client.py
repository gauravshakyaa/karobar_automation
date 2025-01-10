import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, headers=None, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, headers=None, data=None, json=None):
        response = requests.post(f"{self.base_url}{endpoint}", headers=headers, data=data, json=json)
        response.raise_for_status()
        return response.json()