import math
def quad(a,b,c):
    d = b
    e = b ** 2
    f = 4 * a * c
    g = 2 * a
    h = e - f
    i = math.sqrt(h)
    j = -d + i
    k = -d - i
    print("x=" + str(j / g))
    print("x=" + str(k / g))
quad(2,6,4)






