from unicodedata import category

from transaction import Transaction, Income, Expense

class FinanceManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_total_income(self):
        total = 0
        for income in self.transactions:
            if isinstance(income, Income):
                total += income.amount
        return total
    def get_total_expenses(self):
        total = 0
        for expense in self.transactions:
            if isinstance(expense, Expense):
                total += expense.amount
        return total

    def get_balance(self):
        balance = self.get_total_income() - self.get_total_expenses()
        return balance

    def get_expenses_by_category(self):
        categories = {}

        for expense in self.transactions:
            if isinstance(expense, Expense):
                if expense.category not in categories:
                    categories[expense.category] = 0

                categories[expense.category] += expense.amount

        return categories

    def get_most_expensive_category(self):
        categories = self.get_expenses_by_category()

        if not categories:
            return None

        return max(categories, key=categories.get)










