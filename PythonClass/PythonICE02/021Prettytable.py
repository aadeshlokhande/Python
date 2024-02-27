# prettytable

# +---------+-----------+------------+-------+
# |   name  |   lname   | Mobile no  | Grade |
# +---------+-----------+------------+-------+
# |  Tushar |  Tirmare  | 987984923  |  A++  |
# | Pragati | Choudhari | 9879843423 |   a+  |
# |  Megha  |   Tagade  | 9883443423 |   A   |
# +---------+-----------+------------+-------+


# pip install prettytable -----> console
from prettytable import PrettyTable

table = PrettyTable(['name', 'lname','Mobile no', 'Grade'])
a = 10 
a.add_raw
table.add_row(['Tushar','Tirmare', '987984923',"A++"])
table.add_row(['Pragati','Choudhari', '9879843423',"a+"])
table.add_row(['Megha','Tagade', '9883443423',"A"])
# print(table) 
table = str(table).split('\n')
line = table[0]

str = ""
for i in range(len(table)-1):
    if(i>2):
        str = str + table[i] + "\n"
        str = str+line + "\n"
    else:
        str = str + table[i] + "\n"

print(str)