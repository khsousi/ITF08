user_name = input("Enter Your Full Name: ")
mobile_number = input("Enter Your Mobile Number: ")
year_of_birth = input("Enter Your Year Of Birth: ")

mobile_number = f'{mobile_number[:3]}-{mobile_number[3:7]}-{mobile_number[7:]}'
# mobile_number = mobile_number[:3] + "-" + mobile_number[3:7] + "-" + mobile_number[7:]

current_year = 2023
user_age = current_year - int(year_of_birth)

mobile_number = mobile_number.split("-")

print(user_name)
print(user_age)
print(mobile_number)
