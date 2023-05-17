""" Write a function for given a list pairs=[[2,5],[4,2],[9,8],[12,10]], count the number of pairs [a,b] such that both a,b are even. """

lst=[[2,5],[4,2],[9,8],[12,10]]
str=len(lst)

ch=0
for i in lst:
  a,b=i 
  if a%2==0 and b%2==0:
   ch=ch+1

print(ch)