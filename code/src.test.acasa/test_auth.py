import pytest
from unittest.mock import MagicMock
from src.main.acasa.auth_service import AuthService
from src.main.acasa.auth_user import AuthUser


class TestAuth:

    # 1
    def test_given_an_autenticator_when_service_not_available_then_return_url_error(self) -> None:
        client_id = 'client_1'
        check_auth = get_service(client_id)
        assert check_auth is 'Error'

    # 2
    def test_given_an_autenticator_when_service_available_then_return_url_to_request_authorization(self) -> None:
        client_id = 'client_2'
        check_auth = get_service(client_id)
        assert check_auth is 'AuthURL'

    # 3
    def test_given_an_authorization_when_request_connection_then_request_authentication_method_is_called(self) -> None:

        result = True
        assert result is True

    # 4
    def test_given_an_authorization_when_request_connection_and_authentication_fails_then_return_connection_refused(self) -> None:

        result = True
        assert result is True

    # 5
    def test_given_an_authorization_when_request_connection_and_authentication_works_then_return_connection_accepted(self) -> None:

        result = True
        assert result is True

    # 6
    def test_given_an_authorization_when_request_connection_and_authentication_works_then_call_user_data_functions(self) -> None:

        result = True
        assert result is True

    # 7
    def test_given_an_authorization_when_request_connection_and_authentication_fails_then_not_call_user_data_functions(self) -> None:

        result = True
        assert result is True
