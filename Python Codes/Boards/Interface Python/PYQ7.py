import pymysql 

mycon=pymysql.connect("localhost",'root','root','test')
cursor=mycon.cursor()
query='SELECT * FROM Traders WHERE City="Delhi" or City="Mumbai"'

# OR 'SELECT * FROM Traders WHERE City IN ("Delhi", "Mumbai")' 

try:
    cursor.execute(query)
    data=cursor.fetchall() #() present
    for i in data:
        print(i)
except pymysql.Error as e:
    mycon.rollback()
    print("Error",e)
finally:
    mycon.close()
    


#mycon.close() 
#will not be executed if error comes up before

    
    
