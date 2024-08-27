from itertools import permutations

def allPermutations(str):
  #Get all permutations of string 'ABC'
  permList = permutations(str)
  
  for perm in permList:
    print(''.join(perm))
    

