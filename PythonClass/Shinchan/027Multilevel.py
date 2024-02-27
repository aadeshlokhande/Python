# multi level

class GrandParent:
    def grandParentQuality(self):
        print("Story telling")

class Parent(GrandParent):
    def parentQuality(self):
        print("discipline")

class Child(Parent):
    def childQuality(self):
        print("Masti")

tittu = Child()
tittu.grandParentQuality()
tittu.parentQuality()
tittu.childQuality()

