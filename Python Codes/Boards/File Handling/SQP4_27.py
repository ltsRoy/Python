"""Write a function to count the number of lines starting with a digit in a text file “Diary.txt”.
"""


#EXECUTE THE TWO PRINT STATEMENTS ONE AT A TIME AND SEE FUN

def Count():
    with open("TESTFILE.txt","r") as fh:
        #print(sum(1 for line in fh))
        text=fh.readlines()
        count=0
        #print(sum(1 for line in fh))
        for line in text:
            if line[0] in "0123456789":
                count+=1
            #if line[0].isdigit(): #SAME OUTPUT!
               # count+=1
    print(count)
    
Count()