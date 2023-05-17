
def lstcalc(): 
 lst=[8,62,72,7271] 
 for i in range (len(lst)-1,1,-1):
   if (i==len(lst)-1):
     lst[i]=lst[0]
   else: 
     lst[i]=lst[i-1]
   
 print (lst)

lstcalc()




