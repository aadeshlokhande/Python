# constructor

class Laptop:

    def __init__(self):
        print("hello")

    def getData(self,brand, price,model):
        self.brand = brand
        self.price = price
        self.model = model

    def printData(self):
        print(self.brand)
        print(self.price)
        print(self.model)

    def __del__(self):
        print("bye bye")


# MSIMorden15 = Laptop()
# MSIMorden15.getData("MSI", "60000", "Morden 15")
# MSIMorden15.printData()

macbookair = Laptop()
macbookair.getData("apple", 82000, "M1 air")
macbookair.printData()
print("lol")

# ===========================================
# destructor
