import pymysql 

mycon=pymysql.connect("localhost",'root','root','test')
cursor=mycon.cursor()
query='UPDATE Student SET GRADE="A" WHERE Points>10'

"""
Wrong! same quotes cant be used!

query='UPDATE Student SET GRADE='A' WHERE Points>10'

"""
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

    
    
