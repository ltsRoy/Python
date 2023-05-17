#https://stackoverflow.com/questions/2241891/how-to-initialize-a-dict-with-keys-from-a-list-and-empty-value-in-python


def dicts():
    a = {'a':25,'b':72,'c':281,'d':18}

    b={key:value for key, value in sorted(a.items(), reverse=True)}
    print(b)
      
  

   
dicts()