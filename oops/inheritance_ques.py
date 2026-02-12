class Result10th():
    def __init__(self,sname,phno,email,pass_yr10,class_n):
        self.sname=sname
        self.phno=phno
        self.email=email
        self.pass_yr10=pass_yr10
        self.class_n=class_n
    def display(self):
        print(self.sname,self.phno,self.email,self.pass_yr10,self.class_n)
class Result12th(Result10th):
    def __init__(self,sname,phno,email,pass_yr10,class_n,pass_yr12,percent_12):
        super().__init__(sname,phno,email,pass_yr10,class_n) 
        self.pass_yr12=pass_yr12
        self.percent_12=percent_12
    def display(self):
        super().display()
        print(self.pass_yr12,self.percent_12)
class ResultIBE(Result12th):
    def __init__(self,sname,phno,email,pass_yr10,class_n,pass_yr12,percent_12,branch,university,be_percent):
        super().__init__(sname,phno,email,pass_yr10,class_n,pass_yr12,percent_12)
        self.branch=branch
        self.university=university
        self.be_percent=be_percent
    def display(self):
        super().display()
        print(self.branch,self.university,self.be_percent)
b0=ResultIBE("roshika",8426102882,"roshika@gmail.com",2020,"10-b","2022",95.5,"IT","JNTUH",81)
b0.display()


