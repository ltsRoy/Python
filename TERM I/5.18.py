import pickle

with open("book.dat","rb+") as fh:
    p1=fh.tell()
    try:
        while True:
            p1=fh.tell()
            k=pickle.load(fh)
            if k[0]=="lol":
                k[1]="asian homie"
                fh.seek(p1)
                pickle.dump(k,fh)
    except EOFError:
        fh.close()
        

        