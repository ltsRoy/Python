"""Write a method COUNTLINES() in Python to read lines from text file ‘TESTFILE.TXT’ and display the lines 
which are not starting with any vowel.
 Example:
 If the file content is as follows:
Sample Question Papers 23
 An apple a day keeps the doctor away.
 We all pray for everyone’s safety.
 A marked difference will come in our country.
 The COUNTLINES() function should display the output as:
The number of lines not starting with any vowel - 1
    """
    

def COUNTLINES():
    with open ("TESTFILE.txt","r") as fh:
        lines=fh.readlines()
        #for line in lines:
            #print(line.rstrip())
        count=0
        vowels="aeiou"
        for line in lines:
            if line[0].lower() not in vowels:
                count+=1
        print(count)
                
COUNTLINES() 


"""If you read this file using open("testfile.txt", "r") 
    without specifying newline="\n", Python will recognize both \n and \r\n as newline characters on different platforms. However, if you explicitly specify newline="\n", Python will only recognize \n as the newline character, even if the file has \r\n line endings. This ensures consistent behavior across platforms.

In terms of output, if you print the lines read from the 
file, there won't be a visible difference in the output 
itself. However, specifying newline="\n" provides more 
control and predictability over how newline characters
are handled internally by Python.
    """