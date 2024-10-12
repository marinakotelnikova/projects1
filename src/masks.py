def get_mask_card_number(card_number: str) -> str:
    """Функция корая пинимает на вход номер карты и выдает маску
    в формате xxxx xx** **** xxxx, где x-это цифра номера"""

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция корая пинимает на вход номер счета и выдает маску
    в формате ** xxxx, где x-это цифра счета"""

    return f"** {account_number[-4:]}"
