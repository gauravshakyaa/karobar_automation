import configparser

config = configparser.ConfigParser()
config.read("Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get("Basic Info", "baseURL")
        return url

    @staticmethod
    def getPhoneNumber():
        phone = config.get("Basic Info", "phoneNumber")
        return phone

    @staticmethod
    def getOTP():
        otp = config.get("Basic Info", "otp")
        return otp

    @staticmethod
    def getBrowser():
        browser = config.get("Basic Info", "browser")
        return browser
    
    @staticmethod
    def get_API_URL():
        return config.get("API", "BASE_URL")

    @staticmethod
    def get_otp_request_url():
        endpoint = config.get("AUTH", "OTP_REQUEST")
        return endpoint

    @staticmethod
    def get_otp_login_url():
        endpoint = config.get("AUTH", "OTP_LOGIN")
        return endpoint

    @staticmethod
    def get_user_info_url():
        endpoint = config.get("USER", "GET_USER_INFO")
        return endpoint

    @staticmethod
    def get_update_user_info_url():
        endpoint = config.get("USER", "UPDATE_USER_INFO")
        return endpoint
