# Multilevel inheritance

class GrandParent:
    def GrandParentQuality(self):
        print("Story telling")

class Parent(GrandParent):
    def ParentQuality(self):
        print("pyar krna")

class Child(Parent):
    def ChildQuality(self):
        print("Study krna")
print("*******Grand parent*******")
manmohan = GrandParent()
manmohan.GrandParentQuality()

print("*******Parent Quality*****")
rahul = Parent()
rahul.ParentQuality()
rahul.GrandParentQuality()

print("*********Child Quality********")
pratik = Child()
pratik.ChildQuality()
pratik.ParentQuality()
pratik.GrandParentQuality()