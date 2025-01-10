from api_client import APIClient

class AuthAPI(APIClient):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_token(self, phone, otp):
        payload = {
            "phone_number": phone,
            "otp": otp
        }
        login_endpoint = "/oauth/otp-login/"
        response = self.post(endpoint=login_endpoint, json=payload)
        if response and "token" in response:
            return response["token"]
        else:
            raise Exception("Failed to retrieve token. Response: {}".format(response))

    def get_business_list(self, token, business_name=None, business_idx = None):
        headers = {
            "Authorization": f"Token {token}"
        }
        get_business_endpoint = "/business/"
        business_list = self.get(endpoint=get_business_endpoint, headers=headers)
        results = business_list.get("results")
        for result in results:
            print(result.get('name'), result.get('idx'))

auth_api = AuthAPI("https://revamp-beta.karobarapp.com/api/v3")
token = auth_api.get_token(phone="9860725577", otp="123456")
auth_api.get_business_list(token)