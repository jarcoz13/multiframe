import sqlite3

conn = sqlite3.connect('productos2.db')
print("Opened database successfully")

conn.execute('CREATE TABLE producto (nombre TEXT, cantidad INTEGER, valor INTEGER)')
print("Table created successfully")
conn.close()
