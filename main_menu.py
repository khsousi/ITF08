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


while True:
    selection = int(input("1- Sub \n"
                          "2- Subtract\n"
                          "3- Multiply \n "
                          "4- Division \n "
                          "5- Exit \n "
                          "Enter Number: "))
    if selection == 1:
        print(add_num(num1, num2))
    elif selection == 2:
        print(subtraction_num(num1, num2))
    elif selection == 3:
        print(multiplication_num(num1, num2))
    elif selection == 4:
        print(division_num(num1, num2))
    elif selection == 5:
        exit()
