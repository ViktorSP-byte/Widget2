def get_mask_card_number(card_number: str) -> str:
    """Функция, маскирующая номер карты"""
    for _card in card_number:
        mask_number = card_number.replace(card_number[6:-4], "******")
        result = mask_number
    return result


card_number = "7000792289606361"


def get_mask_account(card_account: str) -> str:
    """"Функция, маскирующая номер счета"""
    for _card in card_account:
        mask_account = card_account.replace(card_account[:-4], '**')
        result = mask_account
    return result


card_account = "73654108430135874305"
