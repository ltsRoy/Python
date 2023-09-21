import csv


with open("csvv.csv","r") as fh:
    wo=csv.reader(fh)
    with open('newfile2.csv','w',newline='') as fh2:
        wo2=csv.writer(fh2,delimiter="\t")
        
        for i in wo:
            wo2.writerow(i)
        