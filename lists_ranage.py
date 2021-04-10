cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for num in range(4):
    print(num)

nums = range(4)
nums2 = list(range(4))

print(nums)
print(nums2)

print("range with start and stop---")
for num in range(1, 4):
    print(num)

print("range with start and stop---")
for num in range(1, 20, 3):
    print(num)

print("all even number from 1 to 16(16 should be included)")
for num in range(0, 17, 2):
    print(num)

evens = []
for num in range(0, 17, 2):
    print(num)

print(evens)
for num in range(2, 17, 2):
    print(num)
    evens.append(num)
    print(evens)

print(f"this is the final list: {evens}")

squares = list()
for num in range(10, 21):
    squares.append(num ** 2)
    # print(num*num)
print(squares)
print(f"final list: {squares}")
print(f"min(squares): {min(squares)}")
print(f"max(squares): {max(squares)}")
print(f"sum(squares): {sum(squares)}")

cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
cars_len = len(cars)
for car in cars:
    print(cars)
    print(f"index of the {car} is {cars.index(car)} ")
print("looping the list using index")

for ind in range(4):
    print(ind)
    print(f'index of the {cars[ind]} is {ind}')

# list comprehension
print("# list comprehension : ")
squares = list()
for num in range(10, 21):
    squares.append(num ** 2)
squares = [num ** 2 for num in range(10, 21)]

# Generate numbers between 0 to 6
for i in range(6):
    print(i)

print("****************************")
print("excersise One Million: ****************")
nums = []
for num in range(1, 1001):
    print(num)
    nums.append(num)
print(nums)
print(f"smallest: {min(nums)}")
print(f"biggest: {max(nums)}")
print(f"total: {sum(nums)}")
