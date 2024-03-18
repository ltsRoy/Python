"""Write a function in Python to count the number of blank spaces in a text file named “STORY.txt”.
    """
    
def Count():
    with open ('TESTFILE.txt',"r") as fh:
        text=fh.read()
        count=0
        for i in text:
            if i==" ":
                count+=1
                
        print(count)
        
Count()