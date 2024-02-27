# Add Two Numbers in Python
# a = int(input("Enter a number = "))
# b = int(input("Enter a number = "))
# ans = a + b 
# print(ans)

# Subtract 2 Number in Python
# a = int(input("Enter a number = "))
# b = int(input("Enter a number = "))
# ans = a - b 
# print(ans)

# Product of 2 Number in Python
# a = int(input("Enter a number = "))
# b = int(input("Enter a number = "))
# ans = a * b 
# print(ans)

# Divide Two Numbers in Python
# a = int(input("Enter a number = "))
# b = int(input("Enter a number = "))
# ans = a / b 
# print(ans)

# Average of 2 Numbers in Python
# a = int(input("Enter a number = "))
# b = int(input("Enter a number = "))
# avrg = (a+b)/2
# print(avrg)

# Print the Square of a Number
# num=int(input("Ek number de de re baba = "))
# square = num * num 
# print(square)

# Python Program to Swap Two Numbers
# a = 10 
# b = 20
# print("a =",a, "b =",b)

# tuple
# a,b = b,a

# 3rd variable
# temp = a 
# a = b 
# b = temp

# arithmatic 
# a = a + b 
# b = a - b 
# a = a - b 

# print("a =",a, "b =",b)

# Simple Interest in Python
# s = int(input("Enter principal = "))
# r = int(input("Enter Intrest rate = "))
# t = int(input("Enter time in year = "))
# simpleInterest = s*r*t 
# print(simpleInterest)

# Compound Interest in Python
# p = int(input("Enter principal = "))
# r = int(input("Enter Intrest rate = "))
# n = int(input("Enter number of times per year = "))
# t = int(input("Enter no. of year = "))
# ci = p * ((1 + (r/n))**(n*t))
# print(ci)

# principal = 1000
# rate = 10
# time = 5
# number = 6
# rate = rate/100
# # amount = principal * pow( 1+(rate/number), number*time)
# amount = principal * ( (1+(rate/number))**(number*time))
# ci = amount - principal
# print('Compound interest = %.2f' %ci)
# print('Total amount = %.2f' %amount)


# Python Program to Find Square root
# import math 
# num = int(input("bhagwan ke name pe dedere baba = "))
# # ans = math.sqrt(num)
# # print(ans)
# print(math.sqrt(num))

# Python Program to Find Area of Circle
# r = int(input("Enter rad = "))
# area = 3.14*r**2
# print(area)

# Python Program to Find Area of Triangle
# b = int(input("Enter a base = "))
# h = int(input("Enter a height = "))
# area = 0.5 * b * h
# print(area)

# Python Program to Find Area of Rectangle
# b = int(input("Enter a base = "))
# h = int(input("Enter a height = "))
# area = b * h
# print(area)

# Convert Kilometers to meter and Vice-versa
# meter = int(input("enter a meter = "))
# km = meter / 1000
# print(km)

# km = int(input("enter a km = "))
# m = km * 1000
# print(m)

# Convert Bytes to KB, MB, GB, & TB
# bytes = int(input("Bytes dedo yr = "))

# kb = bytes / 1024
# mb = kb / 1024
# gb = mb / 1024
# tb = gb / 1024

# print("kb = ",kb)
# print("mb = ",mb)
# print("gb = ",gb)
# print("tb = ",tb)

# Convert Bytes to KB in Python
# bytes = int(input("Bytes dedo yr = "))
# kb = bytes / 1024
# print(kb)

# Python Convert Bytes to MegaBytes
# bytes = int(input("Bytes dedo yr = "))
# kb = bytes / 1024
# mb = kb/1024
# print(mb)

# *********************************************
# get seconds from user and convert it into hour, minutes and sec

# input
# seconds = 4000

# output
# hour = 1 
# min = 6
# sec = 40

sec = int(input("Enter a sec = "))
hr = sec // 3600
rem = sec % 3600
min = rem // 60
sec = rem % 60
print("hr = ",hr)
print("min = ",min)
print("sec = ",sec)