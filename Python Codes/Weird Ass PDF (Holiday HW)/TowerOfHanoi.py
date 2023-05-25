def tower_of_hanoi(n, source, destination, auxiliary):
    if n>0: 
      
      tower_of_hanoi(n-1,source, auxiliary, destination)
      print("Move disc ", n , " from peg ", source , "to peg ", destination) 
      tower_of_hanoi(n-1, auxiliary, destination, source) 
      
n = 3  
tower_of_hanoi(n, 'A', 'B', 'C')