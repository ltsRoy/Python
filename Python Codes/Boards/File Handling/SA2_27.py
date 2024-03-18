""" 
Define a function reverse ( ) that overwrites the contents of the file "myfile.txt" with its reverse contexts. That is 
the file will now contain the lines of the original file in reverse order
"""

def reverse():
    with open ("TESTFILE.txt","r+") as fh:
        lines=fh.readlines()
        lines.reverse()
        fh.seek(0) #miss this and your data will be appended not overwritten
        fh.writelines(lines)
        
reverse()
    