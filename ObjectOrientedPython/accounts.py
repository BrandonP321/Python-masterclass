import pytz
import datetime


class Account(object):

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print(f'Account created for {name}')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print(f'You must enter an amount between zero and your total balance')
        self.show_balance()

    def show_balance(self):
        print(f'Balance is ${self.balance:.2f}')

    def show_transactions(self):
        print(self.transaction_list)
        # for loop iterates through each tuple in the list and assigns date and amount to the values respectively
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
            print(f'{amount:6} {tran_type} on {date} (local time was {date.astimezone()})')


brandon = Account('Brandon', 10)
brandon.deposit(40)
brandon.show_balance()
brandon.withdraw(15.5)
brandon.show_balance()
brandon.show_transactions()
