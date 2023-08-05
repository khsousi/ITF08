def tringle():
    height = int(input("Enter Num1: "))
    base = int(input("Enter Num2: "))
    area = (0.5*base)*height
    return area


print(tringle())


def circle():
    radius = int(input("Enter radius: "))
    area = 3.14 * radius** 2
    return area


print(circle())


def rectangle():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    return area


print(rectangle())
