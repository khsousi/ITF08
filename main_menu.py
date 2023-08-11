# I'M SORRY FOR THE DELAY.
def add_num():
    num_1 = int(input("Enter First Number: "))
    num_2 = int(input("Enter Second Number: "))
    return num_1+num_2


def subtraction_num():
    num_1 = int(input("Enter First Number: "))
    num_2 = int(input("Enter Second Number: "))
    return num_1-num_2


def multiplication_num():
    num_1 = int(input("Enter First Number: "))
    num_2 = int(input("Enter Second Number: "))
    return num_1*num_2


def division_num():
    num_1 = int(input("Enter First Number: "))
    num_2 = int(input("Enter Second Number: "))
    return num_1/num_2


def triangle():
    length = int(input("Enter length: "))
    base = int(input("Enter Base: "))
    area = (0.5 * base)*length
    return area


def circle():
    radius = int(input("Enter Radius: "))
    area = 3.14 * radius ** 2
    return area


def rectangle():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    return area


while True:

    selection = int(input("1- Sum \n"
                          "2- Subtract\n"
                          "3- Multiply\n "
                          "4- Division\n "
                          "5- Triangle Area\n"
                          "6- Circle Area\n "
                          "7- Rectangle Area\n"
                          "8- Exit\n"
                          "Select Operation: "))

    while True:
        if 8 >= selection >= 1:
            break
        else:
            selection = int(input("Invalid Input, Try Again: "))

    if selection == 1:
        print(add_num())
    elif selection == 2:
        print(subtraction_num())
    elif selection == 3:
        print(multiplication_num())
    elif selection == 4:
        print(division_num())
    elif selection == 5:
        print(triangle())
    elif selection == 6:
        print(circle())
    elif selection == 7:
        print(rectangle())
    elif selection == 8:
        exit()

