

with open("story.txt", "r") as fh:
            #print(fh.readlines())
            x=fh.readlines()
            for line in x:
                k=line.split()
                for word in k:
                    if len(word)<=4:
                        print (word)
                    