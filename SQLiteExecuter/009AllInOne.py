# Create Table
import sqlite3
conn = sqlite3.connect("lol.db")

command = "create table todo (id int, task text, date , status text)"
conn.execute(command)

# Inserting data 
command = "insert into todo (id, task, date, status) values(3,'buy a gift', '22-01-2023', 'not done')"
conn.execute(command)
conn.commit()
command = "select * from todo"
result = conn.execute(command)
r = result.fetchall()
for row in r:
    print(row)

# Update data 
command = "update todo set status = 'Done' where id = 3"
conn.execute(command)
conn.commit()
result = conn.execute("select * from todo")
for row in result:
    print(row)

# Delete Data
command = "delete from todo where id = 1"
conn.execute(command)
conn.commit()
result = conn.execute("select * from todo")
for row in result:
    print(row)