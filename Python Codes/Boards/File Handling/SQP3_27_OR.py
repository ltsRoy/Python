"""
    Write a function in Python that counts the number of “Me” or “My” words present in a text file “STORY.TXT”. 
 If the “STORY.TXT” contents are as follows: 
 My first book 
 was Me and 
 My Family. It 
 gave me 
 chance to be 
 Known to the 
 world. 
 The output of the function should be: 
 Count of Me/My in file:

    """

def work():
    with open ("TESTFILE.txt","r") as fh:
        count=0
        for line in fh:
            words=line.strip().split()
            for word in words:
                if word.lower()=="hi":
                    count+=1
        print(count)
        

work()