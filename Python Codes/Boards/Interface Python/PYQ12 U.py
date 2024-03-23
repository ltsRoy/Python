import mysql.connector as msql
#IS DATE A STRING? WHY QUOTES THEN?
#SUPER IMPORTANT!!!! USE ' and " in combination when STRING INSIDE STRING => SEE LINE 9

def prog():
    mycon=msql.connect(host="localhost",user="root",passwd="root",database="test") 
    
    cursor=mycon.cursor()
    query="INSERT INTO College(No,Name,Age,Department,Dateofjoin,Basic,Sex) VALUES(%s,'%s',%s,'%s','%s',%s,'%s')"%(15,"Atin",27,"Physics","15/05/02",8500,"M")    # IMPORTANT #THIS IS NOT DATE DATA TYPE BECAUSE THAT HAS FORMAT YYYY-MM-DD
    cursor.execute(query)
    
    cursor.execute("DELETE FROM College WHERE name='Viren'")
    mycon.commit()
    mycon.close()
    
prog()

"""
From the MySQL documentation:

Database and Table names are not case 
sensitive in Windows, and case sensitive 
in most varieties of Unix. One notable 
is Mac OS X, which is Unix-based but uses a 
default file system type (HFS+) that is not case sensitive.
and
Column(Field) and index names are not case 
on any platform, nor are column aliases.
"""
