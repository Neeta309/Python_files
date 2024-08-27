vehicle = input("Pick a vehicle: \n1. mega cycle\n2. mega kart\n")
speed = 5
acceleration = 5

#Players unlock mega vehicles by winning a race on every course.
if vehicle == "mega cycle":
  acceleration = acceleration + 4
elif vehicle == "mega kart":
  speed = speed + 2
  acceleration = acceleration + 2
else:
  print("Choose a valid vehicle.")
  
print("The "+ vehicle + " has "+ str(speed)+" speed and "+ str(acceleration)+" acceleration.")
  
