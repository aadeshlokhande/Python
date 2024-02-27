# nested for loop 
# for j in range(1,6):
#     for i in range(1,6):
#         print(j,i,end="\t")
#     print()


# 1 1     1 2     1 3     1 4     1 5
# 2 1     2 2     2 3     2 4     2 5
# 3 1     3 2     3 3     3 4     3 5
# 4 1     4 2     4 3     4 4     4 5
# 5 1     5 2     5 3     5 4     5 5


# 1 0 0 0 0 
# 0 1 0 0 0 
# 0 0 1 0 0 
# 0 0 0 1 0 
# 0 0 0 0 1 


# for i in range(1,6):
#     for j in range(1,6):
#         if(i==j):
#             print(1,end="  ")
#         else:
#             print(0, end="  ")
#     print()



# ================================

# nested for loop - logic base


# ^^^^^^^^^^^^^^^^^^^ With Logic ^^^^^^^^^^^^^^^^^^^^^^^^^^

# 1)
# * 
# * *
# * * *
# * * * *
# * * * * *



# 2)
#         *
#       * *
#     * * *
#   * * * *
# * * * * *


# 3)
# * * * * *
#   * * * *
#     * * *
#       * *
#         *


# 4)                    
#     *
#    * * 
#   * * *
#  * * * * 
# * * * * * 

# 5)
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# 6)
# * * * * *
# * * * *
# * * *
# * *
# *

# 7)
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# 8)
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 

# 9)
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 

# 10)
# 5 
# 5 4 
# 5 4 3 
# 5 4 3 2 
# 5 4 3 2 1 


# 12)
# 5                 
# 4 5              
# 3 4 5             
# 2 3 4 5           
# 1 2 3 4 5        


# 13)
# 1 - 10 tables 




# 14)
# 1 - 100 counting
# 1 2 3 ......10 
# 11 12 13.....20
# 21 22 23......30
# .
# .
# .
# 91 92 93......100






# 8)
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 


# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()



# 12)
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

# 5 5 5 5....
# 4 4 4 4....
# 3 3 3 3....
# 4 4 4 4....
# 1 1 1 1....

# for i in range(5,0, -1):
#     for j in range(i,6):
#         print(j,end=" ")
#     print()


# 4)                    
#     *
#    * * 
#   * * *
#  * * * * 
# * * * * * 


# for i in range(1,6):
#     for j in range(i,6):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
#           * 
#         * *
#       * * *        
#     * * * *       
#   * * * * * 



# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()



# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()


# for i in range(5,0,-1):
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()



# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end="\t")
#     print()


# 1 - 100 counting
# 1 2 3 ......10 
# 11 12 13.....20
# 21 22 23......30
# .
# .
# .
# 91 92 93......100


# a = 0
# for i in range(1,11):
#     for j in range(1,11):
#         a += 1
#         print(a,end="\t")
#     print()



# list = []
# a = 0
# for i in range(1,11):
#     temp = []
#     for j in range(1,11):
#         a += 1
#         temp.append(a)
#     list.append(temp)

# for a in range(10):
#     for b in range(10):
#         print(list[b][a],end="\t")
#     print()
    



