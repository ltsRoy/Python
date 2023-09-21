with open("lower.txt","w")as fh:
    with open("upper.txt","w")as fh2:
        ans='y'
        while ans=='y':
            a=(input())
            if a.isupper():
                fh2.write(a+"\n")
            else:
                fh.write(a+"\n")
            ans=input("y/n?")
            