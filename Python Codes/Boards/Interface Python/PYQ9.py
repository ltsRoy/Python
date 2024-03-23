import mysql.connector as msql

def prog():
    try:
        mycon = msql.connect(host="localhost", user="root", passwd="root", database="test")
        
        cursor = mycon.cursor()
        query = """
        CREATE TABLE Student(
            RollNo INT PRIMARY KEY,
            FirstName VARCHAR(30) NOT NULL,
            LastName VARCHAR(30),
            Address VARCHAR(30),
            ContactNo INT(10),
            Marks FLOAT(5,2),
            Course CHAR(5),
            Rank ENUM('GOOD', 'BEST', 'BAD', 'WORST', 'AVERAGE')
            #OR USE:
            #RANK CHAR(10) CHECK (RANK IN('GOOD', 'BEST', 'BAD', 'WORST', 'AVERAGE'))
        )
        """
        
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        
    except msql.Error as e:
        print(f"Error: {e}")

prog()
