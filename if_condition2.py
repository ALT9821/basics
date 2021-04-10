num = 12
if num >= 1 and num <= 10:
    print(f"number is equal or greater than 1 and less that 10")
else:
    print(f"number is less than 1 or greater than 10")

#expression AND/OR expression AND/OR expression

#OR:
#expression OR expression = True or Fale =
#where Country = 'UK or country = 'USA'>> True or False


age = int(input('enter the visitor age: '))
if 0 <= age <= 4:
    print(" your admission is $0")
elif 4< age < 18:
    print("your admission is $5")
elif 18<= age < 140:
    print(" your admission is $10")
else:
    print("invalid age was entered")

print("--------second---------")

age = int(input('enter the visitor age: '))
price = 0
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 140:
    price = 10
else:
    print("Invalid age was entered")
print("-----------Three----------")

alien_color = input('enter the alien color - (green/yellow/red):')
if alien_color == 'green':
    print(f"you just earned 5 points")
elif alien_color == 'yellow':
    print(f"youjust earned 2 points")
elif alien_color == 'red':
    print(f"youjust earned 10 points")
else:
    print(f"sorry no points you lose")

print("-----test-----")
numbers = [2, 3, 4, 6]

numbers_sum = sum(numbers)
print(numbers_sum)


num= int(input('enter the number:'))
  if num % 3 == 0 and num % 5 == 0:
    print("FuzzBuzz")
  elif num % 3 == 0:
    print("Fuzz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print("num")


