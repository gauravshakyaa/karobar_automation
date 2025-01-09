from api_client import APIClient


class AuthAPI(APIClient):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_token(self, phone, otp):
        req