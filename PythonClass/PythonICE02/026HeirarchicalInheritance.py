# heirarchical inheritance

# class Parent:
#     def fair(self):
#         print("Fair")
    
# class child1(Parent):
#     def skinny(self):
#         print("Skinny")
    
# class child2(Parent):
#     def lamba(self):
#         print("lamba")

# kumar = Parent()
# kumar.fair()

# karan = child1()
# karan.fair()
# karan.skinny()

# arjun = child2()
# arjun.fair()
# arjun.lamba()
# arjun.skinny()




# ================================================

class Getvalue:
    def getvalue(self,num1, num2):
        self.num1 = num1
        self.num2 = num2 
    
class Add(Getvalue):
    def add(self):
        print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")
    
class Sub(Getvalue):
    def sub(self):
        print(f"{self.num1} - {self.num2} = {self.num1 - self.num2}")

    
obj1 = Add()
obj1.getvalue(12,9)
obj1.add()

obj2 = Sub()
obj2.getvalue(30,20)
obj2.sub()