planet = "Mars"

#We measure a planet's gravitional force in m/s^2.
mars_gravity = 3.7
earth_gravity = 9.81

earth_weight = float(input("How much does it weigh on Earth (kg) ?"))

#An object's weight = mass * gravity

mass = earth_weight / earth_gravity
new_weight = round(mass * mars_gravity, 2)

print("It would weigh "+ str(new_weight) + " kg on "+ planet + ".")