a=123456
b=1000000
print("welcome to sasta atm gareeb bolo kaise madad kare")
print("to with draw cash press 1")
print("to check balance press 2")
print("to deposit pais press 3")
print("to change pin press 4")
c=int(input("press the button here="))
if(c==1):
    d=int(input("enter the amount to withdraw"))
    e=int(input("enter your pin"))
    if(e==a and d<b):
        print("transaction is done succesfully fir kabhi mata ana")
        print(f"balance{b-d}")
    elif(e!=a):
        print("wrong pin")
    else:
        print("aukat maeh rahe insufficient balance")
if(c==2):
    z=int(input("enter your pin"))
    if(z==a):
        print(f"available balance {b}")
        print("thankyou")
    else:
        print("invalid pin")
if(c==3):
    m=int(input("enter the amount to deposit"))
    n=int(input("enter your pin "))
    if(n==a):
        print(f"amount deposited succesfully your available balance is now{b+m}")
    else:
        print("invalid pin")
if(c==4):
    o=int(input("enter your current pin "))
    k=int(input("enter your new pin"))
    x=int(input("confirm your new pin"))
    if(o!=a):
        print("invalid current pin cant change password")
    elif(k==x):
        print(f"password change to{k} from {a} successfully")
    else:
        print("new pin and confirmed pin does not match process terminated")