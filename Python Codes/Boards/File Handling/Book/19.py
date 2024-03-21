



def Show_words():
    with open("NOTES.txt","r") as fh:
        fx=fh.readlines()
        for i in fx:
            i=i.split()
            if len(i)==5:
                print(i)
                
    
    
Show_words()
