class Account:
    def __init__(self,name,identification,deposits,withdrawals):
        self.balance = 0
        self.name = name
        self.identification = identification
        self.deposits = deposits
        self.withdrawals = withdrawals
        self.transaction_cost = 100
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            # return f"Hello {self.name}, you have deposited {amount} and your new balance is {self.balance}"
            self.deposits.append(amount)
            print(self.deposits)
            return f"You deposited Ksh {amount} and your new balance is {self.balance}"
        else:    
            return f"Deposit amount must be greater than zero"
            
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance-=amount
            # return f"Hello {self.name}, you have withdrawn {amount} and your new balance is {self.balance}"    
            self.withdrawals.append(amount)
            print(self.withdrawals)
            return f"You withdrew Ksh {amount}  your new balance is {self.balance}"
        elif amount <=0:
            return f"Withdraw amount must be greater than zero"    
        else:    
            return f"Insuficient funds"

    def deposits_statement(self):
        for deposit in self.deposits:
            print(f"You deposited Ksh {deposit}")  

    def withdrawals_statement(self):
        for withdrawal in self.withdrawals:
            print(f"You withdrew Ksh {withdrawal}")
        

    def withdraws(self,amount):
        if amount > 0:
            self.balance-=amount+self.transaction_cost
            return f"Hello {self.name}, you have withdrawn {amount} and your new balance is {self.balance}"
        elif amount <=0:
            return f"Withdraw amount must be greater than zero" 
        elif amount+self.transaction_cost > self.balance:
            return f"Insuficient funds"  
        elif amount == self.balance:
            return f"Insuficient funds"    
        else:    
            return f"Insuficient funds"

    def current_balance(self):
        return f"The current balance is Ksh {self.balance}"     