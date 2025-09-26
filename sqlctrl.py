import sqlite3

conn = sqlite3.connect('DevOps.db')
cusor = conn.cusor()
cusor.excute('Select * from product_info;')
records = cusor.fetchall()
print(records)
