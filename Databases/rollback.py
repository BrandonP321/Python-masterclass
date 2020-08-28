class Account(object):

    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = opening_balance
        print(f"Account created for {self.name}. ", end='')
        self.show_balance()

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print(f"{amount} deposited")
        return self._balance

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn")
            return amount
        else:
            print("The amount must be greater that zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print(f"Balance on account {self.name} is {self._balance}")


if __name__ == '__main__':
    john = Account('John')
    john.deposit(10.10)
    john.deposit(.10)
    john.deposit(.10)
    john.withdraw(.30)
    john.withdraw(0.0)
    john.show_balance()
"""Notice the rounding error when the balance is shown, refer to rollback2.py to see how to fix this
   Optimal option would be to create a class that uses cents, not dollars and then divides by 100 to show $x.xx"""
