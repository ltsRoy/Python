"""Write a function in Python to count the number of lowercase and uppercase characters in a text file “Book.txt”.
    """
    
def Book():
    with open("TESTFILE.txt","r") as fh:
        
        text=fh.read()
        countU=0
        countL=0
        for i in text:
            if i.isupper():
                countU+=1
            if i.islower():
                countL+=1
    print(countU,' ',countL)
    
Book()