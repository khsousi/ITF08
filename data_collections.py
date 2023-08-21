# # my_list =[10,20,30,50,10,15]
#
# # print(max(my_list))
#
# # my_name = "Mohanad"
#
# # def custom_max(my_list:list):
# #     max_number = my_list[0]
# #     for i in my_list:
# #         # print(i,max_number)
# #         if i > max_number:
# #             max_number = i
# #     print("MAx = ",max_number)
# #
# # list_1 = [100,200,300,120]
# #
# # custom_max(list_1)
# # # print(sum(list_1))
# # def custom_sum(my_list):
# #     total = 0
# #     for i in my_list:
# #         total += i
# #     print("Total ",total)
# #
# #
# # def custom_min(my_list:list):
# #     min_number = my_list[0]
# #     for i in my_list:
# #         if i < min_number:
# #             min_number = i
# #     print("Min is ",min_number)
# # custom_sum(list_1)
# # custom_min(list_1)
#
# # mark1 = float(input("Enter Mark 1 :"))
# # mark2 = float(input("Enter Mark 2 :"))
# # mark3 = float(input("Enter Mark 3 :"))
# # mark4 = float(input("Enter Mark 4 :"))
# # mark5 = float(input("Enter Mark 5 :"))
# # my_marks = [mark1,mark2,mark3,mark4,mark5]
# # average = sum(my_marks) / len(my_marks)
#
# # print(average)
# # total = 0
# # my_marks = []
# # marks_count = int(input("Enter Total Number of Marks"))
# # for i in range(0,marks_count):
# #     mark = float(input(f"Enter Mark {i+1} :"))
# #     my_marks.append(mark)
# #
# # average = sum(my_marks) / len(my_marks)
# # average = round(average,2)
# # print(my_marks)
# # print(average)
# # print("Max MArk = ",max(my_marks))
# # print("Min Mark = ",min(my_marks))
#
# # my_list = ["Ali",True,10,50.5]
# # if 'A' in my_list:
# #     print("Yes")
#
# # for i in range(50):
# #     print(i)
# # my_list = []
# # while len(my_list) < 10:
# #     element = int(input("Enter New Element "))
# #     my_list.append(element)
#
# # my_list = [10,20,20,20,30]
# # my_list2 = [100,200,300]
# # my_name = "Ali"
# # my_name =  my_name.replace("A","*") # Immutable
# # print(my_name)
# # my_list.append(15) # Mutable
# # print(my_list)
# # print(my_list)
# # my_list.append(50)
# # print(my_list)
# # my_list.insert(1,60)
# # print(my_list)
# # my_list.remove(20)
# # print(my_list)
# # print(my_list2)
# # my_list.extend(my_list2)
# # print("After Extension",my_list)
# # print("After Extension",my_list2)
#
# my_list = [10,2,1,50,60,7,8,9,130,5]
# # print("Before Sorting ",my_list)
# # my_list.sort(reverse=True)
# # print("After Sorting ",my_list)
# # my_list.reverse()
# # print("After Reversing ",my_list)
# print(my_list)
# my_list.pop()
# print(my_list)
# my_tuple = (10,2,1,50,60,7,8,9,130,5)
# print(my_tuple)
# # print(my_tuple[5])
# # my_tuple.pop()
# # print(my_tuple)
# # for i in my_tuple:
# #     print(i)
# my_set = {10,20,30,10,50,60}
# print(my_set)
# # my_set.pop()
# my_set.add(10)
# # my_set.clear()
# # my_list.clear()
# # print(my_list)
# print(my_set)
#
# students = []
# students_number = int(input("Enter total students number :"))
# for i in range(students_number):
#     student_name = input("Enter your name :")
#     student_age = input("Enter your age :")
#     student = {
#         "name" : student_name,
#         "age" : student_age
#     }
#     marks_number = int(input("Enter total marks number"))
#     marks = []
#     for j in range(marks_number):
#         mark = float(input(f"Enter Student {i+1} mark {j+1} :"))
#         marks.append(mark)
#     student["marks"] = marks
#     average = round(sum(marks) / len(marks) , 2)
#     student["average"] =average
#     student["min_mark"] =  min(marks)
#     student["max_mark"] = max(marks)
#     students.append(student)
#
# for i in students:
#     print(i)


# my_dict = {"name": "Mohanad",
#            "age": 25,
#            "address":{
#                "City" : "Gaza",
#                "Street" : {
#                    "name" : "Alshohada",
#                    "number" : 25
#                }
#            } ,
#            "single" : True,
#            "Blood" : "AB+"
#             }
# print(my_dict)
# del my_dict["address"]
# print(my_dict)
# my_dict["hobbies"] = ["Football","Basketball"]
# print(my_dict)
# print(my_dict)
# print(my_dict['address']['Street']['number'])
# print(my_dict.get('address'))
# for i,j in my_dict.items():
#     print(i)

products = []
while True:
    selection = int(input("1.Add New Product\n2.Print Product Details"
                          "\n3.Buy Product"
                          "\n4.Delete Product"
                          "\n5.Exit"))
    if selection == 1:
        product_number = input("Enter Product Number : ")
        product_name = input("Enter Product Name : ")
        product_price = input("Enter Product Price : ")
        product_qty =  int(input("Enter Product Quantity : "))
        product = {
            "id": product_number,
            "name": product_name,
            "price": product_price,
            "qty": product_qty
        }
        products.append(product)
        print("Product Added Successfully")
    elif selection == 2:
        product_number = input("Enter product number: ")
        for i in products:
            if i['id'] == product_number:
                print(i)
                break
    elif selection == 3:
        print("3")
        # TODO :: input Product Number
        product_number = input("Enter Product Number: ")
        # TODO :: input Quantity as integer
        qty = int(input("Enter Product Quantity: "))
        # TODO :: update quantity after purchase
        for i in products:
            if i['id'] == product_number:
                while True:
                    qty = int(input("Enter Product qty: "))
                    if qty > i['qty'] or qty <= 0:
                        print("Invalid QTY")
                    else:
                        break

                i['qty'] = i['qty'] - qty
                break
    elif selection == 4:
        # TODO :: input Product Number
        product_number = input("Enter Product Number: ")
        # TODO :: delete Product
        for i in products[:]:
            if i['id'] == product_number:
                products.remove(i)
                break
        print(4)
    else:
        exit()
