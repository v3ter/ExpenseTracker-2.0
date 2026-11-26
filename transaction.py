class Transaction:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def display_info(self):
        print(self.amount, self.category, self.description, self.date)

    def get_type(self):
        return "Транзакция"

    def to_dict(self):
        return {
            "сумма": self.amount,
            "категория": self.category,
            "описание": self.description,
            "дата": self.date,
            "тип": self.get_type()
        }


class Income(Transaction):
    def get_type(self):
        return "Доход"

    def display_info(self):
        print(f'Тип: {self.get_type()}')
        super().display_info()


class Expense(Transaction):
    def get_type(self):
        return "Расход"

    def display_info(self):
        print(f'Тип: {self.get_type()}')
        super().display_info()


