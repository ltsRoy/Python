""" Write a function for given a list pairs=[[2,5],[4,2],[9,8],[12,10]], count the number of pairs [a,b] such that both a,b are even. """

def lstcalc(): 
 lst=[[2,5],[4,2],[9,8],[12,10]]
 str=len(lst)

 ch=0
 for i in range (0,str):
  b=lst[i]
  for j in range (2):
    d=b[j]
    if d%2!=0:
     break 
  else:
    ch=ch+1

 print (ch)

lstcalc()




