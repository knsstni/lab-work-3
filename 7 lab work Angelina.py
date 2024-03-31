class BankAccount:
    def __init__(self, owner_name, account_number, initial_balance):
        self._owner_name = owner_name
        self._account_number = account_number
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Deposit of {} successful.".format(amount))
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print("Withdrawal of {} successful.".format(amount))
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount for withdrawal.")

    def __str__(self):
        return "Owner's Name: {}\nAccount Number: {}\nBalance: {}".format(self._owner_name, self._account_number, self._balance)

class SavingAccount(BankAccount):
    def __init__(self, owner_name, account_number, initial_balance, interest_rate):
        super().__init__(owner_name, account_number, initial_balance)
        self._interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * (self._interest_rate / 100)
        self.deposit(interest)

if __name__ == "__main__":
    # Create a regular bank account
    account1 = BankAccount("Nursultan", "123456789", 1000000)
    print(account1)
    account1.deposit(5000000000)
    account1.withdraw(200000)
    print(account1)

    # Create a savings account
    saving_account = SavingAccount("Angelina", "987654321", 20000, 5)
    print(saving_account)
    saving_account.add_interest()
    print(saving_account)
