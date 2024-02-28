# Create Table

import sqlite3

conn = sqlite3.connect("Aadesh.db")
command = "create table todo (id int, task text, date , status text)"
conn.execute(command)
print("create table")