import math

def sin_cos():
    x = float(input("Enter a number for sin: "))
    y = float(input("Enter a number for cos: "))
    sin_val = math.sin(math.radians(x))
    cos_val = math.cos(math.radians(y))
    print("sin(", x, ") =", sin_val)
    print("cos(", y, ") =", cos_val)

sin_cos()


def fa():
    x = int(input("Enter a number for factorial: "))
    fa_x = math.factorial(x)
    print("Factorial of", x, "is", fa_x)

fa()


def circle_perimeter():
    x = int(input("Enter a radius: "))
    radius_x = x * 2 * math.pi
    print("The perimeter of your radius,(",x,")=",radius_x)


circle_perimeter()
