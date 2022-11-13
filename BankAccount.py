class Account:

    def __init__(self):
        pass
    def title(self):
        print("Ashish")
    def balance(self):
        print("5000")

class SavingsAccount(Account):

    def __init__(self):
        pass
    def interestRate(self):
        print("5%")
    
x=SavingsAccount()
x.title()
x.balance()
x.interestRate()
print("______________________________________________________")
x=Account()
x.title()
x.balance()