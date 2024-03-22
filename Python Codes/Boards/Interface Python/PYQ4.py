import pymysql 

mycon=pymysql.connect("localhost",'root','root','Mobile')
cursor=mycon.cursor()
query='SELECT M_Id,M_Name,M_Supplier FROM MobileStock'


try:
    cursor.execute(query)
    #mycon.commit() not needed here
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

    
    
