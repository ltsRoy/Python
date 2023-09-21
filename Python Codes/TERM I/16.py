import pickle

with open("companies.dat","rb") as fh:
    
    try:
        while True:
            k=pickle.load(fh)
            print(k)
            for ix in k:
                if ix.get("CompID")==1005:
                    print(ix)
    except EOFError:
        fh.close()
        