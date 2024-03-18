#TOPG! 

a=9
#i is line and j is line pos

topg=""
for i in range (a): 
  for j in range (a-2):
    if ( 
      
      ((i==0 or i==a-1) and (j>0) and j<a-2-1)
        or ((i<a/2) and i!=0 and (j==0 or j==a-2))
        or (i==(a//2) and j>=a-2-3) 
        or (i>a/2 and i!= a-1 and (j==0 or j==a-2-1))
      
       ): 
      topg=topg+'*'
    else: 
      topg=topg+' '
  topg=topg+"\n"

print(topg)
      
    
  