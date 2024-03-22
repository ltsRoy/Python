import pymysql 

mycon=pymysql.connect("localhost",'root','root','inventory')
cursor=mycon.cursor()
query="CREATE TABLE Product (PID varchar(30), PName char(30), Price float, Rank varchar(2))"
#no need () after float
try:
    cursor.execute(query)
    mycon.commit()
except pymysql.Error as e:
    mycon.rollback()
    print("Error",e)
finally:
    mycon.close()

#mycon.close() 
#will not be executed if error comes up before

    
    
