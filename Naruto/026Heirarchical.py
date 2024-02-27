# Heirarchical

class Parent:
    def parentQuality(self):
        print("Singing")

class child1(Parent):
    def Child1Quality(self):
        print("guitar")

class child2(Parent):
    def Child2Quality(self):
        print("Dancing")


print("****************")
shrikant = Parent()
shrikant.parentQuality()
print("****************")

om = child1()
om.Child1Quality()
om.parentQuality()
print("****************")

kumar = child2()
kumar.parentQuality()
kumar.Child2Quality()
