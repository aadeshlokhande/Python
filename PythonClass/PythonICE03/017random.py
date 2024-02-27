# Random 

# import random
# a = random.random()
# a = random.randint(1,6)
# list = ["kunal","mahesh", "palak", "gunjan"]
# a = random.choice(list)
# print(list)
# random.shuffle(list)
# print(a)
# clr = ["chidi","badam", "astab","vit"]
# num = ['a',2,3,4,5,6,7,8,9,10,'j','q','k']
# print(random.choice(clr),random.choice(num))
# coin = ["head","tail"]
# coin1 = ["head","tail"]
# print(random.choice(coin))
# print(random.choice(coin1))
# max = len(coin1)**len(coin)
# print(1/max)
# ====================================

# guess the number
# a = 7

# guess the number = 5
# your number is lesser
# guess the number = 8
# your number is greater
# guess the number = 6
# your number is lesser

# you loss 

# you win 
# ========================================
import random
a = random.randint(1,10)
ch = 1
for chance in range(4):
    if(chance<3):
        num = int(input(f"guess the number (chance {ch}/3) = "))
        if(num>a):
            print("your number is greater")
        elif(num<a):
            print("your number is lesser")
        else:
            print(f"you win in {ch} chance")
            break
        ch += 1
    else:
        print(f"you loss : value is {a}")