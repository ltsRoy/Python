

with open("sam.txt") as fh:
    contents=fh.read()
freqy=[]
wlst=contents.split()
existing=[]
county=0
high=0
hw=""
for word in wlst:
    county=wlst.count(word)
    if  word not in existing:
        freqy.append([county,word])
        existing.append(word)
    if county>high:
           high=county
           hw=word
print(county,hw,freqy)
