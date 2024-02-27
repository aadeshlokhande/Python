# inline

# lambda - inline function
# def abc(a):
#     ans = a*a 
#     return ans

# abc = lambda x,y : print(x+y)
# abc(110,230)

# ---------------------------
# list comprehension

# l1 = []
# for i in range(1,101):
#     l1.append(i)

# print(l1)

# [var for var in collectionOfData]
# [var for var in collectionOfData if condition]

# l1 = [f"i love you {i}" for i in range(1,101)]
# print(l1)

# l1 = [i for i in range(1,101) if i%2==0]
# print(l1)

# dic = {a:a*a for a in range(1,11) }
# print(dic)

# trueStatement if condition else FalseStatements

# age = int(input("enter your age = "))
# print("you can drive") if age>18 else print("you cant drive")

# if(age>0 and age<75):
#     if(age>18):
#         print("you can drive")
#     else:
#         print("you can't drive")
# else:
#     print("invalid age")


# (print("you can drive") if(age>18) else print("you can't drive")) if(age>0 and age<75) else print("invalid age")

# and 
# or 
# not
# && 
# if(condition1 or condition2):
