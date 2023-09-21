import csv
lst=[[1,2],[3,4],[5,6]]
with open("newfile3.csv",'w+',newline='') as fh:
    wo=csv.writer(fh)
    wo.writerows(lst)
    
    wo2=csv.reader(fh)
    for i in wo2:
        print(i)
        
        
        