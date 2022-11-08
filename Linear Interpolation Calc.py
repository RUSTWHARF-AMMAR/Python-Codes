#Linear Interpolation Calc
from doctest import script_from_examples
from sys import argv

script = user_name = argv
h = 0
v = 0
def interpolation(x1, y1, x2, y2, x):
    y = y1 + ((x - x1)*((y2 - y1)/(x2 - x1)))
    return(y)

print("What is the thing you are trying to interpolate?")
thing = input()

if thing == 'v':
    print("v for specific vol")
    a1 = int(input("val 1 "))
    b1 = int(input("v1 "))
    a2 = int(input("val 2 "))
    b2 = int(input("v2 "))
    a = int(input("val "))
    ansv = interpolation(a1, b1, a2, b2, a)
    print("%s" %ansv)
elif thing == 'h':
    print("h for entalpy")
    h = 1
elif thing == 'P':
    print("P for pressure")
    P = 1
elif thing == 'T':
    print("T for temp (C)")
    T = 1
else:
    print("invalid")

print("Save values as upper/Lower bounds?")
thing2 = input()

if thing2 == 'y':
    upper = int(input("Upper: "))
    lower = int(input("Lower: "))

    interpolation()

else:
    print("Bye")
