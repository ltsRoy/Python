"""
###
#Author: Soumyajit Roy 
#Lang: Python 3
#Directory: GitHub 
#Code Status: Unfinished 
#Notes: Add more methods for diff functionality.
###

"""

tup=(62,52,82) #making a tuple 

lst=list(tup) #converting tuple to list 

key=(1,2,3) #making a tuple of keys to set up dictionary 

# dict1=dict(tup) -> wrong, lol, we need iterable objects 


""" We will try the following: """

'''
list to tuple ✓
list to dict ✓
list to set ✓
''' #checking out multiple doc string comment styles type 1

"""
tuple to list ✓
tuple to dict ✓
tuple to set ✓

dict to list ✓
dict to tuple ✓
dict to set ✓

set to list ✓
set to tuple ✓
set to dict ✓
"""  #checking out multiple doc string comment styles type 2

"""Lets get tup to dict """

#type 1: 
dict1={key[i]: tup[i] for i in range (len(key))} 
#print (dict1) #checking 

#type 2: 
dict1=dict(zip(key,tup)) 
# print(dict1) #checking 

'''Lets get list to dict'''

#type 1: 
dict1={key[i]: lst[i] for i in range (len(key))} 
#print (dict1) #checking 

#type 2: 
dict1=dict(zip(key,lst)) 
#print(dict1) #checking 

'''Lets get list to set'''

#type 1: 
set1=set(lst) 
#print (set1) #checking 

#type 2: 
set1 = {x for x in lst} 
#print(set1) #checking INTERESTING! ORDER CHANGES! (CAN CHANGE)

#In Python, lists are ordered collections, where the order of elements is maintained as they are added. However, sets use a different internal data structure, such as a hash table, which allows for efficient membership tests and removal of duplicates. This data structure does not preserve the original order of the elements.

#DISCARDED!!! :  BELOW METHOD DOESNT WORK !
#type 3: 
#set1=set(*lst) #effectively set(62,52,82) unpacking is done.

#lets not try more ways for list to set xd.

'''Lets get set to dict'''

# same as list to dict, main diff is set is itself and iterable. Take keys in a list or tuple.

'''Lets get set to list''' 

#list(set_name) and lst=[x for x in set_name] work 

lst2=[]
lst2.extend(set1)
#print (lst2)  #Checking 

#Similar to sets, lists are ordered collections, where the order of elements is preserved. However, when converting a set to a list, the order of the elements can change because sets do not inherently maintain any specific order.

'''Lets get list to tuple'''

tup = tuple(lst)
print(tup) 

tup = (*lst,)
print(tup)

'''Lets get tuple to list''' 

#first method same 

my_tuple = (1, 2, 3, 4, 5)
my_list = [item for item in my_tuple]
print(my_list)

#cant be used vice versa!

#Lists in Python are mutable, meaning that their elements can be modified, added, or removed. They are typically used to store collections of related items that may need to be modified or updated.

#On the other hand, tuples are immutable, meaning that their elements cannot be modified once the tuple is created. Tuples are commonly used to represent collections of values that should not change, such as coordinates or configurations.

'''Lets get tuple to set''' 

my_tuple = (1, 2, 3, 4, 5)
my_set = set(my_tuple)
print(my_set)

my_tuple = (1, 2, 3, 4, 5)
my_set = {item for item in my_tuple}
print(my_set)

'''Lets get set to tuple''' 

my_set = {1, 2, 3, 4, 5}
my_tuple = tuple(my_set)
print(my_tuple)

my_set = {1, 2, 3, 4, 5}
my_tuple = (*my_set,) #set is iterable
print(my_tuple)

'''Lets get dict to list''' 

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_list = list(my_dict.keys())  # Convert keys to a list
value_list = list(my_dict.values())  # Convert values to a list

print(key_list)
print(value_list)

#OR 

my_dict = {'a': 1, 'b': 2, 'c': 3}
pair_list = list(my_dict.items())  # Convert key-value pairs to a list

print(pair_list)

'''Lets get dict to tuple''' 

#SAME AS DICT TO LIST 
#replace list with tuple 


'''Lets get dict to set''' 

set69=set(dict1) 
set69=set(dict1.values())
set69=set(dict1.keys()) #same output without.keys() 

#not printing again, lol


#___________________________________________


#add1, remove1= 62 -> wrong, unpacking needs iterable objects 

add1=remove1=62 #checking out multiple assignments type 1

add2,remove2=89,89 #checking out multiple assignments type 2

add2,remove2=[89]*2 #checking out multiple assignments type 3
#print (add2, remove2) #lets check difference 

[add2, remove2] = [89]*2 #checking out multiple assignments type 4
#print (add2, remove2) #lets check difference

#diff -> no diff

#____________________________________________


def tupcalc(): 

  #tuple is immutable, no append pop etc 
  
  print (tup+(add1,)) #space after print doenst matter
  print(tup+(add2,))

  new_tuple = tuple(item for item in tup if item !=remove1) 
  print(new_tuple)

  new_tuple = tuple(item for item in tup if item !=remove2)
  print(new_tuple)
  
  print() 


def listcalc(): 

  global lst #setting access for global variable
  
  lst.append(add1)
  print(lst)

  lst=list(tup)
  lst.append(add2)
  print(lst)

  #lst.pop(remove1) removes element at index
  #print (lst)

  lst=list(tup)
  lst.remove(remove1)
  print(lst)

  lst=list(tup) #restoring for future use

  #lst=list(tup)
  #lst.remove(remove2) #'ValueError' as not in list
  #print(lst)

  print() 

def setcalc(): 

  
  set1.add(add1)
  print(set1)

  
  #print(set(lst).add(add2)) #direct approach returns none  

  set2=set(list(tup))
  set2.add(add2)
  print(set2)

  set2=set(list(tup))
  set2.remove(remove1) #Raises error 'KeyError' if not present 
  print(set2)

  set2=set(list(tup))
  set2.discard(remove2) #no errors if not present 
  print(set2)

  print()

def dictcalc(): 

  print(dict1) #initial
  dictcopy=dict1
  dictcopy[1] = add1 
  print(dictcopy) 
  
  dictcopy=dict1 
  dictcopy["key2"] = add2 
  print(dictcopy)

  #adding same key and value isnt possible, it'll just update 
  
  dictcopy=dict1 
  del dictcopy[1] #deleting a key
  print (dictcopy)

  my_dict = {"old_key": "value"} # Replacing the key while keeping the value the same
  my_dict["new_key"] = my_dict.pop("old_key")
  print(my_dict) 



tupcalc()
listcalc()
setcalc()
dictcalc()

"""
Conclusive Notes: (Unverified!)

Data Structure	Iterability	Mutability
Set	Yes	Mutable
Tuple	Yes	Immutable
Dictionary	Yes	Mutable
List	Yes	Mutable 

"""

#____________________________________________