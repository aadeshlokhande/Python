print("Welcome to TimePass ATM")
print("Press 1 : Withdraw Cash \nPress 2 : Check Account Balance \nPress 3 : Change Pin \npress 4 : Deposite Cash")
a= int(input())
if a>=5:
    print("Invalid Entry")
elif a<=0:
    print("Invalid Entry")
elif a==1:
    userpin = int(input("Enter the 4 digit not so highly secured PIN\n"))
    pinfile = open("PIN.txt","r")
    actualpin = int(pinfile.read())
    pinfile.close()
    if userpin==actualpin:
        Balancefile = open("balance.txt", "r")
        balance = int(Balancefile.read())
        Balancefile.close()
        amount = int(input("Enter the amount you want to Withdraw\n"))
        newbalance = balance - amount
        Balancefile = open("balance.txt","w")
        var = str(newbalance)
        Balancefile.write(var)
        Balancefile.close()
        print("Cash withdrawn and balance updated successfully")
        print("Thank you for using our TimePass ATM")
    else:
        print("Incorrect PIN")

elif a==2:    
    # print("Code for Account balance check")
    userpin = int(input("Enter the 4 digit not so highly secured PIN\n"))
    pinfile = open("PIN.txt","r")
    actualpin = int(pinfile.read())
    pinfile.close()
    if userpin==actualpin:
        Balancefile = open("balance.txt", "r")
        balance = Balancefile.read()        
        print("Rs.",balance)
        print("Thank you for using our TimePass ATM")

    else:
        print("Incorrect PIN")

elif a==3:
    # print("Code for Pin change")
    userpin = int(input("Enter the 4 digit not so highly secured PIN\n"))
    pinfile = open("PIN.txt","r")
    actualpin = int(pinfile.read())
    pinfile.close()
    if userpin==actualpin:
        a = int(input("Enter New PIN\n")) 
        b = int(input("Confirm PIN\n"))
        if a==b:
            file = open("PIN.txt","w")
            var = str(a)
            file.write(var)
            file.close()
            print("PIN changed successfully\n")
            print("Thank you for using our TimePass ATM")

        else:
            print("PIN Confirmation failed\n")
    else:
        print("Incorrect PIN") 

elif a==4:
    # print("Code for cash Deposite")
    userpin = int(input("Enter the 4 digit not so highly secured PIN\n"))
    pinfile = open("PIN.txt","r")
    actualpin = int(pinfile.read())
    pinfile.close()
    if userpin==actualpin:
        Balancefile = open("balance.txt", "r")
        balance = int(Balancefile.read())
        Balancefile.close()
        amount = int(input("Enter the amount you want to Deposite\n"))
        newbalance = balance + amount
        Balancefile = open("balance.txt","w")
        var = str(newbalance)
        Balancefile.write(var)
        Balancefile.close()
        print("Cash deposited and balance updated successfully")
        print("Thank you for using our TimePass ATM")

    else:
        print("Incorrect PIN")