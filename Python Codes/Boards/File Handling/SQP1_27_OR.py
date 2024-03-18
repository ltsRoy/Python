""" 
Write a function ETCount() in Python, which should read each character of a text file “TESTFILE.TXT” and then 
count and display the count of occurrence of alphabets E and T individually (including small cases e and t too).
 Example:
 If the file content is as follows:
 Today is a pleasant day.
 It might rain today.
 It is mentioned on weather sites
 The ETCount() function should display the output as:
 E or e: 6
 T or t : 9
 """
 
def ETCount():
    
    with open ("TESTFILE.txt","r") as fh:
        chars=fh.read()
        ce=0
        ct=0
        for i in chars:
            if i.lower() == 'e':
                ce+=1
            if i.lower() == 't':
                ct+=1
        print(ce," ",ct)
        
ETCount()


                
                