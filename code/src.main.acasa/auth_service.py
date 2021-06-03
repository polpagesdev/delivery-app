from src.main.acasa.auth_user import AuthUser
from random import random
from random import seed


class AuthService:

    def __init__(self):
        pass

    # It is used to allow the application (acasa) to request authorization to access resources from the user
    # If the user authorizes the request, it returns an authorization code, which has next format:
    # https://acasa.com/callback?code=AUTHORIZATION_CODE
    def request_authorization(self, auth_link: str) -> str:
        if auth_link == 'AuthURL':
            return 'AuthCode'
        else:
            return 'Error'

    # It is used to allow the application (acasa) to request an access token from the authorization server.
    # Request format:
    # https://acasa.com/v1/oauth/token?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=authorization_code&code=AUTHORIZATION_CODE&redirect_uri=CALLBACK_URL
    def request_authentication(self, client_id: str, client_secret: str, authorization_code: str, callback_url: str) -> str:
        token = randint(0, 9999)
        return token

    # It is used to allow the application (acasa) to refresh the token
    # Request format:
    # https://acasa.com/v1/oauth/token?access_token=ACCESS_TOKEN
    def refresh_token(self, access_token: str) -> str:
        fresh_token = randint(0, 9999)
        if fresh_token == access_token:
            fresh_token = randint(0, 9999)
        else:
            return fresh_token
