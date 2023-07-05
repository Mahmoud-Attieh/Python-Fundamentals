class BankAccount: 
    def __init__(self, int_rate = 0.01, balance=0):
        self.int_rate = int_rate 
        self.balance  = balance # self it is an obj
        
    def deposit(self, amount): # incr
        self.balance= self.balance+amount 
        return self
    
    def withdraw(self, amount): # dec
        self.balance = self.balance-amount
        return self

    def display_account_info(self):
        print(f'account_info : ${self.balance}')
        return self
    
    def yield_interest(self):
        self.balance = self.balance * self.int_rate
        return self

Mahmoud = BankAccount(0.05 , 1200)
Mahmoud.deposit(1200).deposit(1400).deposit(1600).withdraw(1200).yield_interest().display_account_info()

Shireen = BankAccount(0.05 , 1300)
Shireen.deposit(1300).deposit(1300).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
