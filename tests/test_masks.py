from src.masks import get_mask_card_number, get_mask_account

import pytest


def test_get_mask_card_number():
    """Функция выволит маску карты"""

    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_account():
    """Функция выводит маску счета"""

    assert get_mask_account("73654108430135874305") == "** 4305"


@pytest.mark.parametrize("mask_account, result", [("73654108430135874305", "** 4305"),
                                                  ("64686473678894779589", "** 9589"),
                                                  ("", "** ")])
def test_mask_param(mask_account, result):
    assert get_mask_account(mask_account) == result


@pytest.mark.parametrize("cart_number, result", [("7000792289606361", "7000 79** **** 6361"),
                                                 ("7000792289606363", "7000 79** **** 6363"),
                                                 ("", " ** **** ")])
def test_cart_param(cart_number, result):
    assert get_mask_card_number(cart_number) == result
