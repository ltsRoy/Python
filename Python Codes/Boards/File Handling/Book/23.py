import csv

def work():
    with open ("data.csv","r") as fh:
        fh2 = open ("data2.csv","w") # if this executed fh, w : it changes to w from r
        stureader=csv.reader(fh)
        w=csv.writer(fh2)
        for i in stureader:
            if i[0]=="check":
                continue
            w.writerow(i)
            
work()

