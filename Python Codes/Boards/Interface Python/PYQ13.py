import mysql.connector as msql



def prog():
    mycon=msql.connect(host="localhost",user="root",passwd="root",database="test") 
    
    cursor=mycon.cursor()
    query="UPDATE Club SET Address='Noida' WHERE Memberid='M003'"
    cursor.execute(query)
    query2="DELETE FROM Club WHERE Name='Sachin'"
    cursor.execute(query2)
    mycon.commit()
    mycon.close()
    
prog()

