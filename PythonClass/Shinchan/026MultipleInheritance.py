# Multiple Inheritance

class Mom:
    def momQuality(self):
        print("Bargaining")

class Dad:
    def dadQuality(self):
        print("paisa kamana")

class Child(Mom, Dad):
    def childQuality(self):
        print("Chije ghumana")

chintu = Child()
chintu.childQuality()
chintu.dadQuality()
chintu.momQuality()