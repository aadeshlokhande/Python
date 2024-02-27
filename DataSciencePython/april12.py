# class Student:
#     pass

# abc = Student()
# abc.name = "abc"
# abc.age = 12
# abc.std = "7th"

# xyz = Student()
# xyz.name = "xyz"
# xyz.age = 13
# xyz.std = "8th"
# xyz.handicap = True  # Extra attribute

class Employee_2:
    school = 'KV-New Delhi'
    country = 'India'
    pincode = 110022
    default_bonus = 0.15

    def __init__(self,a_name, a_salary, a_role, a_dept, a_id):
        self.name = a_name
        self.salary = a_salary
        self.role = a_role
        self.dept = a_dept
        self.id = a_id

    def printData(self):
        print("school =",self.school)
        print("country =",self.country)
        print("pincode =",self.pincode)
        print("default_bonus =",self.default_bonus)
        print("name =",self.name)
        print("salary =",self.salary)
        print("role =",self.role)
        print("dept =",self.dept)
        print("id =",self.id)
        
aadesh = Employee_2("aadesh",74000, "Python developer",12000,1001)
aadesh.printData()    

    