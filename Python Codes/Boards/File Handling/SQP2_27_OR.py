"""Write a function CountHisHer() in Python which reads the contents of a text file “Story.txt” and counts the 
words His and Her (not case sensitive)"""



def CountHisHer():
    fh=open("TESTFILE.txt","r")
    text=fh.read()
    words=text.split() #dont use " " in split ans=2
    #print(words)
    count=0
    for word in words:
        if word=="hi":
            count+=1
    print(count)
    fh.close()
    
CountHisHer()
    
"""

def CountHisHer():
    count = 0
    with open('TESTFILE.txt', 'r') as file:
        print(file)
        for line in file:
            words = line.strip().split()  # Split the line into words
            for word in words:
                # Remove leading and trailing whitespaces, and convert to lowercase
                word = word.strip().lower()
                if word == 'hi':
                    count += 1

    if count == 0:
        print("not found in file")
    else:
        print("count =", count)

CountHisHer()

THEORY:

Yes, in Python, a file object is iterable, meaning you can iterate over its lines using a loop or with other constructs like list comprehensions. When you iterate over a file object, it yields each line of the file as a string.

For example:


with open("example.txt", "r") as file:
    for line in file:
        print(line)
        
        
        
The strip() method in Python removes leading and trailing whitespace characters by default. These whitespace characters include:

Space ( )
Tab (\t)
Newline (\n)
Carriage return (\r)
Form feed (\f)
Vertical tab (\v)


        """