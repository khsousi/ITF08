def tringle():
    height = int(input("Enter Num1: "))
    base = int(input("Enter Num2: "))
    tringle_area = (0.5*base)*height
    return tringle_area


print(tringle())


def circle():
    radius = int(input("Enter radius: "))
    circle_area = 3.14 * radius**2
    return circle_area


print(circle())


def rectangle():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area_rectangle= length * width
    return area_rectangle


print(rectangle())
