



fh=open('sw.txt','r')
sdd=fh.read()
for l in sdd:
    if l.isdigit():
        print(l,end='')
