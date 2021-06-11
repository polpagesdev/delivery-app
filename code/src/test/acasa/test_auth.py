import pytest
from unittest.mock import MagicMock
from src.main.acasa.auth_service import AuthService
from src.main.acasa.auth_user import AuthUser


@pytest.fixture()
def auth_server():
    def _auth_server(service):
        return AuthUser(service)
    return _auth_server()


class TestAuth:

    # 1
    def test_given_an_autenticator_when_service_not_available_then_return_url_error(self) -> None:
        client_id = 'client_1'
        # Client calls service
        check_auth = get_service(client_id)
        # Check if client is signed up, and return corresponding URL
        assert check_auth is 'Error'

    # 2
    def test_given_an_autenticator_when_service_available_then_return_url_to_request_authorization(self) -> None:
        client_id = 'client_2'
        # Client calls service
        check_auth = get_service(client_id)
        # Check if client is signed up, and return corresponding URL
        assert check_auth is 'AuthURL'

    # 3
    def test_given_an_authorization_when_request_connection_then_request_authentication_method_is_called(self, service) -> None:
        client_id = 'client_2'
        mock_service = MagicMock()
        # Client calls service
        auth_code = request_authorization(get_service(client_id))
        # Connection request
        auth_server(mock_service).connect(auth_code)
        # Check if function is called once with correct parameters
        assert mock_service.request_authentication.assert_called_once_with(client_id, 'secret', auth_code,
                                                                           'CallbackURL') is True

    # 4
    def test_given_an_authorization_when_request_connection_and_authentication_fails_then_return_connection_refused(self) -> None:
        client_id = 'client_1'
        mock_service = MagicMock()
        # Client calls service
        auth_code = request_authorization(get_service(client_id))
        # Connection request
        conn = auth_server(mock_service).connect(auth_code)
        # Check if connection is refused
        assert conn is False

    # 5
    def test_given_an_authorization_when_request_connection_and_authentication_works_then_return_connection_accepted(self) -> None:
        client_id = 'client_2'
        mock_service = MagicMock()
        # Client calls service
        auth_code = request_authorization(get_service(client_id))
        # Connection request
        conn = auth_server(mock_service).connect(auth_code)
        # Check if connection is accepted
        assert conn is False

    # 6
    def test_given_an_authorization_when_request_connection_and_authentication_works_then_call_user_data_functions(self) -> None:
        client_id = 'client_2'
        mock_service = MagicMock()
        # Client calls service
        auth_code = request_authorization(get_service(client_id))
        # Connection establishment
        auth_server(mock_service).connect(auth_code)
        # Check if functions are called once with correct parameters
        assert mock_service.get_name.assert_called_once_with(client_id) is True
        assert mock_service.get_total_orders.assert_called_once_with(client_id) is True
        assert mock_service.get_pending_orders.assert_called_once_with(client_id) is True

    # 7
    def test_given_an_authorization_when_request_connection_and_authentication_fails_then_not_call_user_data_functions(self) -> None:
        client_id = 'client_1'
        mock_service = MagicMock()
        # Client calls service
        auth_code = request_authorization(get_service(client_id))
        # Connection establishment
        auth_server(mock_service).connect(auth_code)
        # Check if functions are not called if connection is refused
        assert mock_service.get_name.assert_called_once_with(client_id) is False
        assert mock_service.get_total_orders.assert_called_once_with(client_id) is False
        assert mock_service.get_pending_orders.assert_called_once_with(client_id) is False
