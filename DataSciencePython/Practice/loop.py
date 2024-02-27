# loop
# for 
# for - reserve words 

# for var in collectionOfData:
#     statements

# a = [1,20,3,40,5]

# for i in a:
#     print(i*10)

# for i in "Hello bhai kaise ho":
#     print(i)

# range(5) ----> 0,4
# range(2,9) ----> 2, 8 
# range(2,9,2) ----> 2,4,6,8

# for i in range(4):
#     print("Hello",i)

# for i in range(10):
#     print("I love you",i)

# for i in range(200):
#     print(f"Sorry",end="")

# for i in range(1,11):
#     if(i%2==0):
#         print(i)

# num = int(input("enter a number = "))
# for i in range(1,11):
#     print(f"{num} x {i} = {i*num}")


# write a code to print total sum from 1 to 100


# s_year = int(input())
# p_year = 2023
# sum_=0
# for i in range(s_year,p_year+1):
#     if i%4 == 0:
#         print(i ,': It is a leap year')
#     elif i%400 == 0:
#         print(i ,': It is a Leap Year')

# div 4 
# div 400 
# not div 100 

# count = 0
# sum = 0
# for num in range(2024):
#     if(num%4==0):
#         if(num%100==0):
#             if(num%400 in (100,200,300)):
#                 # print("not a leap year")
#                 pass
#             else:
#                 # print("leap year")
#                 count = count + 1
#                 sum = sum + num
#         else:
#             # print("leap year")
#             count = count + 1
#             sum = sum + num
#     # else:
#     #     print("not a leap year")
    

# print(count)
# print(sum)




# while 
# while(condition):
#     statements

# per = 'ha'
# while(per=="yes" or per=="ha"):
#     a = int(input("enter a number = "))
#     b = int(input("enter a number = "))
#     ans = a + b 
#     print(ans)
#     per = input("Aur calculation krni hai kya = ")

 


# a = 1 
# while (a<10):
#     print(a)
#     a = a + 1


# num = 9
# a = 1 
# while(a<=10):
#     print(num*a)
#     a += 1


# enter a number = 3
# enter a number = 5
# enter a number = 7
# .
# .
# enter a number = 0
# ans 15


# sum = 0
# var = 3
# while(var!=0):
#     var = int(input("enter a number = "))
#     sum += var 
# print(sum)

# a = [12,23,43,54,65,45,77,34,25,23,65]
# i = 0 
# while(a[i]!=77):
#     print(a[i])
#     i+=1


# break
# for i in range(1,11):
#     if(i==7):
#         break
#     print(i)

# print("Good night")


# pass
# def FaceRec():
#     pass 



# continue
# for i in range(1,11):
#     if(i==7):
#         continue
#     else:
#         print(i)

# print("Good night")


# ****************FORMAT********************
# aadesh = "my name is aadesh and my age is 79 year old"
# robin = "my name is robin and my age is 23 year old"

# name = input("Enter your name = ")
# age = int(input("Enter your age = "))

# a = "my name is {} and my age is {} year old".format(name,age)
# a = f"my name is {name} and my age is {age} year old"
# print(a)

# a = int(input("enter a number = "))
# b = int(input("enter a number = "))

# print(f"{a} + {b} = {a+b}")


# Function
# inbuild
# with argument with return
# with argument without return
# without argument with return
# without argument without return

# user define 
# with argument with return
# with argument without return
# without argument with return
# without argument without return