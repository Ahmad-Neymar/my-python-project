# Boolean type casting
user_input=input("enter a string containing 'true' or 'false':")
boolean_value = bool(user_input)
negation = not boolean_value
print("boolean value:", boolean_value)
print("negation:", negation)

#type casting with string concatenation
x=input("enter the first number:")
y=input("enter the second number:")
x_str=str(x)
y_str=str(y)
concatenated_string=x_str+y_str
print("contacatenated string:", concatenated_string)

#interger to character conversion
ascii_code=int(input("enter an integer(ascii code):"))
character=chr(ascii_code)
print("character:",character)

#list to string conversion
words= ["hello","hi","facebook","snapchat","friends"]
result="".join(words)
print("result:",result)

#type casting in mathematical operations
x=int(input("enter the first integer:"))
y=int(input("enter the second integer:"))
z=int(input("enter the third integer:"))
average=(x+y+z)/3
average_float=float(average)
print("average:", average_float)
