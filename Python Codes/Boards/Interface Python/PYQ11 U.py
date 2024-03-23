import mysql.connector as msql



def prog():
    mycon=msql.connect(host="localhost",user="root",passwd="root",database="Test") 
    
    cursor=mycon.cursor()
    query=""" CREATE TABLE Watches(
        WatchID VARCHAR(5) PRIMARY KEY,
        WatchName VARCHAR(15) NOT NULL,
        Price INT(10),
        Type CHAR(10),
        Qty_store INT(5) NOT NULL) 
    """
    
    query2="INSERT INTO Watches(WatchID,WatchName,Price,Type,Qty_store) VALUES(%s,%s,%s,%s,%s)"
    query3="INSERT INTO Watches(WatchID,WatchName,Price,Type,Qty_store) VALUES(%s)"
    values=[("W001","High Time","10000","Un234isex","100"),
    ("W001","Life Time","15000","Unisex","150"),
    ("W001","Wave","20000","Uni43sex","250"),
    ("W001","High Fashion","7000","Unis234ex","1300"),
    ("W001","Golden Time","25000","Unise32x","1300")]
    queryfinal="%s"
    
    values2=[(query),(query3)]
    
    try:
        cursor.executemany(queryfinal,values2)
        cursor.executemany(query2,values)
        mycon.commit()    
    except msql.Error as e:
        mycon.rollback()
        print(e)
    finally:
        mycon.close()
    
prog()

"""Do you still need to put mycon.rollback() in the except block?
Yes, it is a good practice to include mycon.rollback() in the 
except block to ensure that any changes made in the try block are rolled back if an error occurs, preventing incomplete or erroneous data from being committed to the database.

User
if im sure no errors will occur in try then do i need 
it
ChatGPT
If you are confident that no errors will occur in the try 
block, then technically you don't need to include 
mycon.rollback() in the except block. However, it is still a good 
practice to include it as a safety measure to handle 
unexpected errors that might occur.
"""



"""
If you don't provide any arguments to 
cursor.execute() or cursor.executemany(),
you will get a TypeError from both indicating that 
the method requires at least one argument.
"""