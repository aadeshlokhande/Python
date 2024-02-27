# Nested if else 

# if condition:
#     code
#     if condition:
#         code
#     else:
#         code
# else:
#     code 
#     if condition:
#         code
#     else:
#         code


# a = 20
# if(a==20):
#     print("Hello")





# age = int(input("Enter your age = "))

# if( age > 0 and age < 65 ):
#     if(age>18):
#         print("you can drive")
#     else:
#         print("you can't drive")
# else:
#     print("invalid age")

# =========================================


# if condition:
#     code
#     if condition:
#         code
#         if condition:
#             code
#         else:
#             code
#     else:
#         code
# else:
#     code

# ==================================

# smoke nhi kr sakte
# can me nhi milega
# amount > 30 

# smoke = input("tu smoke kr raha hai kya = ")
# if (smoke=="no"):
#     can = input("petrol kisme chahiye = ")
#     if(can=="gadi"):
#         amount = int(input("kitne ka petrol chahiye = "))
#         if(amount>30):
#             print("apko petrol mil jayega")
#         else:
#             print("bhag bhikmange")
#     else:
#         print("ghari ja")
# else:
#     print("mere ko bhi de... pr petrol mat le")



# ===========================================
# gumne ja sakte --- ramtek

# paise > 300
# fds > 5
# permission == True

# paise = int(input("kitne paise hai = "))
# if(paise>300):
#     fds = int(input("sath me fds kitne hai = "))
#     if(fds>5):
#         permission = input("family ki permission hai kya = ")
#         if(permission=="yes"):
#             print("tumhi ramtek jau shakta")
#         else:
#             print("clg se bunk marke jayenge")
#     else:
#         print("bhai rahne dete...")
# else:
#     print("jugad laga le paise ko... ")


# ================================================
# get 3 values from user and print greatest number
# ================================================


a = int(input("Enter a value 1 = "))
b = int(input("Enter a value 2 = "))
c = int(input("Enter a value 3 = "))

if(a > b):
    if(a > c):
        print("A is greater")
    else:
        print("C is greater")
else:
    if(b>c):
        print("B is greater")
    else:
        print("C is greater")

