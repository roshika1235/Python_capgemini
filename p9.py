import sys
# a=[1,2,3,4,5]
# print(sys.getrefcount(a))

a=10
b=20
c=30
d=10
print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.getrefcount(c))   
print(sys.getrefcount(d))