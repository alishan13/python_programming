class BankAcc:
    def __init__(self,acc_no,name,acc_type,balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
    def withdraw(self,amount):
        try:
            self.balance -= amount
            print(f"{amount} withdrawn, Balance : {self.balance}")
        except:
            print("cant withdraw")
    def deposit(self,amount):
        try:
            self.balance += amount
            print(f"{amount} Deposited, Balance : {self.balance}")
        except:
            print("Cant deposit")
    def balanceAmt(self):
        print(f"Acc Balance : {self.balance}")
        
ac1 = BankAcc(12,"alishan","saving",10000)
print(f"Acc_no : {ac1.acc_no}")
print(f"Acc_holder name: {ac1.name}")
print(f"Acc_type : {ac1.acc_type}")
ac1.balanceAmt()
ac1.deposit(2000)
ac1.withdraw(5000)