import pickle

    
def createfile():
    with open("Book.dat","wb+") as fh:
        bb="lol"
        bnn=3
        au="lolpop"
        pr=234
        pickle.dump([bb,bnn,au,pr],fh)
        fh.close()
def countrec(au):
    with open("Book.dat","rb") as fh:
        count=0
        
        try:
            while True:
                k=pickle.load(fh)
                if k[2]==au:
                    l=k[0]

        except EOFError:
            fh.close()
        return l
    
createfile()
pp=countrec("lolpop")
print(pp)