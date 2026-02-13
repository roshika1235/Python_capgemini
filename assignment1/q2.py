import logging
from math import floor
logging.basicConfig(
    filename="hospital.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class Hospital():
    consultant_fee=300
    admit_fee_per_hour=30
    admit_fee_per_day=720
    def __init__(self,pname,admitp,discharge,calbill,days_present,register):
        self.pname=pname
        self.admitp=admitp
        self.discharge=discharge
        self.calbill=calbill
        self.days_present=days_present
        self.register=register
    def display(self):
        logging.info("patient name: %s", self.pname)
        logging.info("patient admitted: %s", self.admitp)
        logging.info("patient discharge: %s", self.discharge)
        logging.info("total bill of patient: %s", self.calbill)
        logging.info("the no. of days patient present: %s", self.days_present)
        logging.info("patient register or not: %s", self.register) 
    def admitted(self,r):
        if self.register==r and r=="yes":
            print("patient admitted")
        else:
            print("not admitted ,register first")
    def discharge_patient(self):
        tot_days=floor(self.days_present)
        tot_hrs=(self.days_present-tot_days)*24
        tot_bill=(self.consultant_fee
        +floor(self.days_present)*self.admit_fee_per_day 
        + floor(tot_hrs)*self.admit_fee_per_hour)
        if self.calbill-tot_bill==0:
            logging.debug("Patient discharged %s")
        else:
            logging.warning("first pay your bill and your remaining balance is: %s",tot_bill-self.calbill)
    def cal_bill(self,tot_bill):
        tot_days=floor(self.days_present)
        tot_hrs=(self.days_present-tot_days)*24
        tot_bill=(self.consultant_fee
        +floor(self.days_present)*self.admit_fee_per_day 
        + floor(tot_hrs)*self.admit_fee_per_hour)
        if self.calbill-tot_bill==0:
            logging.debug("total bill is paid: %s",tot_bill)
        else:
            logging.warning("remaining balance: %s",tot_bill-self.calbill)
    @classmethod
    def update_consultant_fee(cls,new_consultant_fee):
        if new_consultant_fee>0:
            cls.consultant_fee=new_consultant_fee
        else:
            logging.error("consultant fee cannot be negtive %s")
h1=Hospital("rosh","yes","no",1200,2.0,"yes")
h1.display()
h1.admitted("yes")
h1.discharge_patient()
h1.cal_bill(2000)
h1.update_consultant_fee(400)
h1.discharge_patient()



