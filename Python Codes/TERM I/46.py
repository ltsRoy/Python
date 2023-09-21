file=open("a.txt",'r')
line=file.readline()
while line:
    
    if line[0]=='K':
        print(line,end='')
    line=file.readline()

print(type(line))
file.close()

        
          