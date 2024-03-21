import csv

def work():
    with open ("data.csv","r") as fh:
        fh2 = open("data3.csv","w")
        r=csv.reader(fh)
        w=csv.writer(fh2,delimiter='|')
        
        for i in r:
            w.writerow(i)
            

work()
        
         
        