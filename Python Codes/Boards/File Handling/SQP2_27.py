"""Write a method/function DISPLAYWORDS() in python to read lines from a text file STORY.TXT, and display 
those words, which are less than 4 characters. 
"""


def DISPLAYWORDS():
    fh=open("TESTFILE.txt","r")
    text=fh.read()
    words=text.split()
    for word in words:
        if len(word)<4:
            print(word," ",end=" ")
    fh.close()
            
            
DISPLAYWORDS()

""" 
        Split the text based on comma (',') character
        words = text.split(',')
        
        The default character for the split() method in 
        Python is whitespace, which includes spaces, tabs, and newline characters.
    
"""