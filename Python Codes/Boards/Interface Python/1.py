

import mysql.connector as msql

mycon=msql.connect(host="localhost",user="root",passwd="root",database="menagerie")

curse=mycon.cursor()

if mycon.is_connected():
    print("Connected!")
s2="SELECT * FROM '%s'" %("Pet",)
curse.execute(s2)
data=curse.fetchall()
for i in data:
    print(i)
    
curse.close()
mycon.commit()
mycon.close()
    
    
