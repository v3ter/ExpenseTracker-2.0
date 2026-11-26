from transaction import Income, Expense
from finance_manager import FinanceManager
from storage import save_transactions, load_transactions

manager = FinanceManager()
manager.transactions = load_transactions()

while True:
    print('\n===== ФИНАНСОВЫЙ МЕНЕДЖЕР ====')
    print('1. Добавить доход')
    print('2. Добавить расход')
    print('3. Показать баланс')
    print('4. Показать все транзакции')
    print('5. Статистика расходов')
    print('6. Выход')

    choice =  input('Выбери действие:')

    if choice == '1':
        print('Добавление дохода')

        try:
            amount = float(input('Введите сумму дохода:'))
        except ValueError:
            print('Ошибка! Нужно ввести число')
            continue

        if amount <= 0:
            print('Сумма должна быть положительной')
            continue

        category = input('Введите категорию:')
        description = input('Ведите описание:')
        date = input('Введите дату:')

        if not category or not description or not date:
            print('Ошибка, все поля должны быть заполнены.')
            continue

        income = Income(amount, category, description, date)
        manager.add_transaction(income)
        save_transactions(manager.transactions)

        print('Доход успешно добавлен')

    elif choice == '2':
        print('Добавление расхода')

        try:
            amount = float(input('Введите сумму расхода:'))
        except ValueError:
            print('Ошибка! Нужно ввести число')
            continue

        if amount <= 0:
            print('Сумма должна быть положительной')
            continue

        category = input('Введите категорию:')
        description = input('Ведите описание:')
        date = input('Введите дату:')


        if not category or not description or not date:
            print('Ошибка, все поля должны быть заполнены.')
            continue

        expense = Expense(amount, category, description, date)
        manager.add_transaction(expense)
        save_transactions(manager.transactions)

        print('Расход успешно добавлен')

    elif choice == '3':
        print('Показ баланса')

        print('Доходы:', manager.get_total_income())
        print('Расходы:', manager.get_total_expenses())
        print('Баланс:', manager.get_balance())


    elif choice == '4':
        print('Показ всех транзакций')

        for transaction in manager.transactions:
            transaction.display_info()


    elif choice == '5':
        print('Статистика расходов')



        categories = manager.get_expenses_by_category()

        for category, amount in categories.items():
            print(f'{category}, {amount}')

        most_expensive = manager.get_most_expensive_category()
        print('Самая затратная категория:', most_expensive)




    elif choice == '6':
        print('Выход из приложения')
        break

    else:
        print('Неверный выбор')


