"""Bank Account Class"""


class Account:
    """Class to represent a Bank Account"""

    def __init__(self, owner: str, balance=0):
        assert isinstance(owner, str), "owner name should be string"
        assert not isinstance(balance, str), "balance should be int or float"
        if balance < 0:
            raise "balance should not be negative"

        self.__owner = owner
        self.__balance = balance

    @property
    def owner(self):
        """Account owner name"""
        return self.__owner

    @owner.setter
    def owner(self, value: str):
        assert isinstance(value, str), "owner name should be string"
        assert value != "", "owner name should not be empty"

        self.__owner = value

    @property
    def balance(self):
        """Current account balance"""
        return self.__balance

    def deposit(self, amount: float):
        """Deposit amount to the account"""
        self.__balance += amount
        print("Deposit Accepted!!")

    def withdraw(self, amount: float):
        """Withdraw amount from the account"""
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw Accepted!!")
        else:
            print("Fund Unavailable!!")

    def __str__(self):
        return f"{self.__owner} owns this Account with current Balance {self.__balance} !"


ac1 = Account(owner="Jose", balance=500)
ac1.deposit(200)
print(ac1.balance)

ac1.withdraw(400)
print(ac1.balance)

ac1.withdraw(1000)
print(ac1)
