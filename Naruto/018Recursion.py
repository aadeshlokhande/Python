# Recursion


# def FunctionName():
#     code
#     FunctionName()
#
#
# FunctionName()


# def abc():
#     print("Hello")
#     abc()
#
# abc()


# def Abc(a):
#     if a>=1:
#         print("Hello")
#         Abc(a-1)
#
# Abc(5)

# =================================

# factorial

# 5! = 5x4x3x2x1
# 4! = 4x3x2x1

# 5! = 5x4!
# n! = n x (n-1)!

# 1! = 1
# 0! = 1

def factorial(a):
    if(a==0 or a==1):
        return 1
    else:
        return a * factorial(a-1)

a = int(input("enter a number = "))
ans = factorial(a)

print(ans)








