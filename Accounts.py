class Account:
    def __init__(self, name, balance=0):
        self.__account_name = name
        self.__account_balance = balance
        self.set_balance(self.__account_balance)

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name

    def set_balance(self, value):
        if value < 0:
            self.__account_balance = 0
        else:
            self.__account_balance = value


class SavingAccount(Account):
    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name):
        super().__init__(name, SavingAccount.MINIMUM)
        self.__deposit_count = 0

    def apply_interest(self):
        super().deposit(super().get_balance() * SavingAccount.RATE)

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            super().deposit(amount)
            self.__deposit_count += 1
            if self.__deposit_count == 5:
                self.__deposit_count -= 5
                self.apply_interest()

    def withdraw(self, amount):
        if super().get_balance() - amount >= 100:
            super().withdraw(amount)
