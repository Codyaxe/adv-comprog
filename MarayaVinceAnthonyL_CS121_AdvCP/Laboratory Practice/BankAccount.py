
# 1. Create an abstract class BankAccount
# Private attributes: account_number, balance
# Use @property to allow read-only access to account_number and balance
# Abstract methods:
# deposit(amount)
# withdraw(amount)
# display_account_type()

# 2. Create another subclass CurrentAccount
# Inherits from BankAccount
# Allows overdraft up to a limit (-5000). In banking, an overdraft means you are allowed to withdraw more money than what you currently have in your account—up to a certain limit.
# display_account_type() returns "Current Account"

# 3. Create a subclass SavingsAccount
# Inherits from BankAccount
# Withdrawals cannot exceed balance (no overdraft). 
# display_account_type() returns "Savings Account"

# 4. Using Polymorphism, create a function print_account_details(account) that accepts any BankAccount object and prints:
# Account number
# Balance
# Account type (via display_account_type())

from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, account_number = 0, balance = 0):
        self._account_number = account_number
        self._balance = balance
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def display_account_type(self):
        pass

    @property
    def account_number(self):
        return self._account_number
    
    @property
    def balance(self):
        return self._balance

class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if super().balance - amount >= -5000:
            self._balance -= amount
            return self._balance
        else:
            print("Amount Exceeded!")
    
    def deposit(self, amount):
        self._balance += amount
    
    def display_account_type(self):
        return "Current Account"
    
class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if super().balance - amount >= 0:
            self._balance -= amount
            return self._balance
        else:
            print("Amount Exceeded!")
    
    def deposit(self, amount):
        self._balance += amount
    
    def display_account_type(self):
        return "Savings Account"

def print_account_details(account: BankAccount):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Type: {account.display_account_type()}")
    print("--------------------------")

test1 = SavingsAccount("SA123", 1200)
test2 = CurrentAccount("CA456", -200)

print_account_details(test1)
print_account_details(test2)

# test3 = SavingsAccount("SA435", 800)
# test4 = CurrentAccount("CA876", 4000)

# print_account_details(test3)
# print_account_details(test4)