# MultiLevel inheritance

class GrandParent:
    def advice(self):
        print("gyan pelna")
    
class Parent(GrandParent):
    def procreate(self):
        print("hum do aur hone do")

class Child(Parent):
    def deaf(self):
        print("kan ka bahra")

satyanand = GrandParent()
satyanand.advice()

akhandanand = Parent()
akhandanand.procreate()
akhandanand.advice()

munna = Child()
munna.advice()
munna.procreate()
munna.deaf()

