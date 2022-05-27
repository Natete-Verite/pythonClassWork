class Account:
    def __init__(self,name,balance,identification,creation_date):
        self.name = name
        self.balance = balance
        self.identification = identification
        self.creation_date = creation_date
    def deposit(self,amount):
        self.amount = amount
        self.balance+=amount
        return f"Hello {self.name}, your balance is {self.balance}"
    def withdraw(self,amount):
        self.amount = amount
        self.balance-=amount
        return f"Hello {self.name}, your balance is {self.balance}"    
        
