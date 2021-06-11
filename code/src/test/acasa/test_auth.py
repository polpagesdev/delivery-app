import pytest
from unittest.mock import MagicMock
from src.main.acasa.auth_service import AuthService
from src.main.acasa.auth_user import AuthUser


@pytest.fixture()
def auth_server():
    def _auth_server(service, client_id):
        return AuthUser(service, client_id)
    return _auth_server


class TestAuth:

    # 1
    def test_given_an_autenticator_when_service_not_available_then_return_url_error(self, auth_server) -> None:
        #Donat un client que sol·licita un servei, quan el client no està registrat, retornar URL error
        client_id = 'client_1'

        callback_url = "https://acasa.com/v1/oauth/response?response_code=AuthType.NO_AUTH"

        authentication_link = "https://acasa.com/v1/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}&scope=read".format(client_id, callback_url)

        authentication_service = MagicMock(return_value = authentication_link)

        new_authentication_link = auth_server(authentication_service, client_id).get_service(client_id)

        assert new_authentication_link == authentication_link




    # 2
    def test_given_an_autenticator_when_service_available_then_return_url_to_request_authorization(self, auth_server) -> None:
        #Donat un client que sol·licita un servei, quan el client està registrat, retornar URL per demanar autorització
        client_id = 'client_2'

        callback_url = "https://acasa.com/v1/oauth/response?response_code=AuthType.OAUTH"

        authentication_link = "https://acasa.com/v1/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}&scope=read".format(client_id, callback_url)

        authentication_service = MagicMock(return_value = authentication_link)

        new_authentication_link = auth_server(authentication_service, client_id).get_service(client_id)

        assert new_authentication_link == authentication_link

    # 3
    def test_given_an_authorization_when_request_connection_then_request_authentication_method_is_called(self, auth_server) -> None:
        #Donat un client que sol·licita un servei, quan es fa una petició de connexió, comprovar que es crida a la funció ***request_authentication***  una sola vegada amb els paràmetres adequats
        client_id = 'client_2'
        auth_service_from_Mock = MagicMock()
        user_authentication = auth_server(auth_service_from_Mock, client_id)
        authentication_link = user_authentication.get_service(client_id)
        user_authentication.authService.request_authentication = MagicMock()
        code_for_authentication = auth_service_from_Mock.request_authorization(authentication_link)
        user_authentication.connect(code_for_authentication)
        user_authentication.authService.request_authentication.assert_called_once_with(client_id=user_authentication.client_id, client_secret= user_authentication.client_secret, authorization_code= code_for_authentication, callback_url=user_authentication.callback_url )

    # 4
    def test_given_an_authorization_when_request_connection_and_authentication_fails_then_return_connection_refused(self, auth_server) -> None:
        #Donat un client que sol·licita un servei, quan es fa una petició de connexió, i l'autenticació falla, respondre que la connexió ha estat refusada
        client_id = 'client_1'
        authentication_service =AuthService()
        user_authentication = auth_server(authentication_service, client_id)
        authentication_link = user_authentication.get_service(client_id)
        code_for_authentication= authentication_service.request_authorization(authentication_link)
        correct = user_authentication.connect(code_for_authentication)
        assert correct is False
    # 5
    def test_given_an_authorization_when_request_connection_and_authentication_works_then_return_connection_accepted(self, auth_server) -> None:
        #Donat un client que sol·licita un servei, quan es fa una petició de connexió, i l'autenticació funciona, respondre que la connexió ha estat acceptada
        client_id = 'client_2'
        authentication_service = AuthService()
        user_authentication = auth_server(authentication_service, client_id)
        authentication_link = user_authentication.get_service(client_id)
        code_for_authentication = authentication_service.request_authorization(authentication_link)
        correct = user_authentication.connect(code_for_authentication)
        assert correct is True

    # 6
    def test_given_an_authorization_when_request_connection_and_authentication_works_then_call_user_data_functions(self, auth_server) -> None:
        #Donat un client que sol·licita un servei, quan el client ja està autenticat i el token està vigent, comprovar que es crida a les funcions get_name, get_total_orders, get_pending_orders una sola vegada amb els paràmetres adequats
        client_id = 'client_2'
        authentication_service = AuthService()
        user_authentication = auth_server(authentication_service, client_id)
        authentication_link = user_authentication.get_service(user_authentication.client_id)
        code_for_authentication = authentication_service.request_authorization(authentication_link)
        correct = user_authentication.connect(code_for_authentication)
        user_authentication.Database=MagicMock()
        user_authentication.connect(code_for_authentication)
        user_authentication.Database.get_name.assert_called_once_with(client_id= user_authentication.client_id)
        user_authentication.Database.get_pending_orders.assert_called_once_with(client_id=user_authentication.client_id)
        user_authentication.Database.get_total_orders.assert_called_once_with(client_id=user_authentication.client_id)

    # 7
    def test_given_an_authorization_when_request_connection_and_authentication_fails_then_not_call_user_data_functions(self, auth_server) -> None:
        #Donat un client que sol·licita un servei, quan es fa una petició de connexió, i l'autenticació falla, comprovar que no es crida a les funcions get_name, get_total_orders, get_pending_orders una sola vegada amb els paràmetres adequats
        client_id = 'client_1'
        authentication_service = AuthService()
        user_authentication = auth_server(authentication_service, client_id)
        authentication_link = user_authentication.get_service(user_authentication.client_id)
        code_for_authentication = authentication_service.request_authorization(authentication_link)
        correct = user_authentication.connect(code_for_authentication)
        user_authentication.Database = MagicMock()
        user_authentication.connect(code_for_authentication)
        user_authentication.Database.get_name.assert_not_called()
        user_authentication.Database.get_pending_orders.assert_not_called()
        user_authentication.Database.get_total_orders.assert_not_called()
