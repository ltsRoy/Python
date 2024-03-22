import mysql.connector as msql



mycon=msql.connect(host="localhost",user="system",passwd="test",database="inventory")
cursor=mycon.cursor()
query="ALTER TABLE item ADD ManufacturingDate DATE NOT NULL "

cursor.execute(query) 
mycon.commit()
mycon.close()