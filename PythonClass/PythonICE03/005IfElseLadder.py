# If else Ladder

# if(condition):
#     statements
# elif(condition):
#     statements  
# elif(condition):
#     statements  
# elif(condition):
#     statements  
# elif(condition):
#     statements  
# else :
#     statements


# num = int(input("Enter a number = "))

# if(num==1):
#     print("ONE")
# elif(num==2):
#     print("TWO")
# elif(num==2):
#     print("THREE")
# elif(num==4):
#     print("FOUR")
# else:
#     print("invalid number")


################ HOMEWORK ################
# Get percentage from user and print grade 
# 0 - 35 = fails 
# 35 - 50 = D 
# 50 - 60 = c 
# 60 - 70 = b 
# 70 - 80 = A 
# 80 - 90 = A+
# 90 - 100 = A++

# get value from user and print month name

# get value from user and print week days up to 7

# get value from user and print week days 

num = int(input("enter a number = "))
a = num%7
if(a==1):
    print("Monday")
elif(a==2):
    print("Tuesday")
elif(a==3):
    print("wednesday")
elif(a==4):
    print("thursday")
elif(a==5):
    print("friday")
elif(a==6):
    print("saturday")
else:
    print("sunday")