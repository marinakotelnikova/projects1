from src.masks import get_mask_card_number

print(get_mask_card_number("7000792289606361"))


from src.masks import get_mask_account

print(get_mask_account("73654108430135874305"))


from src.widget import mask_account_card

print(mask_account_card("Maestro 1596837868705199" ))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))


from src.widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))
