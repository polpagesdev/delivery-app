from src.main.acasa.auth_type import AuthType


class DbService:

    def __init__(self):
        client_1 = {'auth_type' : AuthType.NO_AUTH, 'name' : 'client no registrat', 'total_orders' : 0, 'pending_orders' : 0}
        client_2 = {'auth_type' : AuthType.OAUTH, 'name' : 'client registrat', 'total_orders' : 3, 'pending_orders' : 1}
        self.__database = {'client_1' : client_1, 'client_2' : client_2}

    def get_auth_type(self, client_id: str) -> AuthType:
        return self.__database[client_id]['auth_type']

    def get_name(self, client_id: str) -> str:
        return self.__database[client_id]['name']

    def get_total_orders(self, client_id: str) -> int:
        return self.__database[client_id]['total_orders']

    def get_pending_orders(self, client_id: str) -> int:
        return self.__database[client_id]['pending_orders']
