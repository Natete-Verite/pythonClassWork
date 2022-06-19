from datetime import datetime


class Account:
    def __init__(self,name,identification):
        self.balance = 0
        self.name = name
        self.identification = identification
        self.deposits = []
        self.withdrawals = []
        self.transaction_cost = 100
        self.loan_balance = 0
    def deposit(self,amount):
        if amount <=0:
            return f"Deposit amount must be greater than zero"
        else:    
            self.balance+=amount
            date = datetime.now()
            depos= {"date": date.strftime('%x'), "amount": amount, "narration": f"You deposited {amount} on {date.strftime('%x %X')}"}
            self.deposits.append(depos)
            return f"You deposited Ksh {amount} and your new balance is {self.balance} on {date.strftime('%x')}"
            
            
    def withdraw(self,amount):
        withdrawable_amount = self.balance-self.transaction_cost
        if amount <=0:
            return f"Withdraw amount must be greater than zero"       
        elif amount> withdrawable_amount:     
            return f"Insuficient funds"
        else:
            amount < self.balance
            self.balance-=amount+self.transaction_cost
            date = datetime.now() 
            withdr= {"date": date.strftime('%x'), "amount": amount, "narration": f"You withdrew {amount} on {date.strftime('%x %X')}"}
            self.withdrawals.append(withdr)
            return f"You withdrew Ksh {amount}  your new balance is {self.balance} on {date.strftime('%x')}"    

    def deposits_statement(self):
        for deposit in self.deposits:
            print(deposit)  

    def withdrawals_statement(self):
        for withdrawal in self.withdrawals:
            print(withdrawal)

    def current_balance(self):
        return f"The current balance is Ksh {self.balance}"     

    def full_statement(self):
        statement = self.deposits + self.withdrawals
        for state in statement:
            if state in self.deposits:
                print (f"{state['date']}... Deposit... {state['amount']}")
            elif state in self.withdrawals:
                 print (f"{state['date']}... Withdrawal... {state['amount']}")   

    def borrow(self,amount):
        deposit_sum=0
        for a in self.deposits:
            deposit_sum+=a["amount"]
        if amount<=0:
            return "invalid amount"
        if len(self.deposits)<10:
            return f"You can't borrow money because of few deposits made, make {10-len(self.deposits)} more deposits to qualify"
        if amount<100:
            return "You can only borrow at least 100"
        if self.balance!=0:
            return f"You have {self.balance} in your account. You are not elligible to borrow money."
        if amount> deposit_sum/3:
            return f"You are not qualified to borrow this amount. You can borrow atmost {deposit_sum/3}"
        if self.loan_balance!=0:
            return f"YOu have unpaid loan of {self.loan_balance}, first clear the loan you have to be elligible"
        else:
            interest=(3/100)*amount
            self.loan_balance+=amount+interest
            return f"You have borrowed {amount} and your loan balance to be paid is {self.loan_balance}"

    def loan_repayment(self,amount):
        if amount<=0:
            return "invalid amount"
        if amount>self.loan_balance:
            remainder=amount-self.loan_balance
            self.loan_balance=0
            return f"Your loan balance is {self.loan_balance} { self.deposit(remainder)}"
        else:
            self.loan_balance-=amount
            return f"You have paid a loan of {amount} and your current loan balance is {self.loan_balance} "        

    def transfer(self,amount,instance_name):
        if amount<=0:
            return "invalid amount"
        elif amount>=self.balance:
            return "insufficient amount"
        else:
            self.balance-=amount
            # instance_name.balance+=amount
            return f"You have transfered {amount} to account with the name of {instance_name.name}. Your new balance is {self.balance}"
