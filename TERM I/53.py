import csv

fh=open("oolala.csv",'w',newline='\n') #or ''
lst=[]
wo=csv.writer(fh)
ans='y'

while ans=='y':
    print("enter a b c:")
    x=int(input())
    y=input()
    z=int(input())
    #print(list(str(x)+","+str(y)+","+str(z)))
    lst.append([x,y,z]) 
    #lst.append(str)returns none
    ans=input("enter ans")
    
print(lst)

wo.writerows(lst)

fh.close()