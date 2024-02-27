# OOPs

# class
# class className:
#     code


# class Abc:
#     pass


# ob = Abc()

# =========================

# class Student:
#     pass
#
# rohit = Student()
#
# rohit.name = "rohit"
# rohit.age = 19
# rohit.std = "1st year"
#
#
#
# print(rohit.name)



# ===========================
class Student:
    def getinfo(self,name, age, std):
        self.name = name
        self.age = age
        self.std = std

    def printData(self):
        print(self.name)
        print(self.age)
        print(self.std)

rohit = Student()
rohit.getinfo("rohit",19,"1st year")

kamlesh = Student()
kamlesh.getinfo("kamlesh",21, "3rd year")

rohit.printData()

