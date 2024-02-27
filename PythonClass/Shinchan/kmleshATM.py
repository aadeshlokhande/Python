# ATM

account_pin = 1212
account_balance = 10000

pin=int(input("enter your pin="))

if(pin==1212):
    print("1-withdraw")
    print("2-deposit")
    print("3-check balance")
    print("4-change pin")

    choice = int(input("enter your choice="))

    if(choice==1):
        withdrawal_pin=int(input("enter your pin="))
        if(withdrawal_pin==account_pin):
            withdrawal_amount=int(input("enter amount="))
            if(withdrawal_amount<=account_balance):
                account_balance-=withdrawal_amount
                print("transaction Done")
                print("current balance:", account_balance)
            else:
                print("insufficient amount")
        else:
            print("wrong pin")
    elif(choice==2):
        deposit_pin = int(input("enter your pin="))
        if (deposit_pin == account_pin):
            deposit_amount = int(input("enter deposit amount="))
            account_balance+=deposit_amount
            print("deposit done")
            print("current balance:", account_balance)
        else:
            print("wrong pin")
    elif(choice==3):
        ac_pin = int(input("enter you pin="))
        if (ac_pin == account_pin):
            print("account_balance:", account_balance)
        else:
            print("wrong pin")
    elif(choice==4):
        acc_pin = int(input("enter your pin="))
        if (acc_pin== account_pin):
            new_pin = int(input("enter new pin="))
            confirm_pin = int(input("confirm pin="))
            print("pin changed:", confirm_pin)
        else:
            print("wrong pin")
else:
    print("worng pin")