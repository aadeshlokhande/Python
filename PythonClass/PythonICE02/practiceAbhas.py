class Python:
    def getdata(self,branch, year,purpose):
        self.branch= branch
        self.year= year
        self.purpose= purpose

    def printData(self):
        print(self.branch)
        print(self.year)
        print( self.purpose)

Abhas = Python()
Aadesh = Python()
Megha = Python()

Abhas.getdata("IT", "final", "job")
Abhas.printData()