class User: 
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
mahm = User("mahmoud", "m.attieh1@outlook.com")

guido.make_deposit(90000000000000).make_deposit(10).make_deposit(5).make_withdrawal(20).display_user_balance()
monty.make_deposit(90000000000000).make_deposit(10).make_withdrawal(5).make_withdrawal(20).display_user_balance()
mahm.make_deposit(90000000000000).make_withdrawal(10).make_withdrawal(5).make_withdrawal(20).display_user_balance()