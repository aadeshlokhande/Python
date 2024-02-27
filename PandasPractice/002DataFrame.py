import pandas as pd 

"""list = [2,3,4,5,6]

df = pd.DataFrame(list)
print(df)
print(type(df))"""

# ============================================

"""dic = {'a':[1,2,3,4,5],'b':[10,20,30,40,50],'d':[11,12,13,14,15],1:['a','b','c','d','e']}
df = pd.DataFrame(dic,columns=['a',1],index=['p','q','r','s','t'])
print(df)
print(type(df))"""

# ===========================================
"""dic = {'a':[1,2,3,4,5],'b':[10,20,30,40,50],'d':[11,12,13,14,15],1:['a','b','c','d','e']}
df = pd.DataFrame(dic)
# print value using indexing
print(df['d'][1])
print(type(df))"""
# ===================================================

"""list = []
for i in range(1,11):
    l = []
    for j in range(1,11):
        l.append(i*j)
    list.append(l)
l = [x for x in range(1,11)]
df = pd.DataFrame(list,columns=l,index=l)
print(df)"""


########################################
"""dic = {'a':[1,2,3,4,5],'b':[10,20,30,40,50],'d':[11,12,13,14,15],1:['a','b','c','d','e']}
df = pd.DataFrame(dic, index=['a','b','c','d','e'])
print(df)
print(type(df))"""
########################################

"""sr = {'s': pd.Series([1,2,3,4,5]), 'r':pd.Series([10,20,30,40,50])}
df = pd.DataFrame(sr)
print(type(df))
print(df)"""
########################################

