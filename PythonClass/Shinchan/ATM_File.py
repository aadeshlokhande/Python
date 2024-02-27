# ATM File Handling

def readPin():
    file = open("pin.txt","r")
    a = int(file.read())
    file.close()
    return a

def readBal():
    file = open("bal.txt","r")
    a = int(file.read())
    file.close()
    return  a

def writePin(a):
    file = open("pin.txt","w")
    file.write(f"{a}")
    file.close()

def writeBal(a):
    file = open("bal.txt","w")
    file.write(f"{a}")
    file.close()



