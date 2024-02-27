# String methods
# a = "Hello Guys... how are you"
# print(a)
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
# print(a.find("Guys"))
# print(a.count("e"))
# print(a.replace("Guys","Mahesh"))
# print(a.join("A"))

# a = ["hello",  ,"zal", "ka","j1"]
# print(" ".join(a))
# print(a.swapcase())

# print(a.split("e"))
# print("   hello hello ".strip())


# ==============================================

# String format

name = input("Enter your name = ")
age = int(input("Enter your age = "))
# sen = "My name is",name,"and my age is", age, "Year old"
# sen  = "My name is {} and my age is {} year old".format(name, age)
sen = f"my name is {name} and my age is {age} year old"

print(sen)
