from typing import Any

transactions = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(transactions: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция фильтрации операций по ключу"""
    new_transactions = []
    for transaction in transactions:
        if transaction.get('state') == state:
            new_transactions.append(transaction)
    return new_transactions


print(filter_by_state(transactions, 'CANCELED'))


def sort_by_date(transactions: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Фунуия сортировки операций по дате"""
    sorted_transactions = sorted(transactions, key=lambda transactions: transactions['date'], reverse=reverse)
    return sorted_transactions


print(sort_by_date(transactions))
