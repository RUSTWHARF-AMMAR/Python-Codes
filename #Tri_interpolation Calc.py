#Tri_interpolation Calc

def interpolation(x1, y1, x2, y2, x):
    y = y1 + ((x - x1)*((y2 - y1)/(x2 - x1)))
    return(y)

print("This is the tri-interpolation calc")
print("form: find upper, lower bounds, then interpolate for final val")
print("first lower bound")
x1L = float(input("Var 1 known "))
y1L = float(input("Var 1 value "))
x2L = float(input("Var 2 known "))
y2L = float(input("Var 2 value "))
xL = float(input("Var "))
lower = interpolation(x1L, y1L, x2L, y2L, xL)

print("Upper bounds")
x1U = float(input("Var 1 known "))
y1U = float(input("Var 1 value "))
x2U = float(input("Var 2 known "))
y2U = float(input("Var 2 value "))
xU = float(input("Var "))
upper = interpolation(x1U, y1U, x2U, y2U, xU)

print("reg interpolation values")
lowerx = float(input("lower known "))
upperx = float(input("Upper known "))
x = float(input("Known "))
y = interpolation(lowerx, lower, upperx, upper, x)
print("%s", y)
