import logging

# Logging configuration
logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BankAccount:
    # Static (Class) Properties
    BNAME = "ABC Bank"
    BRANCH = "Prayagraj"
    ADDRESS = "Civil Lines, Prayagraj"
    OFFICE_TIME = "10 AM - 4 PM"
    WORKING_DAYS = "Mon - Fri"
    MIN_ACCOUNT_BALANCE = 1000

    def __init__(self, name, balance):
        self.name = name
        if balance < BankAccount.MIN_ACCOUNT_BALANCE:
            logging.error(
                "Account creation failed for %s | Balance %s < Min Balance %s",
                name, balance, BankAccount.MIN_ACCOUNT_BALANCE
            )
            raise ValueError("Insufficient opening balance")
        self.balance = balance
        logging.info("Account created for %s with balance %s", name, balance)

    def deposit(self, amount):
        if amount <= 0:
            logging.warning("Invalid deposit amount: %s", amount)
            return
        self.balance += amount
        logging.info("Deposited %s to %s | Balance: %s", amount, self.name, self.balance)

    def withdraw(self, amount):
        if self.balance - amount < BankAccount.MIN_ACCOUNT_BALANCE:
            logging.error(
                "Withdrawal denied for %s | Min balance violation",
                self.name
            )
            return
        self.balance -= amount
        logging.info("Withdrawn %s from %s | Balance: %s", amount, self.name, self.balance)

    @staticmethod
    def bank_details():
        return f"""
                Bank Name   : {BankAccount.BNAME}
                Branch      : {BankAccount.BRANCH}
                Address     : {BankAccount.ADDRESS}
                Office Time : {BankAccount.OFFICE_TIME}
                Working Days: {BankAccount.WORKING_DAYS}
            """
    
# Usage
print(BankAccount.bank_details())

acc = BankAccount("Roshika", 2000)
acc.deposit(500)
acc.withdraw(1000)
acc.withdraw(700)