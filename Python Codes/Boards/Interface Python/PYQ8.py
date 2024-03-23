import mysql.connector as msql



def prog():
    mycon=msql.connect(host="localhost",user="root",passwd="root",database="test") 
    
    cursor=mycon.cursor()
    query="CREATE TABLE Faculty(F_ID int PRIMARY KEY,Fname varchar(30) NOT NULL,Lname varchar(30),Hire_date date,Salary float(30,2))"
    cursor.execute(query)
    mycon.commit()
    mycon.close()
    
prog()

