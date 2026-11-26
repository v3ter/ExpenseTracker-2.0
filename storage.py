import json

from transaction import Income, Expense



def save_transactions(transactions):
    data = []

    for transaction in transactions:
        item = transaction.to_dict()
        item['тип'] = transaction.get_type()
        data.append(item)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_transactions():
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    transactions = []


    for item in data:
        if item['тип'] == 'Доход':
            transactions.append(Income(
                amount=item['сумма'],
                category=item['категория'],
                description=item['описание'],
                date = item['дата']
            ))

        elif item['тип'] == 'Расход':
            transactions.append(Expense(
                amount=item['сумма'],
                category=item['категория'],
                description=item['описание'],
                date=item['дата']
            ))
    return transactions



