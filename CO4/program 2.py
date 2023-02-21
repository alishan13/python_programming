class bank:
    def __init__(self):
        self.acc_no=int(input("enter the account number"))
        self.acc_name=input("enter the name")
        self.acc_type=input("enter account type:")
        self.balance=0
    def deposit(self,amt):
        self.balance=self.balance+amt
        return(self.balance)
    def withdraw(self,amt):
        if self.balance>amt:
            self.balance=self.balance-amt
            return(self.balance)
        else:
            print("insufficient balance")
    def disp(self):
        print("Account Number : ",self.acc_no)
        print("Name : ",self.acc_name)
        print("Account type : ",self.acc_type)
        print("Current balance : ",self.balance)
new=bank()
c=0
while c!=4:
    c=int(input("enter the choice \n1.deposit \n2.withdraw \n3.display "))
    if c==1:
        amt=int(input("enter the amount"))
        print("current balance",new.deposit(amt))
    elif c==2:
        amt=int(input("enter the amount to be withdraw"))
        print("current balance",new.withdraw(amt))
    elif c==3:
        print("Account details are:")
        new.disp()
    else:
        print("invalid")
print("thank you for using Atm")
    
    
