
def tuple1():
    a = (1,2,3)

    b=((key, pow(key,3)) for key in a)
   #is a generator obj.
    print (list(b)) 
      
  

   
tuple1()