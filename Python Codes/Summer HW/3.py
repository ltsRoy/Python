
def lstcalc(): 
 lst=[8,62,72,7271] 
 for i in range (len(lst)-1,0,-1):
   #if (i==len(lst)-1):
     #lst[i]=lst[0]
   #else: 
     lst[i]=lst[i-1]
   
 print (lst)

lstcalc()

def lol():
    lst = [8, 62, 72, 7271]
    lst[1:] = lst[:-1]  # Update elements from index 1 onwards with values from previous indices 
    print(lst)
    lst[0] = lst[-1]  # Update the first element with the last element of the list
    print(lst)

lol()

def bol():
  lst = [8, 62, 72, 7271]
  for i in range(len(lst)-1, 0, -1):
        lst[i] = lst[i-1]
  lst[0] = lst[-1]
  print(lst)

bol()


