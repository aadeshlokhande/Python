# Inheritance

# single 

# class Dad:
#     def dadInfo(self):
#         print("I am a dad class ")

# class Child(Dad):
#     def childInfo(self):
#         print("I am a child class")

# jethalal = Dad()
# jethalal.dadInfo()


# tappu = Child()
# tappu.childInfo()

# tappu.dadInfo()
# ==============================

# multiple 


class Dad:
    def DadQuality(self):
        print("Khadus")

class Mom:
    def MomQuality(self):
        print("acha khana banati hai")

class Child(Dad,Mom):
    def ChildQuality(self):
        print("shaitan")
    
# jethalal = Dad()
# jethalal.DadQuality()

# daya = Mom()
# daya.MomQuality()

tappu = Child()
tappu.ChildQuality()
tappu.MomQuality()
tappu.DadQuality()



