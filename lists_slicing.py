# 3/13/2021
# workin with part of the list

cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars[1:3]:
    print(f"the car is: {car}")

print("---------second-------")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars[:3]:
    print(f"the car is: {car}")

print("---------third-------")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars[2:]:
    print(f"the car is: {car}")

print("---------fourth-------")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars[2:]:
    print(f"the car is: {car}")
print("---------Copying and linking----------")
print("---------Copying and linking the same values----------")
cars2 = cars
print(f"cars: {cars}")
print(f"cars2: {cars2}")
cars.append('bmw')
print(f"cars update: {cars}")
print(f"cars2 update: {cars2}")

print("---------Copying----------")
cars3 = cars[:]
print(f"cars: {cars}")
print(f"cars3: {cars3}")
cars.append('toyota')
print(f"cars: {cars}")
print(f"cars3: {cars3}")
print(f"cars2: {cars2}")
cars4 = cars[:]
print(f" cars 4 is now the same as cars3append: {cars4}")

print("exercise 4-10: slicing")
print(f"the first three items in the list are: {cars[:3]}")
print(f"the first three items from the middle list are: {cars[2:5]}")
print(f"the last three items in the list are: {cars[3:]}")

# lists can be modified
# Tuples are similar to lists but cannot be modified
# use parenthesis not brackets
print('------tuples------')
cars_t = ('bugatti', 'ferrari', 'tesla', 'lexus')
print(f"first value is: {cars_t[0]}")
cars[0] = 'honda'
print(f"cars_t tuple: {cars_t}")
cars_t = ('honda', 'ferrari', 'tesla')
print(f" cars")
