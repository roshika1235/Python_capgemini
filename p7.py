# x=10
# def fun():
#     global x
#     x=x+10
#     print("value of x:",x)

# fun()
# print("value of x:",x)


# def demo():
#     a=5
#     print("value of a:",a)
# demo()  
# # print("value of a:",a)

#method 1
# global x
# x=10
# def out():
#     global x
#     x=10
#     def inn():
#         global x
#         x*=5
#     inn()
#     print("value of x:",x)
# out()
# print("value of x:",x)

#method 2
# def out():
#     x=10
#     def inn():
#         nonlocal x
#         x*=5
#     inn()
#     print("value of x:",x)
# out()
# print("value of x:",x)


