# for i in range (1,5001):
#     a = print("if(num==",i,"):")
#     if(i%2==1):
#         c = "odd"
#     else:
#         c = "even"
#     b = print("  print(\"num is",c,"\")")


# num = int(input("enter a number = "))
# if(num==0):
#     print("Even number")
# elif(num==1):
#     print("Odd number")
# elif(num==2):
#     print("even number")
# ..
# .
# .
# .
# elif(num==500):
#     print("Even Number")
# else:
#     print("OUT of range")






file = open("EvenOdd500.py", "w")
a = """num = int(input("enter a number = "))\nif(num==0):\n\tprint("Even number")\n"""
file.write(a)
num = 1
for i in range(1,501):
    file.write(f"elif(num=={num}):\n")
    file.write("\tprint(\"Odd number\")\n")
    num += 1
    file.write(f"elif(num=={num}):\n")
    file.write("\tprint(\"even number\")\n")
    num += 1
file.write("else:\n\tprint(\"OUT of range\")")
file.close()