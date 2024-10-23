from src.widget import mask_account_card, get_date


def test_mask_account_crt() -> None:
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

    assert mask_account_card("Счет 64686473678894779589") == "Счет ** 9589"


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

    assert get_date("") == ""

