import csv


def work():
    with open("data.csv","r") as fh:
        r=csv.reader(fh,delimiter="\t")
        for i in r:
            print(i)
        
    
work()