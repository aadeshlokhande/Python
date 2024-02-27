# set ----> {values}

a = [12,23,12,43,76,12,24,65,12]
# b = set(a)
#
# a = list(b)
# print(a)

a = list(set(a))
a.sort()
print(a)