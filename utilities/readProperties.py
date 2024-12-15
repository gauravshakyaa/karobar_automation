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
        browser = config.get("Basic Info", "chrome")
        return browser
