"""
1 

In SQL queries, string literals are typically enclosed in single quotes
('). Double quotes (") are used for identifiers like column names, table 
names, etc., but they are optional in most database systems unless the 
identifier contains special characters or is a reserved keyword.
In your specific query, you should use single quotes around the string value 'Kennel':


"""


import pymysql as msql 

mycon=msql.connect("localhost","root",'root',"menagerie")

cursor=mycon.cursor()

#s="SELECT * FROM Event WHERE type='Kennel'" #!!!! - 1 THIS WORKS

s="SELECT * FROM Event {0} type={1}".format('WHERE','Kennel') #Works?

#if cursor.is_connected(): doesnt work here
    #exit() 
    
cursor.execute(s)
data=cursor.fetchall()
for i in data:
    print(i)
    
cursor.close()
mycon.commit()
mycon.close()

"""In the context of your provided code, closing the 
cursor using cursor.close() is a good practice to release 
the resources associated with the cursor. However, it is not 
strictly necessary since you are closing the connection immediately afterward 
with mycon.close().
"""