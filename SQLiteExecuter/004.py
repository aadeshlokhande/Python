# Fetch data 

import sqlite3

conn = sqlite3.connect("Aadesh.db")

command = "select * from todo"
result = conn.execute(command)

r = result.fetchall()
# print(r)

for row in r:
    print(row)