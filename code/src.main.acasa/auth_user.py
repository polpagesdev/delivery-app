from src.main.acasa.auth_type import AuthType
from src.main.acasa.db_service import DbService
from src.main.acasa.auth_service import AuthService


class AuthUser:

    def __init__(self, authService: AuthService, client_id : str):
        self.Database = DbService()
        self.authService = authService
        self.client_secret = ""
        self.client_id = client_id

    # It allows the user to get the service URL to request access to the application
    # It has next format:
        # https://acasa.com/v1/oauth/authorize?response_type=code&client_id=CLIENT_ID&redirect_uri=CALLBACK_URL&scope=read
        # client_id: identificador de l'usuari que fa login
    # CALLBACK_URL: URL a la que cridarà el OAuth2 Server per enviar la resposta (Ex: https://acasa.com/v1/oauth/response?...)
    def get_service(self, client_id: str) -> str:
        if not client_id:
            return 'Missing Client ID'

        auth_type = self.Database.get_name(client_id)

        if auth_type == 'Unregistered client':
            cr = 'Not Registered User'
        else:
            cr = self.Database.get_auth_type(client_id)

        callback_url = "https://acasa.com/v1/oauth/response?response_code={0}".format(cr)

        authentication_link = "https://acasa.com/v1/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}&scope=read".format(client_id, callback_url)

        return authentication_link




    def connect(self, authorization_code: str) -> bool:
        self.callback_url = "https://acasa.com/v1/oauth/response?access_token={0}"
        self.Token_accessible = self.authService.request_authentication(client_id=self.client_id, client_secret=self.client_secret, authorization_code=authorization_code, callback_url=self.callback_url)


        if self.Token_accessible != 'Invalid Authentication Code':
            username = self.Database.get_name(client_id=self.client_id)
            orders = self.Database.get_pending_orders(client_id=self.client_id)
            total_orders = self.Database.get_total_orders(client_id=self.client_id)

            print('Username: ', username)
            print('Pending Orders: ', orders)
            print('Total orders: ', total_orders)
            return True
        else:
            return False


        return True
