
with open("strs.txt","w") as fh:
    ans='y'
    while ans=='y':
        ad=input("Enter line: ")
        fh.write(ad+"\n")
        ans=input("y/n?")
    