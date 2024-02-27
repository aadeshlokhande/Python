# Series is a single dimensional array

import pandas as pd  
"""
x = [12,13,14,15]
# var = pd.Series(x)
# var = pd.Series(x, index=['a','b','c','d'])
# var = pd.Series(x, index=['a','b','c','d'],dtype="float")
var = pd.Series(x, index=['a','b','c','d'],dtype="float",name="Aadesh")
print(var)
print(type(var))

# print(var[2])   # print data using indexing
print(var['a'])   # print data using indexing"""


# ===========================================
"""dic = {
    "name":["Aadesh","Shubham", "Manish"],
    "age":[25,28,30], 
    "rank":[10,20,30]
    }

var1 = pd.Series(dic)
print(var1)"""

# ======================================================

"""ser = pd.Series(12, index = [1,2,3,4,5,6,7,8,9,10])
print(ser)
print(type(ser))"""
# =====================================================

"""ser1 = pd.Series(12, index = [1,2,3,4,5,6,7,8,9,10])
ser2 = pd.Series(12, index = [1,2,3,4,5,6])
var = ser1 + ser2
# if data is not available its shows NaN(Not a Number)
print(var)"""

# ====================================================

