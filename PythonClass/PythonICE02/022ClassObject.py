# Class and Object

# class
# object :- instance 

# class Student:
#     pass 

# tushar = Student()
# tushar.roll = 10001
# tushar.clg = "priyadarshini"
# tushar.std = "3rd year"
# tushar.age = 21

# print(tushar.roll)



# =================================
 
class Student:
    def getData(self,roll,clg,std,age):
        self.roll = roll 
        self.clg  = clg 
        self.std = std 
        self.age = age 
    
    def printData(self):
        print(self.roll)
        print(self.clg )
        print(self.std)
        print(self.age)

pragati = Student()
tushar = Student()
abhas = Student()
# kumar = Student()
# megha = Student()
# akshay = Student()

pragati.getData(10002, "mahatma gandhi","10th", 15)
tushar.getData(10003, "mahatma gandhi","10th", 15)
abhas.getData(10004, "mahatma gandhi","10th", 15)
# kumar.getData(10005, "mahatma gandhi","10th", 15)
# megha.getData(10006, "mahatma gandhi","10th", 15)
# akshay.getData(10007, "mahatma gandhi","10th", 15)

# akshay.printData()
# _________________________________
name = input("nav sang be = ")

dictionary = {
    "pragati" : pragati,
    "tushar" : tushar,
    "abhas" : abhas,
    # "kumar" : kumar,
    # "megha" : megha,
    # "akshay" : akshay
}

dictionary[name].printData()