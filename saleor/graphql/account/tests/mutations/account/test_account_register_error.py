# test_ciclo3_error.py

"""
from unittest.mock import patch
from src.mutations import account_register

def test_account_register_does_not_generate_id_on_error():

    email = ""
    password = "StrongPass123"

    with patch("src.mutations.build_user_global_id") as mock_build:
        response = account_register(email, password)

    assert response["errors"] != []

    assert response["user"] is None

    mock_build.assert_not_called()
"""

from unittest.mock import patch
from saleor.graphql.tests.utils import get_graphql_content

ACCOUNT_REGISTER_MUTATION = """
mutation Register($input: AccountRegisterInput!) {
  accountRegister(input: $input) {
    errors {
      field
      message
    }
    user {
      id
      email
    }
  }
}
"""


def test_account_register_does_not_generate_id_on_error(api_client, db):
    variables = {"input": {"email": "", "password": "Senha123!"}}

    with patch(
        "saleor.graphql.account.mutations.account_register.build_user_global_id"
    ) as mock_id:
        response = api_client.post_graphql(ACCOUNT_REGISTER_MUTATION, variables)
        content = get_graphql_content(response)
        data = content["data"]["accountRegister"]

    assert data["errors"] != []

    assert data["user"] is None

    mock_id.assert_not_called()
