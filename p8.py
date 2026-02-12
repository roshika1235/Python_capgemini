# class Mobile:
#     brand="samsung"
#     cost=10000
# m1=Mobile()
# print(m1.brand)
# print(m1.cost)

# class SBI:
#     bname="sbi"
#     loc="hyderabad"
# c1=SBI()
# c2=SBI()
# SBI.loc="mumbai"

# print(c1.bname)
# print(c1.loc)
# print(c2.bname)
# print(c2.loc)

# update with the help of object
# class SBI:
#     bname="sbi"
#     loc="hyderabad"
# c1=SBI()
# c2=SBI()
# # SBI.loc="mumbai"

# print(c1.bname)
# print(c1.loc)
# SBI.loc="mumbai"
# print(c2.bname)
# print(c2.loc)

# class School():
#     sname="abcschool"
#     loc="hyd"
# st1=School()
# st1.name="priya"
# st1.age=10
# print(st1.School())


# class Bank():
#     bname="sbi india"
#     bid=101
#     branchname="rr"
#     bcode=1234
# b1=Bank()
# b2=Bank()
# b3=Bank()
# b4=Bank()
# b5=Bank()

# b1.cname="priya"
# b1.cage=22
# b1.cadd="goa"
# b1.cid="r01"
# b1.cph=1234567890

# b2.cname="anu"
# b2.cage=21
# b2.cadd="hyd"
# b2.cid="r02"
# b2.cph=12345676820

# b3.cname="roshni"
# b3.cage=22
# b3.cadd="goa"
# b3.cid="r03"
# b3.cph=12347267890


# b4.cname="sneha"
# b4.cage=21
# b4.cadd="goa"
# b4.cid="r04"
# b4.cph=1234567890

# b5.cname="sindhu"
# b5.cage=22
# b5.cadd="hbj"
# b5.cid="r05"
# b5.cph=1234578231

# print(b1.bname,b1.bid,b1.branchname,b1.bcode,b1.cname,b1.cage,b1.cadd,b1.cid,b1.cph)
# print(b2.bname,b2.bid,b2.branchname,b2.bcode,b2.cname,b2.cage,b2.cadd,b2.cid,b2.cph)
# print(b3.bname,b3.bid,b3.branchname,b3.bcode,b3.cname,b3.cage,b3.cadd,b3.cid,b3.cph)
# print(b4.bname,b4.bid,b4.branchname,b4.bcode,b4.cname,b4.cage,b4.cadd,b4.cid,b4.cph)
# print(b5.bname,b5.bid,b5.branchname,b5.bcode,b5.cname,b5.cage,b5.cadd,b5.cid,b5.cph)


# class Bank():
#     bname="sbi india"
#     bid=101
#     branchname="rr"
#     bcode=1234
#     def fun(obj,bcname,bcage,bcadd,bcid,bcph):
#         obj.cname=bcname
#         obj.cage=bcage
#         obj.cadd=bcadd
#         obj.cid=bcid
#         obj.cph=bcph
#     def show(obj):
#         print(obj.bname,obj.bid,obj.branchname,obj.bcode,obj.cname,obj.cage,obj.cadd,obj.cid,obj.cph)
# b1=Bank()
# b2=Bank()
# b3=Bank()
# b4=Bank()
# b5=Bank()
# b1.cname="priya"
# b1.cage=22
# b1.cadd="goa"
# b1.cid="r01"
# b1.cph=1234567890

# b2.cname="anu"
# b2.cage=21
# b2.cadd="hyd"
# b2.cid="r02"
# b2.cph=12345676820

# b3.cname="roshni"
# b3.cage=22
# b3.cadd="goa"
# b3.cid="r03"
# b3.cph=12347267890


# b4.cname="sneha"
# b4.cage=21
# b4.cadd="goa"
# b4.cid="r04"
# b4.cph=1234567890

# b5.cname="sindhu"
# b5.cage=22
# b5.cadd="hbj"
# b5.cid="r05"
# b5.cph=1234578231

# b1.show()
# b2.show()
# b3.show()
# b4.show()
# b5.show()

# class Bank():
#     bname="sbi india"
#     bid=101
#     branchname="rr"
#     bcode=1234
#     def fun(obj,bcname,bcage,bcadd,bcid,bcph):
#         obj.cname=bcname
#         obj.cage=bcage
#         obj.cadd=bcadd
#         obj.cid=bcid
#         obj.cph=bcph
# b1=Bank()
# b1.fun("priya",22,"goa","r01",1234567890)


# b2=Bank()
# b2.fun("anu",21,"hyd","r02",12345676820)

# b3=Bank()
# b3.fun("roshni",22,"goa","r03",123472678)

# b4=Bank()
# b4.fun("sneha",21,"goa","r04",1234567890)

# b5=Bank()
# b5.fun("sindhu",22,"hbj","r05",1234578231)

# class Bank():
#     bname="sbi india"
#     bid=101
#     branchname="rr"
#     bcode=1234
#     def __init__(self,bcname,bcage,bcadd,bcid,bcph):
#         self.cname=bcname
#         self.cage=bcage
#         self.cadd=bcadd
#         self.cid=bcid
#         self.cph=bcph
#     def show(self):
#         print(self.bname,self.bid,self.branchname,self.bcode,self.cname,self.cage,self.cadd,self.cid,self.cph)
# b1=Bank("priya",22,"goa","r01",1234567890)
# b2=Bank("anu",21,"hyd","r02",12345676820)
# b3=Bank("roshni",22,"goa","r03",123472678)
# b4=Bank("sneha",21,"goa","r04",1234567890)
# b5=Bank("sindhu",22,"hbj","r05",1234578231)
# b1.show()
# b2.show()
# b3.show()
# b4.show()
# b5.show()



class Bank():
    bname="sbi india"
    bid=101
    branchname="rr"
    bcode=1234
    def __init__(self,bcname,bcage,bcadd,bcid,bcph,withdrawal=0):
        self.cname=bcname
        self.cage=bcage
        self.cadd=bcadd
        self.cid=bcid
        self.cph=bcph
        self.withdrawal=withdrawal
    def show(self):
        print(self.bname,self.bid,self.branchname,self.bcode,self.cname,self.cage,self.cadd,self.cid,self.cph,self.withdrawal)
    def change_phno(self,new_phno):
        self.cph=new_phno
    def change_name(self,new_name):
        self.cname=new_name
    def change_withdrawal(self,new_withdrawal):
        if new_withdrawal<0:
            print("can't withdraw")
            
        else:
            if new_withdrawal>self.withdrawal:
                print("insufficient balance")
            else:
                self.withdrawal-=new_withdrawal
                print("withdrawal successful")
b1=Bank("priya",22,"goa","r01",1234567890,10000)
b2=Bank("anu",21,"hyd","r02",12345676820,20000)
b3=Bank("roshni",22,"goa","r03",123472678,86)
b4=Bank("sneha",21,"goa","r04",1234567890,79)
b5=Bank("sindhu",22,"hbj","r05",1234578231,76)
# b1.show()
# b1.change_phno(9876543210)
# b1.show()
# b2.show()
# b2.change_name("sneha")
# b2.show()
b3.show()
b3.change_withdrawal(20)
b3.show()




