from typing import Optional


def filter_by_state(lists_state: list, state: Optional[str]= "EXECUTED") -> list[str]:
    """Функция возвращает список словарей по ключу state с указанным значением"""

    new_lists = []
    for k in lists_state:
        if k["state"] == state:
            new_lists.append(k)
    return new_lists


def sort_by_date(det_data: list, data: bool = True) -> list:
    """Функция возвращает дату по убыванию"""

    sort_list = sorted(det_data, key=lambda x: x.get("date"), reverse=data)
    return sort_list
