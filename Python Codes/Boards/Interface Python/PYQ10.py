import mysql.connector as msql



def prog():
    mycon=msql.connect(host="localhost",user="root",passwd="root",database="test") 
    
    cursor=mycon.cursor()
    query="SELECT * FROM MobileMaster WHERE M_Price>8000"
    cursor.execute(query)
    data=cursor.fetchall()
    query2="UPDATE MobileMaster SET M_Price=M_Price+2000 WHERE M_Company='Samsung'"
    cursor.execute(query2)
    #data=cursor.fetchall()
    for i in data:
        print(i)
    mycon.commit()
    mycon.close()
    
prog()


"""
In the first example (Fetching Before UPDATE and 
Commit), the data variable contains the records 
fetched before the UPDATE query and will not reflect the 
updated M_price values. The updated_data variable fetches
the data again after committing the transaction, and it 
ill reflect the updated M_price values.

In the second example (Fetching After UPDATE and 
Commit), the updated_data variable fetches the data after 
committing the UPDATE query, and it will directly 
reflect the updated M_price values.
"""
