from operator import itemgetter
def tuple2():

  a=[(1,52),('a', 72),("lol",1)]

  for i in range (len(a)):
    for j in range (len(a)-i-1):
      if a[j] [1]> a[j+1] [1]:
        temp=a[j]
        a[j]=a[j+1] 
        a[j+1]=temp 

  print(a)
   
tuple2()

def tuple2alt():

  d=[(1,52),('a', 72),("lol",1)]

  b=d.sort(key= lambda x:x[1])

  print (b) #prints none
  print (d)
  print (sorted(d, key=itemgetter(1)))

tuple2alt()