class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self


class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    


Mahmoud=User("Mahmoud ", "m.attieh1@outlook.com")
Mahmoud.account.deposit(20000000).display_account_info()
