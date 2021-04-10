fullname = "john doe"
msg = "we are looking at strings"
msg1 = fullname + ", " + msg
msg2 = fullname.upper() + "n\t\t," + msg
msg3 = '\n\t\t\t' + fullname.upper() + ", " + msg
msg4 = f"{fullname.upper()},{msg} "

print(fullname)
print(fullname.upper())
print(msg.replace('we','you'))
print(msg1)
print(msg2)
print(msg3)
print(msg3.strip() + '!!!')

num1 = 500
num2 = 600

print(f"num1 + num2 = {num1 + num2}")
print(f"num1 - num2 = {num1 - num2}")
print(f"num1 * num2 = {num1 * num2}")
print(f"num1 / num2 = {num1 / num2}")

quote = '\t\t\tA wise man once said "An apple a day \n\t\t\tkeeps the doctor away"'

print(quote)

#str
print("value of number is : " + str(num))
print(f"3**2 = {3**2}")
Print(int(45.4988))

cars = ['bmw', 'audi', 'toyota', 'subaru']
sorted_cars = sorted(cars)
print(f"cars: {cars}")
Print(f"sorted_cars: {sorted_cars}")
Print(f"sorted_cars_asc: {sorted_cars_asc}")
Print(f"sorted_cars_desc: {sorted_cars_desc}")