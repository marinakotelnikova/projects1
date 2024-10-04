from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number: str) -> str:
    """Функция маскирующая счета/карты"""
    if len(number.split()[-1]) == 16:
        return f"{number[:-16]}{get_mask_card_number(number.split()[-1])}"
    elif len(number.split()[-1]) == 20:
        return f"{number[:-20]}{get_mask_account(number.split()[-1])}"


def get_date(old_data: str) -> str:
    """Функция которая возвращает строку с датой в формате дд.мм.гггг"""
    data = old_data[0:10].split("-")
    return ".".join(data[::-1])
