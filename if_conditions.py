# If statements
#if expression:
#    code here when expression is ture
#else:
#    code here when expression is false

num1 = 2
num2 = 3
if num1<num2:
    print("expression is true")
else:
    print("expression is false")
print("if statement is complete")

print("------------")
if num1 == num2:
    print("expression is true")
else:
    print("expression is false")
print("if statement is complete")

print("-----input strings integers-------")
num3_str = input("enter the num4: ")
num3 = int(num3_str)
num4 = 3
if num3 == num4:
    print("expression is true")
else:
    print("expression is false")
print("if statement is complete")

print("------------")
num = 5
if num in range(6):
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")

print("------sixth----")
msg = input("enter the number")
if msg.strip() != '':
    print(f" this message was enetered: \n '{msg}'")
else:
    print("white space was entered")


print("-----------------count------------")
nums = [45, 4, 5, 6, 3, 10, 5, 123, 346, 4, 5, 666, 5]
cnt = 0
for num in nums:
    if num == 5:
        cnt = cnt + 1
print(cnt)




domestic_cars = ['camaro, corvette, mustang, firebird, jeep, cadillac, ']
foreign_cars = ['audi', 'bmw', 'mercedes', 'lexus', 'acura']
for car in domestic_cars:
    if car == 'mercedes':
        print('true')
else:
    print('false')