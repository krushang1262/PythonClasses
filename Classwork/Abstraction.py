from abc import ABC, abstractmethod

class Account(ABC):
    balance = 0
    
    @abstractmethod
    def deposit(self,amt):
        pass
    
    @abstractmethod
    def withdraw(self,amt):
        pass
    
    def checkBalance(self):
        print(f"current balance is {self.balance}")
        
class SavingAccount(Account):
    
    def deposit(self, amt):
        self.balance += amt
        
    def withdraw(self, amt):
       if amt > self.balance:
           print("insuffcient balance")
       else:
           self.balance -= amt
           
# s = SavingAccount()
# s.deposit(5000)
# s.withdraw(4000)
# s.withdraw(1000)
# s.checkBalance()

class Loan(Account):
    def deposit(self, amt):
        if amt > self.balance:
            print("amount is greater than loan amount")
        else:
            self.balance -= amt
    
    def withdraw(self, amt):
        self.balance += amt
        
l = Loan()
l.withdraw(10000)
l.deposit(5000)
l.withdraw(50000)
l.deposit(55000)

l.checkBalance()