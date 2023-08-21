
file1 = open('text.txt', 'w')
user_name = input("Enter User Name: ")
age = int(input("Enter User Age: "))
date_of_birth = input("Enter User Date Of Birth: ")
file1.write(f'{user_name }| {age} | {date_of_birth}')

file1.close()