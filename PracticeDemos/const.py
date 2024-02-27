# # constructor

# # class abc:
# #     def __init__(self):
# #         print("Hello")
    
#     # def getData(self,a,b,c):
#     #     print(a+b+c)
    
# # pop = abc()
# # pop.hello()

# # pop.getData(10,20,30)
# # =========================================

# # class Student:
# #     def __init__(self,name,age,roll,std):
# #         self.name = name 
# #         self.age = age 
# #         self.roll = roll
# #         self.std = std 
    
# #     def printData(self):
# #         print(self.name)
# #         print(self.age)
# #         print(self.roll)
# #         print(self.std)

# # kunal = Student("kunal", 25, 101, "3rd")
# # mahesh = Student("mahesh", 25, 102, "3rd")
# # gunjan = Student("gunjan", 19, 103, "3rd")
# # palak = Student("palak", 20, 104, "3rd")


# # =====================================================
# # class abc:
# #     def __init__(self):
# #         print("hello")
    
# #     def __del__(self):
# #         print("Bye bye")


# # lol = abc()
# # print("hahahaha")


# # =============================================
# # class abc:
# #     def __init__(self,name):
# #         self.name = name
# #         print("hello",name)
    
# #     def __del__(self):
# #         print("Bye bye",self.name)


# # lol = abc("lol")
# # if(True):
# #     a = abc("a")
# #     if(True):
# #         b = abc("b")
# #         if(True):
# #             c = abc("c")
# #         d = abc("d")
# #     e = abc("e")

# # ===================================================================

# var = int(input("Enter a number = "))
# a = 1
# for i in range(1,11):
#     for j in range(1,11):
#         if(j==1):
#             print(i*var,end="   ")
#         elif(i==1):
#             a += 1
#             print(var*a,end="   ")
#         else:
#             print(end="   ")
#     print()


print(10,flush=True)
print(10,flush=False)