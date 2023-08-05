def scan(area):
    if area >= 10:
        print("its big")
    elif area < 0:
        print("its invalid")
    else:
        print("its small")


def tringle(height, base):
    area = (0.5 * base) * height
    scan(area)

def circle(radius):
    area = 3.14 * radius ** 2
    scan(area)


def rectangle(length, width):
    area = length * width
    scan(area)


tringle(3, 3)
circle(5)
rectangle(5, 10)




