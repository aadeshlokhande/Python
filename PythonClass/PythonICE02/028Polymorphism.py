# Poly-morphism
# a = "Hello"
# a = [12,23,43]
# print(type(a))
# print(len(a))



# function overloading
def add(type, val1, val2):
    if(type=="str"):
        print(f"{val1} {val2}")
    elif(type=="int"):
        print(f"{val1} + {val2} = {val1+val2}")
    
# add("str","pragati","choudhari")
add("int", 12,90)



# function overriding

# class Dad:
#     def info(self):
#         print("I am a Dad class")
    
# class Child(Dad):
#     def infoo(self):
#         print("I am a Child class")
    
# babu = Child()
# babu.info()
# babu.infoo()





# class Student:
#     def __init__(self,name, age):
#         self.name = name 
#         self.age = age

#     def printInfo(self):
#         print(f"My name is {self.name} and my age is {self.age}.")
    
# tushar = Student("Tushar","21")
# akshay = Student("akshay","31")
# kumar = Student("kumar","201")
# abhas = Student("Abhas","12")

# list = [tushar,akshay,kumar,abhas]

# for i in range(len(list)):
#     print(f"{i+1})",end=" ")
#     list[i].printInfo()
