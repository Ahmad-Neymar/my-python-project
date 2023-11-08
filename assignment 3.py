#data types/type casting

a=(input("enter number:"))
print("interger =", a)
print("converted number =",float(a))


# strings to integer conversion
a ="3"
b =int(a)+10
print(b)

# floating-point division
x=float(input("enter first number:"))
y=float(input("enter second number:"))
z=x/y
print(z)

try:
    number = int(input("enter a number:"))
    print("converted to integer:", number)
except ValueError:
    print("error: can not be converted")


import math
float_input = float(input("enter a floatingpoint number:"))
integer = int(float_input)
square = integer**2
print(float_input)
print(square)
