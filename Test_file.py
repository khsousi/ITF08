# # name = input("Enter Your Name: ")
# # # print(name)
# # age = input("Enter Your Age: ")
# # # print(age)
# # date = input("Enter Your date: ")
# # # print(date)
# #
# # text = f"""My name is {name}
# # my age is {age}
# # my birthday date is {date} """
# #
# # print(text)
# #
# # print(len(name))
#
# a = "Welcome to my python file "
# b = len(a)
# print(b)
# print("o" in a)
# if "W" in a:
#     print("Yes Its in")
#
# print("w" not in a)
# # Slicing
# print(a[2:11])
# print(a[:9])
# print(a[6:])
#
# # capital and small letter
# print(a.upper())
# print(a.lower())
# print(a.title())
#
# # Strip for remove white space from beginning and ending
# print(a.strip())
# print(a.replace("W", "w"))
#
# # The split() method returns a list
# print(a.split(" "))
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))
# txt2 = f"My name is john, and I am {age}"
# print(txt2)
#
# print(10 > 11)
#
# Age = input("Enter Your Age: ")
# def my_age(age):
#     print("My Age = " + Age)
#
#
# my_age(Age)


# def add(num_1, num_2):
#     return num_1 + num_2
#
#
# print(add(100, 15))
#

# for i in range(0, 101):
#     if i % 2 == 0:
#         print(i)
#
#
# for x in range(0, 101, 3):
#     print(x)


# def tringle(heigh, base):
#     area = (0.5*base)*height
#     return area
#
# print(tringle(heigh,base))


# def rectangle():
#     length = int(input("Enter length: "))
#     width = int(input("Enter width: "))
#     area = length * width
#     return area
#
#
# print(rectangle())

# even_sum = 0
# odd_sum = 0
# for i in range(12, 38):
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i
#
# print(f"Even Numbers Sum={even_sum}")
# print(f"Odd Numbers Sum={odd_sum}")
# #
#
# for i in range(1, 21):
#     if i % 2 == 0 or i % 3 == 0:
#         continue
#     else:
#         print(i)

# num = int(input("Enter Any Number: "))
#
# for i in range(1, 11):
#     print(num, "*", i, "=", num*i)
#

# def summ(num1, num2):
#     summ = num1 + num2
#     if summ in range(10, 21):
#         return 10
#     else:
#         return summ
#
#
# print(summ(5, 50))


# def test(x, y):
#     summ = x+y
#     diff = x-y
#     if x != y or summ == 7 or diff == 6:
#         return True
#     else:
#         return False
#
# print(test(5,8))


# def calc(n1, n2, n3):
#     summ = n1 + n2 + n3
#     if n1 == n2 == n3:
#         # return summ*3
#         summ *= 3
#         return summ
#     else:
#         return summ
#
# print(calc(1,2,3))
# print(calc(3,3,3))


# import calendar
# year = int(input("Enter the Year: "))
# month = int(input("Enter the Month: "))
# print(calendar.month(year, month))

my_list = ["apple", "banana", "cherry", 55, True]
print(my_list)
print(len(my_list))
print(type(my_list))
