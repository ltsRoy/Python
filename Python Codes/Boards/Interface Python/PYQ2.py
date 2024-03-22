import mysql.connector as msql

mycon=msql.connect(host="localhost",user="root",passwd="root",database="test")
cursor=mycon.cursor()
query="INSERT INTO Persons (P_ID,LastName,FirstName) VALUES (%s,'%s','%s')"%(5,"Peterson","Kari")

try:
    cursor.execute(query)
    mycon.commit()
except: 
    mycon.rollback()
    

cursor.close()
mycon.close()


""" 
If you provide fewer values than the number of %s placeholders in a string formatting operation in languages like Python, C, Java, etc., you will likely encounter errors like:

IndexError: In Python, if you provide fewer values than the number of placeholders, an IndexError will be raised.
Format Error or Segmentation Fault: In C, providing fewer values than placeholders can lead to format errors or segmentation faults, as the program tries to access memory that it shouldn't.
MissingFormatArgumentException: In Java, providing fewer arguments than the number of placeholders will result in a MissingFormatArgumentException being thrown.
It's important to ensure that the number of values provided matches the number of placeholders in order to avoid such errors.


"""