
import mysql.connector as msql

mycon=msql.connect(host="localhost",user="root",passwd="root",database="items")

cursor=mycon.cursor()

s="DELETE FROM category WHERE name='%s' " #quote or not?
data=("Stockable",)
cursor.execute(s,data) 
mycon.commit()
print("rows affected: ",cursor.rowcount)
mycon.close()
