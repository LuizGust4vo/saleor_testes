# test_ciclo2_register_user.py

"""
from src.mutations import account_register

def test_account_register_populates_user_id_on_success():
    email = "user@example.com"
    password = "StrongPass123"

    response = account_register(email, password)

    assert response["errors"] == []

    user = response["user"]
    assert user is not None

    assert user["id"] != ""
"""

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


def test_account_register_populates_user_id_on_success(api_client, db):
    variables = {
        "input": {"email": "novo_usuario@example.com", "password": "SenhaForte123!"}
    }

    response = api_client.post_graphql(ACCOUNT_REGISTER_MUTATION, variables)
    content = get_graphql_content(response)

    data = content["data"]["accountRegister"]

    assert data["errors"] == []

    user = data["user"]
    assert user is not None

    assert user["id"] != ""
    assert user["email"] == "novo_usuario@example.com"
