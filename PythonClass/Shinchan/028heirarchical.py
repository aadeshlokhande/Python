# Heirarchical inheritance

class Parent:
    def Parent(self):
        print("singing")

class Son(Parent):
    def sonQuality(self):
        print("guitar")

class Daughter(Parent):
    def daughterQuality(self):
        print("Dancing")

golu = Son()
golu.Parent()
golu.sonQuality()

bitti = Daughter()
bitti.Parent()
bitti.daughterQuality()