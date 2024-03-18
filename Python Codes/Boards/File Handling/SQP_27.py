"""Write a method COUNTLINES() in Python to read lines from text file ‘TESTFILE.TXT’ and display the lines 
which are not starting with any vowel.
 Example:
 If the file content is as follows:
Sample Question Papers 23
 An apple a day keeps the doctor away.
 We all pray for everyone’s safety.
 A marked difference will come in our country.
 The COUNTLINES() function should display the output as:
The number of lines not starting with any vowel - 1
    """
    

def COUNTLINES():
    with open ("TESTFILE.txt","r") as fh:
        lines=fh.readlines()
        print(lines)