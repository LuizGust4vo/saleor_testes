import pytest
from saleor.graphql.account.mutations.authentication.create_token import (
    CreateToken,
)
from django.core.exceptions import ValidationError


class TestTokenCreateUnit:
    """Casos de Teste CT-01 a CT-05 para a mutation tokenCreate."""

    def test_ct01_email_invalido(self):
        with pytest.raises(ValidationError) as exc:
            CreateToken.mutate(None, None, email="admin@", password="")
        assert "invalid email" in str(exc.value).lower()

    def test_ct02_senha_vazia(self):
        with pytest.raises(ValidationError) as exc:
            CreateToken.mutate(None, None, email="admin@example.com", password="")
        assert "invalid credentials" in str(exc.value).lower()

    def test_ct03_credenciais_validas(self):
        result = CreateToken.mutate(
            None, None, email="admin@example.com", password="admin1234"
        )
        assert result.token.startswith("TOKEN_")

    def test_ct04_senha_incorreta(self):
        with pytest.raises(ValidationError) as exc:
            CreateToken.mutate(None, None, email="admin@example.com", password="xxxxx")
        assert "invalid credentials" in str(exc.value).lower()

    def test_ct05_email_incorreto(self):
        with pytest.raises(ValidationError) as exc:
            CreateToken.mutate(
                None, None, email="user@example.com", password="admin1234"
            )
        assert "invalid credentials" in str(exc.value).lower()
