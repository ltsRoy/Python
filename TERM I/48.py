import pickle
fh=open("S.dat",'rb')
count=0
try:
    while True:
        xp=pickle.load(fh)
        if xp[2]>=75:
            print(xp)
            count+=1
except EOFError:
    fh.close()
    
    