#mysql and cursor and python = not python keywords


import mysql.connector as msql
def mysql():
    mycon=msql.connect(host="localhost",user="root",passwd="root",database="menagerie")
    if mycon.is_connected():
        print("Connected!")
    cursor=mycon.cursor()
    query=input("Enter your query: ")
    cursor.execute(query)
    for i in cursor.fetchall():
        print(i)
    print("No.of rows: ",cursor.rowcount)
    cursor.close()>
    mycon.commit()
    mycon.close()  
mysql()

