total = 0
my_marks = []
student_count = int(input("Enter Student Count: "))
marks_count = int(input("Enter Marks Count: "))
for j in range(0, student_count):
    for i in range(0, marks_count):
        mark = float(input(f"Enter mark {i+1}: "))
        my_marks.append(mark)

    average = sum(my_marks) / len(my_marks)
    print(average)
    print(my_marks)

    print(f"Max Mark = {max(my_marks)}")
    print(f"Min Mark = {min(my_marks)}")