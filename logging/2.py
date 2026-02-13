import logging
logging.basicConfig(
    filename="BankAccount.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s -%(message)s"
)

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
                logging.info("withdraw suceessful %s",self.balance)
            else:
                logging.error("exceeding min balance %s")
        else:
            logging.warning("invalid amount %s")
    def deposit_1(self,amount):
        if amount<0:
            logging.warning("unable to deposit %s")
        else:
            self.balance+=amount
        print(self.balance)
    def display_acc_details(self):
        print(self.balance,self.deposit,self.bname,self.min_b)
    @classmethod
    def min_1(cls,update_min_balance):
        if update_min_balance<0:
            print("can't update")
        else:
            cls.min_b=update_min_balance
            print(cls.min_b) 
b1=BankAccount("rosh",10,300)
b1.min_1(50)
b2=BankAccount("sir",20,200)
b1.display_acc_details()
b2.display_acc_details()
b1.new_withdraw(10)
print(b1.balance,b1.deposit)

