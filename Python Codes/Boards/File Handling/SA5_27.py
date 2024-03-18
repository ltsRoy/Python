"""
Consider the file "Poem.txt"
                                                    Autumn Song
 Like a joy on the heart of a sorrow,
 The sunset hangs on a cloud;
 A golden storm of glittering sheaves,
 Of fair and frail and fluttering leaves,
 The wild wind blow in a cloud.
 
 Define a function reverse() that prints the lines of the file in reverse order.
"""


def poemsarekindanice():
    
    with open("Poem.txt","r+") as fh:
        lines=fh.readlines()
        fh.seek(0)
        for line in lines:
            line=line.strip()[::-1]+"\n" # \n must
            fh.write(line) #writeline doest exist 
            

poemsarekindanice()
         
            
