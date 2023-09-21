import csv

with open("csvv.csv","r") as fh:
    wo=csv.reader(fh)
    nf=open("newfile.csv","w",newline='')
    wo2=csv.writer(nf)
    for i in wo:
        if "check" in i:
            continue
        else:
            wo2.writerow(i)
    nf.close()
   
            
            
