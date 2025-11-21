# test_ciclo1_global_userID.py

"""
import pytest

from src.mutations import (
    build_user_global_id,
)


def test_build_user_global_id_returns_non_empty_string():

    user_pk = 1

    result = build_user_global_id(user_pk)

    assert isinstance(result, str)
    assert result != ""
"""

import base64
from saleor.graphql.account.mutations.account.account_register import (
    build_user_global_id,
)


def test_build_user_global_id_returns_non_empty_string():
    user_pk = 1

    result = build_user_global_id(user_pk)

    assert isinstance(result, str)

    assert result != ""

    expected_raw = "User:1".encode()
    expected_b64 = base64.b64encode(expected_raw).decode()
    assert result == expected_b64
