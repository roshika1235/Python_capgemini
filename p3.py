# import copy
import re
# # print("hello")
# a=[1,2,3]
# # b=copy.copy(a)
# # a.append(4)
# # print(a)
# # print(b)

# c=copy.deepcopy(a)
# a.append(5)
# print(a)
# print(c)
# str1="roshika is good girl"
# print(str1[4:15])
# print(str1[0:20:2])
# print(str1[::-1])
# print(str1[:5]) # only first 5 characters
# print(str1[5:]) #remaining characters after 5th index
# print(str1[:-5]) # all characters except last 5 characters
# print(str1[-5:]) # last 5 characters
# str2="bvrit college of engineering"
# print(str2[:-8])
# print(str2[-13:-8])
# print(str2[-11:])
# print(str2[:-12:-1])

# print(str2[0:5])
# print(str2[:-23])
# print(str2[17:])
# print(str2[17:28])
# print(str2[-11:])

# print(2,3,4,sep='@')
# print(10,sep='&')
# print(1,2,3,end='#')
# print("")
# print(1,2,3,4,sep='\t',end='#')
# print("")
# print(1,2,3,4,sep=' ',end='\n')
# print(1,2,3,4,sep='\t',end='#')
# x=print("hello")
# print(x) 
# var=[i for i in range(1,6)]
# print(var)
# var2=[i for i in range(1,10) if i%2!=0 ]
# print(var2)
# var3=[i**2 if i%2==0 else i**3 for i in range(1,11)]
# print(var3)
# input="python is very very easy language"
# # output=[(i[0:],len(i)) for i in input.split()]
# output=[(i[0:]) for i in input.split()]
# print(output)

# dict1={i:i**2 for i in range(1,6)}
# print(dict1)
# dict2={i:i*2 for i in range(1,10) if i%2!=0}
# print(dict2)
# dict3={i:i*2 if i%2==0 else i*3 for i in range(1,10)}
# print(dict3)
# input="Hai HeLLO"
# output={i:ord(i) for i in input if i.isupper()}
# print(output)
# print(dir(re))
# help(re)
# import keyword
# print(keyword.kwlist)
# ip2="python is yrev easy"
# ip3=re.compile(ip2)
# if(re.search("very",ip3)):
#     print("found")
#print(re.search("easy",ip2))
# m=re.search(r"\d+","age  is 22 ")
# m=re.search(r"(\d+)-(\d+)","2023-2024" )  
# print(m.group())
print(re.search(r"colou?r","color"))
print(re.search(r"\d{4}","2026"))
print(re.search(r"\d{2,4}","id: 12345"))