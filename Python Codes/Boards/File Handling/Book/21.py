import csv


def work():
    with open("data4.csv","r+") as fh:
        lst=[["hi","ball"],["poor","lol"],["okay","man"]]
        w=csv.writer(fh)
        w.writerows(lst)
        
        fh.seek(0)
        r=csv.reader(fh)
        for i in r:
            print(i) 
    
        
        
work()


"""#Your code has a potential issue. When you open the file with 
# mode "r+", it allows both reading and writing, but the file pointer is positioned at the beginning of the file. Therefore, if you write to the file before reading from it, the file pointer will be at the end after writing, resulting in reading nothing.

To overcome this issue, you need to move the file pointer 
to the beginning before reading from the file. You can achieve 
this by either closing and reopening the file or by using fh.seek(0)
to move the file pointer to the beginning of the file."""