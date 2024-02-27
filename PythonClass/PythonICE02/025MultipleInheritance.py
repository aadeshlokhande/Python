# Multiple Inheritance

# parent -> base 
# child -> derive

class Mom:
    def cooking(self):
        print("khana acha bnati hai")
    
class Dad:
    def kutna(self):
        print("Kuthayi acha krte hai")
    

class Child(Dad,Mom):
    def chutiya(self):
        print("chutiya hai")


    
# govinda = Dad()
# govinda.kutna()

# kasturibai = Mom()
# kasturibai.cooking()


pragati = Child()
print(dir(pragati))
