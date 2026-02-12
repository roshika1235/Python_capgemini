class BankAccount():
    bname="State Bank"
    bcode=5242
    bloc="hyd"
    min_b=200
    def __init__(self,bname,deposit=0,balance=0):
        self.bname=bname
        self.deposit=deposit
        self.balance=balance
    def new_withdraw(self,amount):
        if(amount>0):
            if self.balance-amount>BankAccount.min_b:
                print("withdraw suceessful",self.balance)
            else:
                print("exceeding min balance")
        else:
            print("invalid amount")
    def deposit_1(self,amount):
        if amount<0:
            print("")
        self.balance+=amount
        print(self.balance)
    def display_acc_details(self):
        print(self.balance,self.deposit,self.bname,self.min_b)
    @classmethod
    def min_1(cls,update_min_balance):
        cls.min_b=update_min_balance
        print(cls.min_b) 

b1=BankAccount("rosh",10,300)
b1.min_1(500)
b2=BankAccount("sir",20,200)
b1.display_acc_details()
b2.display_acc_details()
b1.new_withdraw(100)
print(b1.balance,b1.deposit)