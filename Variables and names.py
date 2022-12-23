cars = 100
space_in_a_car = 6
drivers = 35
passanger =105
cars_not_driven = cars - drivers
cars_driven = drivers
carspool_capacity = cars_driven * space_in_a_car
average_passanger_per_car = passanger/cars_driven

print ("There are total", cars,"cars" )
print ("Each car has space for", space_in_a_car,"people" )
print ("There are only", drivers,"drivers available")
print ("There will be",cars_not_driven,"empty cars today")
print ("We can transport",carspool_capacity,"passangers")
print ("And we have",passanger,"passangers")
print ("So we need to put ",average_passanger_per_car,"passangers in each car")