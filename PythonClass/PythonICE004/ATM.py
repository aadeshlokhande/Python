def readPin():
    file = open("Pin.txt")
    a = file.read()
    file.close()
    return int(a)

def readBal():
    file = open("Bal.txt")
    a = file.read()
    file.close()
    return int(a)

def writePin(a):
    file = open("Pin.txt","w")
    file.write(str(a))
    file.close()

def writeBal(a):
    file = open("Bal.txt","w")
    file.write(str(a))
    file.close()

print("press 1 : withdraw")
print("press 2 : check balance")
print("press 3 : change pin")
print("press 4 : Deposit")
choice = int(input("enter your choice = "))

if(choice==1):
    upin = int(input("enter a pin = "))
    pin = readPin()
    if(pin==upin):
        amount = int(input("enter a amount = "))
        bal = readBal()
        if(amount < bal):
            print("transaction done")
            bal = bal - amount
            print("current balance = ",bal)
            writeBal(bal)
        else:
            print("low balance")
    else:
        print("wrong pin")
    