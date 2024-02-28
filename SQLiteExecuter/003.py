# Inserting data 

import sqlite3

conn = sqlite3.connect("Aadesh.db")

command = "insert into todo (id, task, date, status) values(1,'bunk', '14-02-2024', 'not done')"

conn.execute(command)
conn.commit()

print("Data Inserted")