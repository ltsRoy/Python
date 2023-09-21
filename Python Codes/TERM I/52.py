import csv
fh=open("sp.csv","w",newline='')
wo=csv.writer(fh,delimiter="\t")


ans='y'
try:
    while ans=='y':
        sport=input("Sport")
        comp=int(input("Comp"))
        pr=int(input("prizes"))
    
        wo.writerow([sport,comp,pr])
        ans=input("continue?")
except EOFError:
    fh.close()
    

    