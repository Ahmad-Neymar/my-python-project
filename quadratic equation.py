#quadratic equation
import cmath
print("quadratic formula:ax**2+bx+c=0")
a=int(input("enter number:",))
b=int(input("enter nunmber:",))
c=int(input("enter number:",))
d=-b
e=b**2
f=4*a*c
g=2*a
h=e-f
i= cmath.sqrt(h)
j=d+i
k=d-i
print("x="+ str(j/g))
print("x="+str(k/g))