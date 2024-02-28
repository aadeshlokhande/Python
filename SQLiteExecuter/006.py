# Delete Data

import sqlite3
conn = sqlite3.connect("Aadesh.db")
command = "delete from todo where id = 3"
conn.execute(command)
conn.commit()
print("total Changes = ",conn.total_changes)

result = conn.execute("select * from todo")

for row in result:
    print(row)