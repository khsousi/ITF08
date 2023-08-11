# I'M SORRY FOR THE DELAY.

num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))


def add_num(num_1, num_2):
    return num_1+num_2


def subtraction_num(num_1, num_2):
    return num_1-num_2


def multiplication_num(num_1, num_2):
    return num_1*num_2


def division_num(num_1, num_2):
    return num_1/num_2


def triangle(heigh, base):
    area = (0.5*base)*heigh
    return area


def circle(radius):
    area = 3.14 * radius ** 2
    return area


def rectangle(length, width):
    area = length * width
    return area


while True:

    selection = int(input("1- Sub \n"
                          "2- Subtract\n"
                          "3- Multiply\n "
                          "4- Division\n "
                          "5- Triangle Area\n"
                          "6- Circle Area\n "
                          "7- Rectangle Area\n"
                          "8- Exit\n"
                          "Select Operation: "))
    while True:
        if selection <= 8 and selection >= 1:
            break
        else:
            selection = int(input("Invalid Input, Try Again: "))

    if selection == 1:
        print(add_num(num1, num2))
    elif selection == 2:
        print(subtraction_num(num1, num2))
    elif selection == 3:
        print(multiplication_num(num1, num2))
    elif selection == 4:
        print(division_num(num1, num2))
    elif selection == 5:
        print(triangle(heigh=num1, base=num2))
    elif selection == 6:
        print(circle(radius=num1))
    elif selection == 7:
        print(rectangle(length=num1, width=num2))
    elif selection == 8:
        exit()

