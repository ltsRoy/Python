import pickle

emp={}
found=False
fh=open("OJ.dat","rb")
fh.seek(0)


try:
    while True:
        rpos=fh.tell()
        emp=pickle.load(fh)
        if emp['empno']==1251:
            emp['sa']=emp['sa']+2000
            fh.seek(rpos)
            pickle.dump[emp,fh]
            found=True
except EOFError:
    if found==False:
        print("sorry")
    else: 
        print("yeahhh")
    fh.close()