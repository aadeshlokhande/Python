# Update data 

import sqlite3

conn = sqlite3.connect("Aadesh.db")

command = "update todo set status = 'Done' where id = 3"
conn.execute(command)
conn.commit()

print("total Changes = ",conn.total_changes)

result = conn.execute("select * from todo")

for row in result:
    print(row)