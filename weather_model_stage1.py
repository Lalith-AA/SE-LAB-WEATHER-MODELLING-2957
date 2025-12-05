import math

# Hardcoded coefficients
a = 1.2
b = -3.4
c = 2.1

discriminant = b*b - 4*a*c

if discriminant < 0:
    print("No real solutions (complex weather state)")
else:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Weather State Solutions:")
    print("x1 =", x1)
    print("x2 =", x2)
