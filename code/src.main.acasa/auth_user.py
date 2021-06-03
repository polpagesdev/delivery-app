from src.main.acasa.auth_type import AuthType
from src.main.acasa.db_service import DbService
from src.main.acasa.auth_service import AuthService


class AuthUser:

    def __init__(self):
        pass

    # It allows the user to get the service URL to request access to the application
    # It has next format:
    # https://acasa.com/v1/oauth/authorize?response_type=code&client_id=CLIENT_ID&redirect_uri=CALLBACK_URL&scope=read
    # client_id: identificador de l'usuari que fa login
    # CALLBACK_URL: URL a la que cridarà el OAuth2 Server per enviar la resposta (Ex: https://acasa.com/v1/oauth/response?...)
    def get_service(self, client_id: str) -> str:
        auth_type = get_auth_type(client_id)
        if auth_type == 0:
            return 'Error'
        else:
            return 'AuthURL'

    def connect(self, authorization_code: str, client_id: str) -> bool:
        client_token = request_authentication(client_id, 'secret', authorization_code, 'CallbackURL')


        return True
