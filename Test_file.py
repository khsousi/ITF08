# name = input("Enter Your Name: ")
# # print(name)
# age = input("Enter Your Age: ")
# # print(age)
# date = input("Enter Your date: ")
# # print(date)
#
# text = f"""My name is {name}
# my age is {age}
# my birhday date is {date} """
#
# print(text)
#
# print(len(name))

a = "Welcome to my python file "
b= len(a)
print(b)
print("o" in a)
if "W" in a:
    print("Yes Its in")

print("w" not in a)
# Slicing
print(a[2:11])
print(a[:9])
print(a[6:])

# capital and small letter
print(a.upper())
print(a.lower())

# Strip for remove white space from beginning and ending
print(a.strip())
print(a.replace("W", "w"))

# The split() method returns a list
print(a.split(" "))

