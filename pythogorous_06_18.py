my_tuple = [3, 4, 5]

pythogorous = False

if pow(my_tuple[0], 2) == pow(my_tuple[1], 2) + pow(my_tuple[2], 2):
  pythogorous = True
  
elif pow(my_tuple[1], 2) == pow(my_tuple[0], 2) + pow(my_tuple[2], 2):
  pythogorous = True

elif pow(my_tuple[2], 2) == pow(my_tuple[1], 2) + pow(my_tuple[0], 2):
  pythogorous = True


print(pythogorous)