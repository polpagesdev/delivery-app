from random import random
from random import seed
import uuid

class AuthService:

    def __init__(self):
        self.authorization_code = ""


    # It is used to allow the application (acasa) to request authorization to access resources from the user
    # If the user authorizes the request, it returns an authorization code, which has next format:
    # https://acasa.com/callback?code=AUTHORIZATION_CODE
    def request_authorization(self, auth_link: str) -> str:
        """if auth_link == 'AuthURL':
            return 'AuthCode'
        else:
            return 'Error'"""

        if "AuthType.OAUTH" in auth_link:
            authorization_code = uuid.uuid1()
            callback_url = "https://acasa.com/callback?code={0}".format(authorization_code)

            return callback_url

        else:
            print("Error: Authorization service is not acceptable")
            return 'Invalid Authorization Service'


    # It is used to allow the application (acasa) to request an access token from the authorization server.
    # Request format:
    # https://acasa.com/v1/oauth/token?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=authorization_code&code=AUTHORIZATION_CODE&redirect_uri=CALLBACK_URL
    def request_authentication(self, client_id: str, client_secret: str, authorization_code: str, callback_url: str) -> str:

        if client_id!= "" and client_secret!= "Empty" and authorization_code != "Invalid Authorization Service":
            Token_accessible = uuid.uuid1()
            callback_url = str(Token_accessible)
            return callback_url

        else:
            print("Error: Authentication code unacceptable")
            return "Invalid Authentication Code"

    # It is used to allow the application (acasa) to refresh the token
    # Request format:
    # https://acasa.com/v1/oauth/token?access_token=ACCESS_TOKEN
    def refresh_token(self, access_token: str) -> str:
        fresh_token = random(0, 9999)
        if fresh_token == access_token:
            fresh_token = random(0, 9999)
        else:
            return fresh_token
