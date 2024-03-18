"""Consider the file "Poem.txt"

 Autumn Song
 Like a joy on the heart of a sorrow,
 The sunset hangs on a clouds:
 A golden storm of glittering sheaves,
 Of fair and frail and flattering leaves,
 The build wind blows in a cloud.
 
 Define a function reverse( ) that prints the lines of the file in reverse order
"""


with open("TESTFILE.txt","r+") as fh:
    lines=fh.readlines()
    lines.reverse()
    fh.seek(0)
    fh.writelines(lines)
    
    